def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total

tests = [
    ([1, 2, 3, 4], 5),
    ([2, 2, 2], 3),
    ([10, 1, 1], 10),
    ([], 10),
]

for nums, th in tests:
    print((nums, th), "->", sum_until(nums, th))
