from xmlrpc.client import Boolean


def Palindrome(s) -> Boolean:
  return s[::-1] == s

max = 0
for x in range(100,1000):
  for y in range(100,1000):
    prod = x*y
    if (prod > max and Palindrome(str(prod))):
      max = prod

print("3 digit maximum palindrome equals: " + str(max))
    