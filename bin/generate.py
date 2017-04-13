"""Generates a vim color theme."""
from functools import partial, reduce


N = "None"
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

DARK_THEME = [
    ("Normal", "background", "foreground", N),
    ("Visual", "background", "foreground", "Reverse"),
    ("Comment", N, "comment", N),
    ("Constant", N, N, N),
    ("String", N, "string", N),
    ("Character", N, "string", N),
    ("Identifier", N, N, N),
    ("Statement", N, "standout", "Bold"),
    ("PreProc", N, "standout", "Bold"),
    ("Type", N, "standout", "Bold"),
    ("Special", N, N, N),
    ("Underlined", N, N, "Underline"),
    ("Ignore", N, N, N),
    ("Error", "error", N, N),
    ("Todo", "warning", "background", N),
    ("ColorColumn", "standback", "foreground", N),
    ("Cursor", N, N, "Reverse"),
    ("CursorLine", "standback", N, N),
    ("Directory", "background", "foreground", "Underline"),
    ("ErrorMsg", "error", N, N),
    ("VertSplit", "chrome", "chrome", N),
    ("Folded", N, N, N),
    ("FoldColumn", N, "comment", N),
    ("SignColumn", N, "error", N),
    ("IncSearch", "highlight", "background", N),
    ("LineNr", N, "comment", N),
    ("CursorLineNr", N, "comment", "Bold"),
    ("MatchParen", N, N, "Reverse"),
    ("Pmenu", "standback", "highlight", N),
    ("PmenuSel", "standback", "highlight", "Reverse"),
    ("PmenuSbar", "standback", "standback", N),
    ("PmenuThumb", "chrome", "chrome", N),
    ("Search", "highlight", "background", N),
    ("SpecialKey", N, "highlight", N),
    ("SpellBad", "error", N, N),
    ("SpellCap", "warning", "background", N),
    ("StatusLine", "chrome", "very_standout", "Bold"),
    ("StatusLineNC", "chrome", "foreground", N),
    ("TabLine", "chrome", "foreground", N),
    ("TabLineFill", "chrome", "foreground", N),
    ("TabLineSel", "background", "very_standout", "Bold"),
    ("Title", N, N, "Bold"),
    ("WarningMsg", "error", N, N),
]

LIGHT_PALETTE = {
    "background": "255",
    "foreground": "234",
    "string": "031",
    "highlight": "031",
    "comment": "245",
    "error": "160",
    "warning": "226",
    "chrome": "249",
    "standback": "254",
    "standout": "233",
    "very_standout": "000"
}

LIGHT_THEME = [
    ("Normal", "background", "foreground", N),
    ("Visual", "background", "foreground", "Reverse"),
    ("Comment", N, "comment", N),
    ("Constant", N, N, N),
    ("String", N, "string", N),
    ("Character", N, "string", N),
    ("Identifier", N, N, N),
    ("Statement", N, "standout", "Bold"),
    ("PreProc", N, "standout", "Bold"),
    ("Type", N, "standout", "Bold"),
    ("Special", N, N, N),
    ("Underlined", N, N, "Underline"),
    ("Ignore", N, N, N),
    ("Error", "error", N, N),
    ("Todo", "warning", "foreground", N),
    ("ColorColumn", "standback", "foreground", N),
    ("Cursor", N, N, "Reverse"),
    ("CursorLine", "standback", N, N),
    ("Directory", "background", "foreground", "Underline"),
    ("ErrorMsg", "error", N, N),
    ("VertSplit", "chrome", "chrome", N),
    ("Folded", N, N, N),
    ("FoldColumn", N, "comment", N),
    ("SignColumn", N, "error", N),
    ("IncSearch", "highlight", "foreground", N),
    ("LineNr", N, "comment", N),
    ("CursorLineNr", N, "comment", "Bold"),
    ("MatchParen", N, N, "Reverse"),
    ("Pmenu", "standback", "highlight", N),
    ("PmenuSel", "standback", "highlight", "Reverse"),
    ("PmenuSbar", "standback", "standback", N),
    ("PmenuThumb", "chrome", "chrome", N),
    ("Search", "highlight", "background", N),
    ("SpecialKey", N, "highlight", N),
    ("SpellBad", "error", "background", N),
    ("SpellCap", "warning", "foreground", N),
    ("StatusLine", "chrome", "foreground", "Bold"),
    ("StatusLineNC", "chrome", "very_standout", N),
    ("TabLine", "chrome", "foreground", N),
    ("TabLineFill", "chrome", "foreground", N),
    ("TabLineSel", "background", "foreground", "Bold"),
    ("Title", N, N, "Bold"),
    ("WarningMsg", "error", N, N),
]


def to_rule(palette, group, background, foreground, term):
    """Returns a tuple containing the a highlight function call and its arguments."""
    return (
        "hi",
        group,
        "ctermbg={}".format(palette.get(background, background)),
        "ctermfg={}".format(palette.get(foreground, foreground)),
        "cterm={}".format(palette.get(term, term)))


def tuple_width(tup):
    """Returns the lengths of all the strings in a tuple."""
    return tuple(len(i) for i in tup)


def tuple_max(left, right):
    """Returns a tuple containing the max value at each index between two tuples."""
    return tuple(max(a, b) for (a, b) in zip(left, right))


def get_max_widths(tuples):
    """Returns a tuple containing the max value at each index in a list of tuples."""
    return reduce(tuple_max, map(tuple_width, tuples))


def get_format_string(max_widths):
    """Returns a format string for writing out a value with a given width."""
    return " ".join(("{{{0}:{1}}}".format(n, w) for (n, w) in enumerate(max_widths)))


def print_rules(rules, indent):
    """Prints out a list of rules in tabular format with a given indent."""
    max_widths = get_max_widths(rules)
    format_string = get_format_string(max_widths)

    for rule in rules:
        print(indent + format_string.format(*rule).strip())


def get_rules(theme, palette):
    """Returns a list of rule tuples based on a theme and palette."""
    rule = partial(to_rule, palette)
    return [rule(group, bg, fg, term) for (group, bg, fg, term) in theme]


def main():
    """Main entry point for script."""
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
    # print_dark_only()
    print_dark_and_light()


def print_dark_and_light():
    """Prints the dark and light color themes."""
    indent = "  "
    dark_theme = get_rules(DARK_THEME, DARK_PALETTE)
    light_theme = get_rules(LIGHT_THEME, LIGHT_PALETTE)

    print('if &background == "light"')
    print_rules(light_theme, indent)
    print("else")
    print_rules(dark_theme, indent)
    print("endif")


def print_dark_only():
    """Prints the dark theme only."""
    indent = ""
    dark_theme = get_rules(DARK_THEME, DARK_PALETTE)
    print("set background=dark")
    print_rules(dark_theme, indent)


if __name__ == "__main__":
    main()
