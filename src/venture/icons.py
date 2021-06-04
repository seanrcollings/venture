from typing import Optional, NamedTuple

Icon = NamedTuple("Icon", [("code", str), ("color", str)])

# Uses Nerd Fonts Icons
icons: dict[str, Icon] = {
    "html": Icon(code="\uf13b", color="#e44f39"),
    "markdown": Icon(code="\uf853", color="#42a5f5"),
    "css": Icon(code="\uf81b", color="#42a5f5"),
    "css-map": Icon(code="\ue749", color="#42a5f5"),
    "sass": Icon(code="\ue603", color="#ed507a"),
    "less": Icon(code="\ue60b", color="#277bd"),
    "json": Icon(code="\ue60b", color="#fbc13c"),
    "yaml": Icon(code="\ue60b", color="#f4443e"),
    "xml": Icon(code="\uf72d", color="#409945"),
    "image": Icon(code="\uf71e", color="#30a69a"),
    "javascript": Icon(code="\ue74e", color="#ffca3d"),
    "javascript-map": Icon(code="\ue781", color="#ffca3d"),
    "test-jsx": Icon(code="\uf595", color="#23bcd4"),
    "test-js": Icon(code="\uf595", color="#ffca3d"),
    "react": Icon(code="\ue7ba", color="#23bcd4"),
    "react_ts": Icon(code="\ue7ba", color="#248ed3"),
    "settings": Icon(code="\uf013", color="#42a5f5"),
    "typescript": Icon(code="\ue628", color="#388d1"),
    "typescript-def": Icon(code="ﯤ", color="#388d1"),
    "test-ts": Icon(code="\uf595", color="#388d1"),
    "pdf": Icon(code="\uf724", color="#f4443e"),
    "table": Icon(code="\uf71a", color="#8bc34a"),
    "visualstudio": Icon(code="\ue70c", color="#ad63bc"),
    "database": Icon(code="\ue706", color="#ffca3d"),
    "mysql": Icon(code="\ue704", color="#15e86"),
    "postgresql": Icon(code="\ue76e", color="#31638c"),
    "sqlite": Icon(code="\ue7c4", color="#13954"),
    "csharp": Icon(code="\uf81a", color="#277bd"),
    "zip": Icon(code="\uf410", color="#afb42b"),
    "exe": Icon(code="\uf2d0", color="#e54d3a"),
    "java": Icon(code="\uf675", color="#f4443e"),
    "c": Icon(code="ﭰ", color="#277bd"),
    "cpp": Icon(code="ﭱ", color="#277bd"),
    "go": Icon(code="ﳑ", color="#20adc2"),
    "go-mod": Icon(code="ﳑ", color="#ed507a"),
    "go-test": Icon(code="ﳑ", color="#ffd54f"),
    "python": Icon(code="\uf81f", color="#34668f"),
    "python-misc": Icon(code="\uf820", color="#823d1c"),
    "url": Icon(code="\uf836", color="#42a5f5"),
    "console": Icon(code="\uf68c", color="#fa6f42"),
    "word": Icon(code="\uf72b", color="#1579b"),
    "certificate": Icon(code="\uf623", color="#f9593f"),
    "key": Icon(code="\uf805", color="#30a69a"),
    "font": Icon(code="\uf031", color="#f4443e"),
    "lib": Icon(code="\uf831", color="#8bc34a"),
    "ruby": Icon(code="\ue739", color="#e53d3a"),
    "gemfile": Icon(code="\ue21e", color="#e53d3a"),
    "fsharp": Icon(code="\ue7a7", color="#378bba"),
    "swift": Icon(code="ﯣ", color="#f95f3f"),
    "docker": Icon(code="\uf308", color="#187c9"),
    "powerpoint": Icon(code="\uf726", color="#d14733"),
    "video": Icon(code="\uf72a", color="#fd9a3e"),
    "virtual": Icon(code="\uf822", color="#39be5"),
    "email": Icon(code="\uf6ed", color="#42a5f5"),
    "audio": Icon(code="ﭵ", color="#ef5350"),
    "coffee": Icon(code="\uf675", color="#42a5f5"),
    "document": Icon(code="\uf718", color="#42a5f5"),
    "rust": Icon(code="\ue7a8", color="#fa6f42"),
    "raml": Icon(code="\ue60b", color="#42a5f5"),
    "xaml": Icon(code="ﭲ", color="#42a5f5"),
    "haskell": Icon(code="\ue61f", color="#fea83e"),
    "git": Icon(code="\ue702", color="#e54d3a"),
    "lua": Icon(code="\ue620", color="#42a5f5"),
    "clojure": Icon(code="\ue76a", color="#64dd17"),
    "groovy": Icon(code="\uf2a6", color="#29c6da"),
    "r": Icon(code="ﳒ", color="#1976d2"),
    "dart": Icon(code="\ue798", color="#57b6f0"),
    "mxml": Icon(code="\uf72d", color="#fea83e"),
    "assembly": Icon(code="\uf471", color="#fa6d3f"),
    "vue": Icon(code="\ufd42", color="#41b883"),
    "vue-config": Icon(code="\ufd42", color="#3a796e"),
    "lock": Icon(code="\uf83d", color="#ffd54f"),
    "handlebars": Icon(code="\ue60f", color="#fa6f42"),
    "perl": Icon(code="\ue769", color="#9575cd"),
    "elixir": Icon(code="\ue62d", color="#9575cd"),
    "erlang": Icon(code="\ue7b1", color="#f4443e"),
    "twig": Icon(code="\ue61c", color="#9bb92f"),
    "julia": Icon(code="\ue624", color="#86529f"),
    "elm": Icon(code="\ue62c", color="#60b5cc"),
    "smarty": Icon(code="\uf834", color="#ffcf3c"),
    "stylus": Icon(code="\ue600", color="#c0ca33"),
    "verilog": Icon(code="\ufb19", color="#fa6f42"),
    "robot": Icon(code="ﮧ", color="#f9593f"),
    "solidity": Icon(code="ﲹ", color="#388d1"),
    "yang": Icon(code="ﭾ", color="#42a5f5"),
    "vercel": Icon(code="\uf47e", color="#cfd8dc"),
    "applescript": Icon(code="\uf302", color="#78909c"),
    "cake": Icon(code="\uf5ea", color="#fa6f42"),
    "nim": Icon(code="\uf6a4", color="#ffca3d"),
    "todo": Icon(code="\uf058", color="#7cb342"),
    "nix": Icon(code="\uf313", color="#5075c1"),
    "http": Icon(code="\uf484", color="#42a5f5"),
    "webpack": Icon(code="ﰩ", color="#8ed6fb"),
    "ionic": Icon(code="\ue7a9", color="#4f8ff7"),
    "gulp": Icon(code="\ue763", color="#e53d3a"),
    "nodejs": Icon(code="\uf898", color="#8bc34a"),
    "npm": Icon(code="\ue71e", color="#cb3837"),
    "yarn": Icon(code="\uf61a", color="#2c8ebb"),
    "android": Icon(code="\uf531", color="#8bc34a"),
    "tune": Icon(code="ﭩ", color="#fbc13c"),
    "contributing": Icon(code="\uf64d", color="#ffca3d"),
    "readme": Icon(code="\uf7fb", color="#42a5f5"),
    "changelog": Icon(code="ﮦ", color="#8bc34a"),
    "credits": Icon(code="\uf75f", color="#9ccc65"),
    "authors": Icon(code="\uf0c0", color="#f4443e"),
    "favicon": Icon(code="\ue623", color="#ffd54f"),
    "karma": Icon(code="\ue622", color="#3cbeae"),
    "travis": Icon(code="\ue77e", color="#cb3a49"),
    "heroku": Icon(code="\ue607", color="#6963b9"),
    "gitlab": Icon(code="\uf296", color="#e24539"),
    "bower": Icon(code="\ue61a", color="#ef583c"),
    "conduct": Icon(code="\uf64b", color="#cddc39"),
    "jenkins": Icon(code="\ue767", color="#f0d6b7"),
    "code-climate": Icon(code="\uf7f4", color="#eeeeee"),
    "log": Icon(code="\uf719", color="#afb42b"),
    "ejs": Icon(code="\ue618", color="#ffca3d"),
    "grunt": Icon(code="\ue611", color="#fbaa3d"),
    "django": Icon(code="\ue71d", color="#43a047"),
    "makefile": Icon(code="\uf728", color="#ef5350"),
    "bitbucket": Icon(code="\uf171", color="#1f88e5"),
    "d": Icon(code="\ue7af", color="#f4443e"),
    "mdx": Icon(code="\uf853", color="#ffca3d"),
    "azure-pipelines": Icon(code="\uf427", color="#1465c0"),
    "azure": Icon(code="ﴃ", color="#1f88e5"),
    "razor": Icon(code="\uf564", color="#42a5f5"),
    "asciidoc": Icon(code="\uf718", color="#f4443e"),
    "edge": Icon(code="\uf564", color="#ef6f3c"),
    "scheme": Icon(code="ﬦ", color="#f4443e"),
    "3d": Icon(code="\ue79b", color="#28b6f6"),
    "svg": Icon(code="ﰟ", color="#ffb53e"),
    "vim": Icon(code="\ue62b", color="#43a047"),
    "moonscript": Icon(code="\uf186", color="#fbc13c"),
    "codeowners": Icon(code="\uf507", color="#afb42b"),
    "disc": Icon(code="\ue271", color="#b0bec5"),
    "fortran": Icon(code="F", color="#fa6f42"),
    "tcl": Icon(code="\ufbd1", color="#ef5350"),
    "liquid": Icon(code="\ue275", color="#28b6f6"),
    "prolog": Icon(code="\ue7a1", color="#ef5350"),
    "husky": Icon(code="\uf8e8", color="#e5e5e5"),
    "coconut": Icon(code="\uf5d2", color="#8d6e63"),
    "sketch": Icon(code="\uf6c7", color="#ffc23d"),
    "pawn": Icon(code="\ue261", color="#ef6f3c"),
    "commitlint": Icon(code="ﰖ", color="#2b9689"),
    "dhall": Icon(code="\uf448", color="#78909c"),
    "dune": Icon(code="\uf7f4", color="#f47f3d"),
    "shaderlab": Icon(code="ﮭ", color="#1976d2"),
    "command": Icon(code="גּ", color="#afbcc2"),
    "stryker": Icon(code="\uf05b", color="#ef5350"),
    "modernizr": Icon(code="\ue720", color="#ea4863"),
    "roadmap": Icon(code="ﭭ", color="#30a69a"),
    "debian": Icon(code="\uf306", color="#d33d4c"),
    "ubuntu": Icon(code="\uf31c", color="#d64935"),
    "arch": Icon(code="\uf303", color="#218eca"),
    "redhat": Icon(code="\uf316", color="#e73d3a"),
    "gentoo": Icon(code="\uf30d", color="#948dd3"),
    "linux": Icon(code="\ue712", color="#eecf37"),
    "raspberry-pi": Icon(code="\uf315", color="#d03c4c"),
    "manjaro": Icon(code="\uf312", color="#49b95a"),
    "opensuse": Icon(code="\uf314", color="#6fb424"),
    "fedora": Icon(code="\uf30a", color="#3467ac"),
    "freebsd": Icon(code="\uf30c", color="#af2c2a"),
    "centOS": Icon(code="\uf304", color="#9d5387"),
    "alpine": Icon(code="\uf300", color="#e577b"),
    "mint": Icon(code="\uf30f", color="#7dbe3a"),
    "routing": Icon(code="נּ", color="#43a047"),
    "laravel": Icon(code="\ue73f", color="#f85051"),
    "directory": Icon(code="\ue5ff", color="#ffffff"),
    "dir-config": Icon(code="\ue5fc", color="#20adc2"),
    "dir-controller": Icon(code="\ue5fc", color="#ffc23d"),
    "dir-git": Icon(code="\ue5fb", color="#fa6f42"),
    "dir-github": Icon(code="\ue5fd", color="#546e7a"),
    "dir-npm": Icon(code="\ue5fa", color="#cb3837"),
    "dir-include": Icon(code="\uf756", color="#39be5"),
    "dir-import": Icon(code="\uf756", color="#afb42b"),
    "dir-upload": Icon(code="\uf758", color="#fa6f42"),
    "dir-download": Icon(code="\uf74c", color="#4caf50"),
    "dir-secure": Icon(code="\uf74f", color="#f9a93c"),
    "dir-images": Icon(code="\uf74e", color="#2b9689"),
    "dir-environment": Icon(code="\uf74e", color="#66bb6a"),
}


def icon(name: str) -> Optional[str]:
    """Get an icon associated with a filename,
    returns the default if it doesn't exist"""
    name = name.lstrip(".")
    icon = icons.get(name)
    if not icon:
        return None
    return icon.code
