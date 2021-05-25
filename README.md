# Venture

A Rofi / Wofi menu to open projects and files in your favorite editor!


## Installation
Clone the project. And install with

```
$ pip install ./venture
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
# the directory of file that the user selected.
exec: code -r {path}
# Whether or not to display files
show_files: true
# Whether or not to display dotfiles
show_hidden: false
# Whether or not to display an icon of the file type
show_icons: true
# Which external command to use for the UI either rofi or wofi
ui_provider: rofi
# Configuration for Wofi.
# Allows keys 'config' and 'stylesheet'
# and expects file paths to those
wofi: {}
# Configuration for Rofi
# Allows key 'theme' which
# points to a file path for your rofi theme
rofi: {}
```

