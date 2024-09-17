while string := input(): 
    if n := eval(string) == 13:
        print("13 is there")
        break
    if n % 2 == 0: 
        print(string)
else: 
    print("13 is not there!")
