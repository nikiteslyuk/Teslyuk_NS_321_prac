a = eval(input())
match a: 
    case 1: 
        print(1)
    case 2:
        print(2)
    case 3: 
        print(3)
    case var if var % 2 == 0: 
        print("четное")
    case var: 
        print("нечетное")
    case _: 
        print("много")
