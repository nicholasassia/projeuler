def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def digitcount(n):
    factorial = fact(n)
    count = 0
    for digit in str(factorial):
        count += int(digit)
    return count
    
if __name__ == '__main__':
    print(digitcount(100))