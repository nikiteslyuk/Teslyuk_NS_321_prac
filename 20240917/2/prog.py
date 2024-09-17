summ = 0
while (n := eval(input())) > 0:
    summ += n
    if summ > 21: 
        print(summ)
        break
else: 
    print(n)
