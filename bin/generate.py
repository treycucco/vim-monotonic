from functools import partial, reduce


DARK_PALETTE = {
    "background": "234",
    "foreground": "252",
    "string": "031",
    "highlight": "039",
    "comment": "244",
    "error": "160",
    "warning": "226",
    "chrome": "238",
    "standback": "235",
    "standout": "254",
    "very_standout": "015"
}

LIGHT_PALETTE = {
    "background": "255",
    "foreground": "234",
    "string": "031",
    "highlight": "039",
    "comment": "244",
    "error": "160",
    "warning": "226",
    "chrome": "249",
    "standback": "254",
    "standout": "232",
    "very_standout": "000"
}

def to_rule(palette, group, bg, fg, term):
  return (
      "hi",
      group,
      "ctermbg={}".format(palette.get(bg, bg)),
      "ctermfg={}".format(palette.get(fg, fg)),
      "cterm={}".format(palette.get(term, term)))


def tuple_width(tup):
  return tuple(len(i) for i in tup)


def tuple_max(l, r):
  return tuple(max(a, b) for (a, b) in zip(l, r))


def get_max_widths(tuples):
  return reduce(tuple_max, map(tuple_width, tuples))


def get_format_string(max_widths):
  return " ".join(("{{{0}:{1}}}".format(n, w) for (n, w) in enumerate(max_widths)))


def print_rules(rules, indent):
  max_widths = get_max_widths(rules)
  format_string = get_format_string(max_widths)

  for rule in rules:
    print(indent + format_string.format(*rule).strip())


def get_rules(palette):
  rule = partial(to_rule, palette)
  theme = [
      rule("Normal", "background", "foreground", "None"),
      rule("Visual", "background", "foreground", "Reverse"),
      rule("Comment", "None", "comment", "None"),
      rule("Constant", "None", "None", "None"),
      rule("String", "None", "string", "None"),
      rule("Character", "None", "string", "None"),
      rule("Identifier", "None", "None", "None"),
      rule("Statement", "None", "standout", "Bold"),
      rule("PreProc", "None", "standout", "Bold"),
      rule("Type", "None", "standout", "Bold"),
      rule("Special", "None", "None", "None"),
      rule("Underlined", "None", "None", "Underline"),
      rule("Ignore", "None", "None", "None"),
      rule("Error", "error", "None", "None"),
      rule("Todo", "warning", "background", "None"),
      rule("ColorColumn", "standback", "foreground", "None"),
      rule("Cursor", "None", "None", "Reverse"),
      rule("CursorLine", "standback", "None", "None"),
      rule("Directory", "background", "foreground", "Underline"),
      rule("ErrorMsg", "error", "None", "None"),
      rule("VertSplit", "chrome", "chrome", "None"),
      rule("Folded", "None", "None", "None"),
      rule("FoldColumn", "None", "comment", "None"),
      rule("SignColumn", "None", "error", "None"),
      rule("IncSearch", "highlight", "background", "None"),
      rule("LineNr", "None", "comment", "None"),
      rule("CursorLineNr", "None", "comment", "Bold"),
      rule("MatchParen", "None", "None", "Reverse"),
      rule("Pmenu", "standback", "highlight", "None"),
      rule("PmenuSel", "standback", "highlight", "Reverse"),
      rule("PmenuSbar", "standback", "standback", "None"),
      rule("PmenuThumb", "chrome", "chrome", "None"),
      rule("Search", "highlight", "background", "None"),
      rule("SpecialKey", "None", "highlight", "None"),
      rule("SpellBad", "error", "None", "None"),
      rule("SpellCap", "warning", "background", "None"),
      rule("StatusLine", "chrome", "very_standout", "Bold"),
      rule("StatusLineNC", "chrome", "foreground", "None"),
      rule("TabLine", "chrome", "foreground", "None"),
      rule("TabLineFill", "chrome", "foreground", "None"),
      rule("TabLineSel", "background", "very_standout", "Bold"),
      rule("Title", "None", "None", "Bold"),
      rule("WarningMsg", "error", "None", "None"),
  ]
  return theme


def main():
  print("""" Vim color theme
"
" This file is generated, please check bin/generate.py.
"
" Name:       monotonic
" Maintainer: Trey Cucco
" License:    BSD

hi clear
if exists('syntax_on')
  syntax reset
endif

let g:colors_name = 'monotonic'
""")
  print_dark_only()


def print_dark_and_light():
  indent = "  "
  dark_theme = get_rules(DARK_PALETTE)
  light_theme = get_rules(LIGHT_PALETTE)

  print('if &background == "light"')
  print_rules(light_theme, indent)
  print("else")
  print_rules(dark_theme, indent)
  print("endif")


def print_dark_only():
  indent = ""
  dark_theme = get_rules(DARK_PALETTE)
  print("set background=dark")
  print_rules(dark_theme, indent)


if __name__ == "__main__":
  main()

