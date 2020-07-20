import math
import matplotlib.pyplot as plt

X = []
y = []
def isPrime(x):
    flag = True
    for i in range(2,(x-1)):
        if x % i == 0:
            flag = False
            break
    return flag

def calculate(n):
    i = 1
    sum = 0
    while i != n:
        i+=1
        if isPrime(i):
            sum += math.log(i)
    
    print(n, sum, n/sum)
    X.append(n)
    y.append(n/sum)



def ranges():
    for i in range(2,1000,1):
        calculate(i)


ranges()
plt.plot(X,y)
plt.show()