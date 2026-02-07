def at_least(min_value):
    return lambda x: x >= min_value

nums = [1, 5, 2, 10, 7]

pred = at_least(5)
result = list(filter(pred, nums))

print("nums:", nums)
print("filtered:", result)
