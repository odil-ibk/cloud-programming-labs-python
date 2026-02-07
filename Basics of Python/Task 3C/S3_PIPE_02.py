def compose(*fns):
    def run(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return run

f = lambda x: x + 1
g = lambda x: x * 2
h = lambda x: x - 3

p = pipe(f, g, h)
c = compose(f, g, h)

for t in [0, 5, -2]:
    print(t, "pipe->", p(t), "compose->", c(t))
