def invert(d):
    out = {}
    for k, v in d.items():
        if v in out:
            out[v].append(k)
        else:
            out[v] = [k]
    return out

d = {"a": 1, "b": 2, "c": 1}
print(invert(d))
