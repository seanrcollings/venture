# Wofi Projects Menu

# TODO
- `wofi-projects` is a lame name
  - Plus, I might write multiple UI frontends (curses, rofi), so it wouldn't be accurate
- How to handle name collisions?
  - Just let them happen (maybe log them somewhere?)
  - Force everything to be namespaced to some extent
  - Have some other way to distinguish between two of the same name (not great, would make it hard as a user)
- Formalize a list of configuration options I *defo* want to include
- Find a comprehensive list of nerd font icons to file name mapping
- Allow for file paths to use shell-like expansion (i.e. ~ = /home/<current_user>)
- Considering caching the list of projects for (maybe) better performance