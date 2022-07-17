num = [0,1,2,3,11,12,13,21,22,23,31,32,33,111,112,113,121,122,123,131]
upper = 111111111111222333
ans = 0

def check(x):
    for i in range(0, 20): 
        if num[i] == x:
            return True
    return False

def C(x, y):
    return fac(x)/fac(y)/fac(x-y)

def real_get(a, b, c, length): 
    ret = 0
    for i in range(0, 20):
        if num[i] > length:
            break
        if num[i] < a:
            continue
        for j in range(0, 20):
            if num[i] + num[j] > length or length - num[i] - num[j] < c:
                break
            if num[j] < b or check(length - num[i] - num[j]) == False:
                continue
            ret = ret + C(length-a-b-c, num[i]-a) * C(length-b-c-num[i], num[j]-b)
    return ret 

def fac(x): 
    if x == 0:
        return 1
    return x*fac(x-1) 

def equal(x, y):
    if x==y:
        return 1
    return 0

index = 0

for index in range(1,50):
    buf = real_get(0,0,0,index)
    if upper >= buf:
        upper = upper - buf
    else:
        print(index, upper)
        break

a = [0, 0, 0]

for i in range(0, index):
    for j in range(0, 3):
        buf = real_get(a[0] + equal(j, 0), a[1] + equal(j, 1), a[2] + equal(j, 2), index)
        if upper > buf:
            upper = upper - buf
        else:
            a[j] = a[j] + 1
            ans = ans * 10 + j + 1
            break
print(ans % 123123123)