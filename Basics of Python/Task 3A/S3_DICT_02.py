def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}

defaults = {"a": 1, "b": {"x": 1}}
overrides = {"b": {"y": 2}}

print(merge_defaults(defaults, overrides))
