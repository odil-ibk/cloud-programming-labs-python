def pipe_safe(*fns):
    def run(x):
        try:
            for fn in fns:
                x = fn(x)
            return {"ok": True, "value": x}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return run

to_int = lambda s: int(s)
invert = lambda n: 1 / n

safe = pipe_safe(to_int, invert)

for t in ["5", "0", "x"]:
    print(t, "->", safe(t))
