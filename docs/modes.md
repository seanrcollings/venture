# Modes
Venture centers around two modes, Browse Mode and Quick Launch Mode

# Browse Mode
Browse mode is what you see when just executing `venture`. It reads in the paths listed in the `entries` in the browse section of the config file and generates an output of directories and files for the user to pick from.

## How to structures `entries`
Imagine we have this file structure
```
example
├── python
│   ├── A
│   ├── B
│   └── C
└── rust
    ├── A
    ├── B
    └── C
```

## Simple String Entries
Given a simple string, venture will assume it to be a path to a directory whose contents you want displayed in the menu. So with this config
```yaml
entries:
  - example
```
Venture would display this:
```
python
rust
```
If you wanted to also display the contents of the `rust` directory, you could add it to the entries list as a new entry.
```yaml
entries:
  - example
  - example/rust
```
```
python
rust
A
B
C
```

Notice that in doing this, we lose any hierarchy between the example and rust directory. If that's what you want, that's fine, but the `dict` syntax below allows us to preserve this relationship.

Note that venture gurantees that all names in the listing are unique. So if you add the python directory, even though there are names shared between it and rust directory, they will all be displayed. It does this by advancing up the file tree one level at a time until it finds a unique path.
```
python
rust
A
B
C
python/A
python/B
python/C
```
No Collisions!

## More Complicated entries

Given a dictionary, it will assume this syntax:
```YAML
base: example
subs: # Subs being subdirectories of the ^ base directory
- rust
- python
```
This perserves the relationship between the parent directory `example` and it's sub directories. With the above configuration the list will look something like this:
```
rust
python
rust/A
rust/B
rust/C
python/A
python/B
python/C
```
Each subdirectory listing will be namespaced with respect to the base directory. In this circumstance, if you don't want to display the parent directories (in this case `rust` and `python`), then you can do so by setting `include_parent_folder` to false in the config

## Globs
If any path ends in a glob pattern: `/*`, then it will display everything in that directory, and everything in each of it's sub directories.
```YAML
entries:
    - example/*
```
Will produce very similar output as above
```
rust
python
rust/A
rust/B
rust/C
python/A
python/B
python/C
```
The difference being that the glob will automatically include another sub directory in the listing, whereas the `dict` syntax will only open sub directories explicitly given in the list.

# Quick Launch Mode
The quick-launcher allows you to add specific files / directories to it for easy searchable access.

### Excute
```
$ venture quicklaunch
```

### Add an entry
Entries are added to `~/.config/venture.yml`
```
$ venture quicklaunch:add \
        name=ARC \
        path=~/sourcecode/arc \
        icon=\uF625 \
        tags=:py:,project
```
Possible Arguments:
- `name`: What name to display in the quick-launch menu
- `path`: Filepath to open on selection
- `icon`: Icon to display along side the name **optional**
- `tags`: comma-seperated list of strings to display along with the title. **optional**
- `--no-default-tags`: Disables Venture's automatic tag detection / creation
- `--icon-only`: Ventur's automatic tags will contain only an icon.

Both the `icon` and `tags` arguments parse [icon-strings](./icons.md)