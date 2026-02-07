
lst = [1, 2, 3]
lst[0] = 99
print("List after modification:", lst)

tup = (1, 2, 3)
try:
    tup[0] = 99
except TypeError as e:
    print("Tuple modification error:", e)
