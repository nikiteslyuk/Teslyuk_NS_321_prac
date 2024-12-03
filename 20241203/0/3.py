import readline

while s := input("> "):
    match s.split():
        case ["mov", str(a), str(b)]:
            print(f"mov {a}, {b}")
        case [("push" as st) | ("pop" as st), *reglist]:
            print(f"{st}ing {', '.join(reglist)}")
        case [cmd, r1]:
            print(f"making {cmd} with {r1}")
        case default:
            print("parse error")
