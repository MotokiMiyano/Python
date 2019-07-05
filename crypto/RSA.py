import random
import math

def primeGenerate():
	while True:
		i = 1
		p = random.randint(pow(2,1023),pow(2,1024)-1)
		while(i < 40):
			a = random.randint(1,p-1)
			if(POW(a,p-1,p) != 1):
				break
			i = i + 1
		if(i >= 40):
			break

	return p
'''
べき乗剰余演算
'''
def POW(m,e,n):
	i = 0 #現在のbitの位置
	e = format(e,'b') #eを二進数表現

	i = i + 1 #最上位bitは１確定なので飛ばす
	c = m #mをセット（bitを飛ばした分）

	while i != len(e): #最下位bitまで
		c = (c * c) % n #繰り上がるのでかける
		if e[i] == "1":
			c = (c * m) % n #bitが１なら要素を加える
		i = i + 1 #bit繰り上げ

	return c

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

def GenCRTkey(p,q,d):
	dP = d % (p-1)
	dQ = d % (q-1)
	qI = Euclidean(p,q)

	return dP,dQ,qI

def lcm(p,q):
	return (p * q) // math.gcd(p, q)

def encord(m,e,n):
	return POW(m,e,n)

def decord(c,d,n):
	return POW(c,d,n)

def CRTdecord(c,dP,dQ,qI,P,Q):
	m1 = POW(c,dP,P)
	m2 = POW(c,dQ,Q)
	M = m1 - m2
	if M < 0:
		M = M + P
	H = (qI * M) % P

	return m2 + (H * Q)


P = primeGenerate()
Q = primeGenerate()



print("p=",P)
print("q=",Q)

n = P * Q
print("n =",n)

l = lcm(P-1,Q-1)
print("l=",l)

e = 65537
print("e=",e)

d = Euclidean(l,e)
print("d=",d)

dP,dQ,qI = GenCRTkey(P,Q,d)

m = 12345
print("m=",m)

c = encord(m,e,n)
print("c=",c)

CRTm = CRTdecord(c,dP,dQ,qI,P,Q)
print("CRTm=",CRTm)

m2 = decord(c,d,n)
print("m2=",m2)

