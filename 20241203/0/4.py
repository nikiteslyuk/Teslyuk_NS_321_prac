class C:
    a, b, c = input().split()


while st := input():
    match st.split():
        case [C.a, *_] if "yes" in _:
            print(1)
        case [C.b]:
            print(2)
        case [C.a, *_, C.c]:
            print(3)
        case default:
            print(0)
