import math
n=int(input())
if n<4:
    print(0)
else:
    print(int(math.factorial(n)/(math.factorial(4)*math.factorial(n-4))))