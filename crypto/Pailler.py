import random
import math

def primeGenerate():
	while True:
		i = 1
		p = random.randint(pow(2,1023),pow(2,1024)-1)
		while(i < 20):
			a = random.randint(pow(2,1023),pow(2,1024)-1)
			if(pow(a,p-1,p) != 1):
				break
			i = i + 1
		if(i == 20):
			break

	return p

def Euclidean(n,x):
	max = n
	min = x

	max2 = 0
	min2 = 1

	while(max % min != 0):
		q = max // min
		max, min = (min, max%min)
		max2, min2 = (min2, max2 - (q * min2))

	if(min2 < 0):
		return n + min2
	else:
		return min2

def lcm(p,q):
	return (p * q) // math.gcd(p, q)

def L(u,n):
	return (u - 1) // n

def encord(m,g,n):
	r = random.randint(1,pow(n,2))
	return ( (pow(g,m,pow(n,2))) * (pow(r,n,pow(n,2))) ) % pow(n,2)

def decord(c,μ,λ,n):
	return (L(pow(c,λ,pow(n,2)),n) * μ) % n

def setkey():
	p = primeGenerate()
	q = primeGenerate()
	print("p=",p)
	print("q=",q)

	n = p * q
	print("n =",n)

	g = n + 1
	print("g=",g)

	λ = lcm(p-1,q-1)
	print("λ=",λ)

	μ = Euclidean(n,L(pow(g,λ,pow(n,2)),n))
	print("μ=",μ)

m = 123450
print("m=",m)

m1 = 12345
print("m1=",m1)

c = encord(m,g,n)
print("c=",c)

c1 = encord(m1,g,n)
print("c1=",c1)

# m+m
c2 = c * c1
print("c2=",c2)

# m-m
c2 = c * Euclidean(pow(n,2),c1)
print("c2=",c2)

# am
c2 = pow(c,3)
print("c2=",c2)

m2 = decord(c2,μ,λ,n)
print("m2=",m2)
