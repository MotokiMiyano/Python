# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:25:05 2018

@author: 18T0015
"""
import copy
import math
import random


def productA():
    A = 4
    Sa = [1,2,4,11]
    puls = A+1
    ci = [0]*puls
    sci = [0]*puls
    ei = [0]*puls
    ci[0] = 1
    
    for i in range(A):
        for k in range(puls):
            sci[k] = copy.deepcopy(ci[k])
        for j in range(A):
            ci[j+1] = copy.deepcopy(sci[j])
        ci[0] = 0
        for l in range(puls):
            ci[l] = ci[l] + (sci[l]*(-1*Sa[i]))
    
    key = setkey()
    n = key[0]
    g = key[1]
    l = key[2]
    m = key[3]
    
    for i in range(len(ci)):
        if(ci[i] < 0):
            ci[i] = ci[i] + n
    
    
    for i in range(len(ei)):
        ei[i] = encord(ci[i],g,n)
    
    return ei,n,g,l,m

def productB(ei,n,g):
    B = 8
    SB = [2,4,5,6,7,8,9,10]
    
    dj = [0]*B
    
    for i in range(B):
        Enc = encord(SB[i],g,n)
        mult = multi(ei,SB[i])
        rnd = random.randint(pow(2,2047),pow(2,2048)-1)
        dj[i] = pow(mult,rnd,pow(n,2)) * Enc % (n*n)
    
    return dj

def multi(ei,SB):
    mul = 1
    for i in range(len(ei)):
        mul = mul * pow(ei[i],pow(SB,i),pow(n,2)) % (n*n)
        
    return mul
    
            
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

def encord(plane,g,n):
    r = random.randint(1,pow(n,2))
    return ( (pow(g,plane,pow(n,2))) * (pow(r,n,pow(n,2))) ) % pow(n,2)

def decord(c,m,l,n):
	return (L(pow(c,l,pow(n,2)),n) * m) % n

def setkey():
    p = primeGenerate()
    q = primeGenerate()
    n = p * q
    g = n + 1
    
    l = lcm(p-1,q-1)
    
    m = Euclidean(n,L(pow(g,l,pow(n,2)),n))
    
    key = [0]*4
    
    key[0] = n
    key[1] = g
    key[2] = l
    key[3] = m
    return key

    
ei,n,g,l,m = productA()
dj = productB(ei,n,g)

for i in range(len(dj)):
    print(decord(dj[i],m,l,n))
	

    