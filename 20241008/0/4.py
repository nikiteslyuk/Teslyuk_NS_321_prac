def binh(f, t):
    w = len(f'{bin(t)} = {hex(t)}')
    for i in range(f, t + 1):
        mw = len(f'{bin(i)} = {hex(i)}')
        print(f'{bin(i)} {' =': {w - mw + 1}} {hex(i)}')
