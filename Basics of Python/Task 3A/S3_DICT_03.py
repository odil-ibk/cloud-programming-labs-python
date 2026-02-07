def pick(d, keys):
    out = {}
    for k in keys:
        if k in d:
            out[k] = d[k]
    return out

d = {"a": 1, "b": 2, "c": 3}
print(pick(d, ["a", "c", "x"]))
