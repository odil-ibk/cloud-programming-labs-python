def run_command(cmd):
    match cmd:
        case "start":
            return "START"
        case "stop":
            return "STOP"
        case "status":
            return "STATUS"
        case _:
            return "UNKNOWN_COMMAND"

commands = ["start", "stop", "status", "restart", ""]

for c in commands:
    print(c, "->", run_command(c))
