# Configuration
Venture's config defaults to `~/.config/venture.yaml`, but this can be overridden with the `VENTURE_CONFIG` environment variable.

## Global Configuration
- `ui: str` - What venture should use to render the UI selection menu. Currently, supports `dmenu`, `rofi`, and `wofi`, but support for other UI providers is planned!
- `args: dict` - A dictionary of values to get passed to the UI Provider of choice as arguments. For example, if your UI of choice was `rofi`, you could provide a theme like this:
    ```YAML
    args:
        theme: "~/.config/rofi/venture.rasi"
    ```
- `exec: str` - A command to execute when the user selects an item. Recieves `path` as a token which is the absolute path to what the user selected. To open VS Code with the file / directory on selection, you would set it it `code {path}`.
- `color_icons: bool` - Whether or not to display the icons in color or in plain white

## Browse Mode
- `entries: list[str | dict]` - List of entrie points that Venture uses to generate the browse menu items. Check [modes.md](./modes.md) for a deep dive on the possible syntax here.
- `exec: str` - Same as the global config, if this isn't present, browse will default to the global value
- `include_parent_folder: bool` - Determines whether or not a sub-folder is considered an entry in the. browse list. Consider the following `entries` configuration
    ```YAML
    browse:
      entires:
        - base: /home/sean/sourcecode
          subs:
          - rust
    ```
    if `include_parent_folder` is false, then the all of the contents of `/home/sean/sourcecode` would be the browse list, along with the contents of `/home/sean/sourcecode/rust`, but not `rust` itself. If `include_parent_folder` is true, then it would be included
- `show_files: bool` - Whether or not to display files
- `show_hidden: bool` - Whether or not to displa hidden files (those beginning with a '.')
- `show_icons: bool`  - Whether or not to display icons based on filetype
- `show_quicklaunch: bool` - Wether or not to add a button to navigate to the Quick Launch mode to the top of the browse menu.
- `use_cache: bool` - Cache the generated menu items for quicker subsequent access. However, when caching, your output will not always be 1-to-1 with the filesystem. I would recommend trying it out with it both on and off and see how it feels. The cache can be forced to update with `venture cache:refresh`

## Quick Launch Mode
- `entires: dict[str, dict[str, str]]` - The items to render in quick-launch mode. You generally don't have to worry about editing this yourself, because `venture quicklaunch:add` will generate the correct syntax for you.
    ### Example
    ```YAML
    ARC: # Name displayed in the menu
      icon: "\uF192" # Icon displayed next to the name (Optional)
      path: /home/sean/sourcecode/arc # Path to execute when selected
      tags:
          - "|py|" # searchable-tags to render for each item. Icon-strings valid here
    ```
- `exec: str` - Same as the global config, if this isn't present, quick-launch will default to the global value
- `show_filepath: bool` - Whether or not to display the filepath of each entry along with the tags.

# Examples
## Default Configuration
```YAML
ui: rofi
args: {}
exec: code -r {path}
color_icons: true
browse:
  entries:
  - '~'
  exec: ''
  include_parent_folder: true
  show_files: true
  show_hidden: false
  show_icons: true
  show_quicklaunch: false
  use_cache: true
quicklaunch:
  entries: {}
  exec: ''
  show_filepath: false
```

## Customized Configuration
```YAML
ui: rofi
exec: code -r {path}
args:
  theme: /home/sean/.config/rofi/venture.rasi
browse:
  entries:
    - base: /home/sean/sourcecode
      subs:
        - rust
        - crystal
        - ComputerScience/*
        - scripts
        - atomicjolt
        - python
  exec: ""
  include_parent_folder: false
  show_files: true
  show_hidden: false
  show_icons: true
  show_quicklaunch: false
  use_cache: false
quicklaunch:
  entries:
    ARC:
      icon: "\uF192"
      path: /home/sean/sourcecode/arc
      tags:
        - "|py|"
    Fish:
      icon: "\uF8DC"
      path: ~/.config/fish/config.fish
      tags:
        - "|fish|"
        - "|config|"
    Mugenmonkey:
      icon: "\uF737"
      path: ~/mugenmonkey-rails
      tags:
        - "|rb|"
        - "|jsx|"
        - "|ts|"
    Qualtrics:
      icon: "\uFAB4"
      path: ~/sourcecode/atomicjolt/qualtrics/
      tags:
        - "|rb|"
        - "|js|"
        - "|ts|"
    Sway:
      icon: "\uF2D2"
      path: ~/.config/sway/config
      tags:
        - "|config|"
    Venture:
      icon: "\uE771"
      path: ~/sourcecode/venture
      tags:
        - "|py|"
        - rofi
  exec: ""
  show_filepath: false
```