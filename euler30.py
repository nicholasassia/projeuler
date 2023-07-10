result = 0
for n in range(2, 1000000):
    sum = 0
    for num in str(n):
        sum += pow(int(num),5)
    if sum == n:
        result += n
        print("5th power sum thingy is ", n)
print(result)