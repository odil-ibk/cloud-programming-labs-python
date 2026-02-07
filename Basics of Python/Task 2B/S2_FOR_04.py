def count_occurrences(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts

tests = [
    [1, 2, 1, 3, 2, 1],
    ["a", "b", "a", "c", "b", "a"],
    [],
]

for t in tests:
    print(t, "->", count_occurrences(t))
