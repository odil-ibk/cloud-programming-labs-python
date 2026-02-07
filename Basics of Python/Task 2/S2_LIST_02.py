def unique(values):
    out = []
    for v in values:
        if v not in out:
            out.append(v)
    return out

tests = [
    [1, 2, 1, 3, 2, 4],
    ["a", "b", "a", "c", "b"],
    [],
    [None, None, 0, 0, False, False, True, True],
]

for t in tests:
    print(t, "->", unique(t))
