# Icons
Venture uses [Nerdfonts](https://www.nerdfonts.com/#home) glyphs to render icons. You'll want to download one of their patched fonts and use it for parts of Venture to look correct.

The full set of icons that venture supports can be found [here](../src/venture/icons.py)

## Rendering Icons
To have venture render out an icon for the `icon` or `tag` field of a quick-launch item, you can use this syntax

```
:py: cool-tag
```
This would result in a small python logo, and then the text cool-tag. The string to use in between the two colons is usually just the filename of whatever you want to display, but there are some exception.

## Bar Syntax
Optionally, icons can also be rendered using bars instead of colons. The only difference being that using bars also adds a longer name to the end of the generated string. For example:

```
|py| cool-tag
```

Would result in a python logo, the word "python" and then cool-tag. Essentially, the bar syntax is shorthand for
```
:py: python cool-tag
```