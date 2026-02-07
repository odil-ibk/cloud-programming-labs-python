def grade(score):
    if not isinstance(score, int) or score < 0 or score > 100:
        return None
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for s in [59, 60, 69, 70, 79, 80, 89, 90, 100, 101]:
    print(s, "->", grade(s))
