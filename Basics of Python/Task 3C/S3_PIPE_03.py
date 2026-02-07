def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run

strip_ = lambda s: s.strip()
lower_ = lambda s: s.lower()
collapse_spaces = lambda s: " ".join(s.split())

normalize = pipe(strip_, lower_, collapse_spaces)

s = "  Ala   Ma  Kota  "
print(normalize(s))
