def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run

f = lambda x: x + 1
g = lambda x: x * 2
h = lambda x: x - 3

p = pipe(f, g, h)

for t in [0, 5, -2]:
    print(t, "->", p(t))
