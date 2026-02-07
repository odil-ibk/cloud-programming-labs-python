def normalize_name(x):
    if not x:
        return "Anonymous"
    name = x.strip()
    if name == "":
        return "Anonymous"
    return name

tests = ["", " ", None, " ola "]

for t in tests:
    print(repr(t), "->", normalize_name(t))
