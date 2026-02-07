def flatten1(lst):
    out = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                out.append(x)
        else:
            out.append(item)
    return out

tests = [
    [1, [2, 3], 4],
    [[1, 2], [3], 4, [5, 6]],
    [1, 2, 3],
    [[], [1], 2],
]

for t in tests:
    print(t, "->", flatten1(t))
