def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None

tests = [
    [1, 3, 5, 8, 10],
    [1, 3, 5],
    [2, 3, 4],
    [],
]

for t in tests:
    print(t, "->", find_first_even(t))
