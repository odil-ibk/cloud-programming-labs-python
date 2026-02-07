def clean_numbers(values):
    out = []
    for s in values:
        try:
            out.append(float(s.strip()))
        except (ValueError, AttributeError):
            pass
    return out

tests = [
    [" 1 ", "x", "2"],
    ["3.5", "  -2  ", "0", "bad"],
    ["", "   ", "7"],
    [None, "4"],
]

for t in tests:
    print(t, "->", clean_numbers(t))
