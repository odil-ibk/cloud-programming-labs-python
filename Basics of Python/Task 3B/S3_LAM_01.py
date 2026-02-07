square = lambda n: n * n
is_odd = lambda n: n % 2 != 0
greet = lambda name: f"Hello, {name}"

for t in [0, 2, -3]:
    print(t, "->", square(t))

for t in [0, 1, 2]:
    print(t, "->", is_odd(t))

for t in ["Ola", "Ana", "Mike"]:
    print(t, "->", greet(t))
