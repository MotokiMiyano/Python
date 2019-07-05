import random
import math
import time

def f(x):
    return (x*x) - 1

def primeGenerate():
	while True:
		i = 1
		p = random.randint(pow(2,39),pow(2,40)-1)
		while(i < 40):
			a = random.randint(1,p-1)
			if(pow(a,p-1,p) != 1):
				break
			i = i + 1
		if(i >= 40):
			break

	return p

p = primeGenerate()
q = primeGenerate()

n = p * q

d = 1
x = 2
y = 2

start = time.time()
while(d == 1):
    x = f(x) % n
    y = f(f(y)) % n
    d = math.gcd(abs(x-y),n)

end = time.time()
print(n,"=",d,"*",n//d)
print(end-start,"sec")