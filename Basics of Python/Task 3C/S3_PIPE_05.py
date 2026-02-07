def parse_line(line):
    left, rest = line.split(":", 1)
    parts = rest.strip().split()
    d = {"level": left.strip()}
    for p in parts:
        if "=" in p:
            k, v = p.split("=", 1)
            d[k] = v
    return d

def extract_info_user_ids(lines):
    out = []
    for line in lines:
        try:
            d = parse_line(line)
        except ValueError:
            continue
        if d.get("level") != "INFO":
            continue
        user = d.get("user")
        if user is None:
            continue
        try:
            out.append(int(user))
        except ValueError:
            continue
    return out

lines = [
    "INFO: user=42 action=login",
    "WARN: user=17 action=login",
    "INFO: user=abc action=login",
    "INFO: action=logout user=7",
    "BAD LINE",
]

print(extract_info_user_ids(lines))
