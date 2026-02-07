def make_adder(x):
    return lambda y: y + x

add10 = make_adder(10)
add3 = make_adder(3)

for t in [0, 5, -2]:
    print(t, "->", add10(t))

for t in [0, 5, -2]:
    print(t, "->", add3(t))
