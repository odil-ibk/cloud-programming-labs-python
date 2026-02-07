def sum_nested(matrix):
    total = 0
    for row in matrix:
        if not isinstance(row, list):
            return None
        for n in row:
            total += n
    return total

tests = [
    [[1, 2], [3, 4]],
    [[-1, 5], [10]],
    [],
    [1, [2, 3]],
]

for t in tests:
    print(t, "->", sum_nested(t))
