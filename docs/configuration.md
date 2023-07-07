## Configuration
The configuration file is located at `~/.config/venture.toml` by default, but can be specified using the `--config` argument

### UI
Configuration for how to render out the choices

- `ui.exec` - Command to execute to display the UI. Will receive the options in their STDIN and should write the user choice to STDOUT (i.e. how rofi behaves). Required
- `ui.seperator` - Character(s) that separate each choice in STDIN. Defaults to newline.
- `ui.format` - Format string that defines how each entry should be sent to the UI
- `ui.response_format` - The format that the response from the UI will be in. Will receive the same tokens as format above. If it is not provided, `ui.format` will be assumed as the default.

#### Optional UI Features
Extensions for particular UI components
- `ui.supports.pango` - The interface being rendered supports pango markup. If enabled, icons can be colored.

### Browse
Configurations for the browse mode

#### Profiles
You define multiple profiles for browse mode that each define their own configuration values. The profile to use is then picked when executing the program.

- `browse.ui` - Default UI for every profile. Reference UI above for options
- `browse.profiles.<name>.ui.format` - Receives 3 arguments:
	- **name** - A unique name for the option derived from the path of the item
	- **path** - The full path of the option
	- **icon** - The icon detected for the filetype
- `browse.profiles.<name>.exec` - Program to execute with user choice. Should be a format string like this: `xdg-open {path}`
- `browse.profiles.<name>.paths` - Array of paths to search through for options
- `browse.profiles.<name>.exclude` - Array of regexes (or globs?) that will filter the list of items discovered from the paths above.
- `browse.profiles.<name>.ui` -  UI configuration for this profile. Reference UI above for options
- `browse.profiles.<name>.show.hidden` - Display hidden files. Defaults to False
- `browse.profiles.<name>.show.files` - Display Files. Defaults to True
- `browse.profiles.<name>.show.directories` - Display Directories. Defaults to True

### QuickLaunch
Settings for the quicklaunch mode

- `quicklaunch.exec` - Global exec command for all quicklaunch entries that do not provide their own one
- `quicklaunch.format` - Format for each entry. It will receive 4 arguments:
	- **name** - Entry name
	- **path** - Entry path
	- **icon** - Entry icon
	- **details** - Entry Details
- `quicklaunch.ui` - Default UI for every profile. Reference UI above for options

#### Quicklaunch Entries
An array of items to render for the quicklaunch
- `quicklaunch.entires[].name` - Human readable name for the item
- `quicklaunch.entires[].exec` - Command to execute when this option is picked. This or path (or both) must be provided
- `quicklaunch.entires[].path` - Path to the item
- `quicklaunch.entires[].icon` - Optional icon to display alongside the name of the item
- `quicklaunch.entires[].details` - String of additional details that can be rendered with your options
- `quicklaunch.entires[].format` - Format specifier for this specific entry. same arguments as above

### Configuration Example
```toml
[browse.ui]
exec = "rofi -dmenu -theme venture.rasi -markup-rows"
format = "{icon} {name}"
supports.pango = true

[browse.profiles.code]
exec = "code -r {path}"
paths = [
	"~/sourcecode",
	"~/sourcecode/school/*"
]

exclude = ["school"]

[quicklaunch]
exec = "code -r {path}"

[quicklaunch.ui]
exec = "rofi -dmenu -theme venture.rasi -markup-rows"
format = "{icon} {name}"
seperator = "|"
supports.pango = true

[[quicklaunch.entries]]
name = "arc"
path = "~/sourcecode/arc"
icon = ":py:"
details = ":py: python"

[[quicklaunch.entries]]
name = "Sway"
path = "~/.config/sway/config"
icon = "\uF2D2"
details = ":config: config"

[[quicklaunch.entries]]
name = "Venture"
path = "~/sourcecode/venture"
icon = "\uE771"
details = ":py: python"

```
