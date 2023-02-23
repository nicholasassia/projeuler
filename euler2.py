def fib():
    a = 1 
    b = 2
    evenfib = 0
    
    while a <= 4000000:
        if (a % 2) == 0:
            evenfib += a
        print(a)
        a, b = b, a+b
    print(f'sum of even vals: {evenfib}')
        
if __name__ == '__main__':
    fib()
