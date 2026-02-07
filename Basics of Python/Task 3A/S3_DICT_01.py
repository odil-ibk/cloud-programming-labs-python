def get_path(obj, path, fallback=None):
    cur = obj
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return fallback
        cur = cur[part]
    return cur

data = {"a": {"b": {"c": 1}}}

tests = ["a.b.c", "a.b.x", "a.x.c"]

for p in tests:
    print(p, "->", get_path(data, p, "NA"))
