def calc(a, op, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None

tests = [
    (2, "+", 3),
    (5, "-", 1),
    (4, "*", 2),
    (10, "/", 2),
    (10, "/", 0),
    (1, "%", 2),
]

for t in tests:
    print(t, "->", calc(*t))
