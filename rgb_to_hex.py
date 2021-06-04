from venture.icons import icons, Icon


for key, value in icons.items():
    icons[key] = Icon(code=value["i"], color=value["c"])

breakpoint()