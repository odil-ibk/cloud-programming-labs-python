def group_by(items, key):
    out = {}
    for item in items:
        val = item.get(key)
        if val in out:
            out[val].append(item)
        else:
            out[val] = [item]
    return out

items = [
    {"name": "a", "type": "x"},
    {"name": "b", "type": "y"},
    {"name": "c", "type": "x"},
]

print(group_by(items, "type"))
