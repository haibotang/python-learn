def fab(max):
    n , a, b = 0, 0 , 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

if __name__ == '__main__':
    for m in fab(6): # 1 1 2 3 5 8
        print(m)