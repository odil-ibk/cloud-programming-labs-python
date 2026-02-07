def omit(d, keys):
    out = {}
    for k, v in d.items():
        if k not in keys:
            out[k] = v
    return out

d = {"a": 1, "b": 2, "c": 3}
print(omit(d, ["b"]))
