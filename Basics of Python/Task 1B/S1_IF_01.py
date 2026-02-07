def shipping_cost(weight_kg, is_member):
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return None
    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30
    if is_member:
        cost *= 0.8
    return cost

tests = [
    (-1, False),
    (0, True),
    (0.5, False),
    (1, True),
    (5, False),
    (6, True),
]

for t in tests:
    print(t, "->", shipping_cost(*t))
