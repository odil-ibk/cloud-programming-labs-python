def to_floats(strings):
    for s in strings:
        try:
            yield float(s.strip())
        except (ValueError, AttributeError):
            continue

def doubled(values):
    for v in values:
        yield v * 2

def pipeline_sum(strings):
    return sum(doubled(to_floats(strings)))

data = [" 1 ", "x", "2.5", "  -3  ", "", "7 "]
print(pipeline_sum(data))
