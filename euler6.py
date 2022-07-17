sumsquare = 0
square = 0
for i in range(1,101):
    square += i**2
    
for i in range(1,101):
    sumsquare += i

sumsquare = sumsquare**2

print(sumsquare-square)
