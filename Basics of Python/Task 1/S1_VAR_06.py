
def to_int_or_none(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None

tests = ["12", " 12 ", "12x", "", None]

for t in tests:
    print(f"{t!r:<6} -> {to_int_or_none(t)}")
