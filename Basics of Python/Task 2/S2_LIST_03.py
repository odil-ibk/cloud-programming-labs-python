def chunk(lst, size):
    if size <= 0:
        return None
    out = []
    i = 0
    while i < len(lst):
        out.append(lst[i:i + size])
        i += size
    return out

tests = [
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 3),
    ([], 2),
    ([1, 2, 3], 0),
]

for lst, size in tests:
    print((lst, size), "->", chunk(lst, size))
