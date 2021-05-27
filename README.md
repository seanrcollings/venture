# Venture

A Dmenu / Rofi / Wofi menu to open projects and files in your favorite editor!



### Dependancies
Venture supports three UI providers: dmenu, rofi, and wofi. It is expected that you have the one you intend to use installed.

## Installation

```
$ pip install venture
```

## Configuration
While not required, you can generate a deafult config with this command
```
$ venture dump
```
This will create a file `~/.config/venture.yaml`


```yaml
# The Entry Points for Venture. Venture will list each sub-directory or file
# for the given directories.
directories:
- '~' # Simple String syntax for a directory
# If you have a primary directory you want to list, but then multiple
# sub-directories within the main directory that need to also be listed,
# the below syntax can be used
- base: ~/sourcecode
  sub:
    - rust # this would resolve to ~/sourccode/rust/...
    - python
    - ruby
    - work
# Venture also accepts a simple glob pattern. This would be equivelant to listing out each of the sub-directories as entry points manually.
- ~/sourcecode/school/*
# Command To execute when an option is chosen. Recieve the {path} token which is the absolute path to
# the directory or file that the user selected.
exec: code -r {path}
# Whether or not to display files
show_files: true
# Whether or not to display dotfiles
show_hidden: false
# Whether or not to display an icon of the file type
show_icons: true
# What provides the UI, currently supports dmenu, rofi, and wofi
ui_provider: rofi
# For all 3 ui providers, you can add a dictionary to pass arbitrary arguments to the command
rofi:
  theme: ~/.config/rofi/theme.rasi

```

## Quick-launcher
The quick-launcher allows you to add specific files / directories to it for easy searchable access.

### Excute
```
venture quicklaunch
```

### Add an entry
Entries are added to `~/.config/venture.yml`
```
venture quicklaunch:add \
        name=ARC \
        path=~/sourcecode/arc \
        icon=\uF625 \
        tags=py,project
```
Possible Arguments:
- `name`: What name to display in the quick-launch menu
- `path`: Filepath to open on selection
- `icon`: Icon to display along side the name **optional**
- `tags`: comma-seperated list of strings to display along with the title. **optional**
- `--no-default-tags`: Disables Venture's automatic tag detection / creation
- `--disable-short-tags`: Disables Venture's tag shorthand matching.
  - enabled: `tags=py` would result in: `[\uF81F python]`
  - disabled: `tags=py` would result in: `[py]`