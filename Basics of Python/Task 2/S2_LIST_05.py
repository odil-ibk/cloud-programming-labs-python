def stats(nums):
    if len(nums) == 0:
        return None
    total = 0
    mn = nums[0]
    mx = nums[0]
    for n in nums:
        total += n
        if n < mn:
            mn = n
        if n > mx:
            mx = n
    return {"min": mn, "max": mx, "avg": total / len(nums), "sum": total}

tests = [
    [1, 2, 3, 4],
    [-5, 0, 10],
    [7],
    [],
]

for t in tests:
    print(t, "->", stats(t))
