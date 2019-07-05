import random

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


a = primeGenerate()
b = primeGenerate()
n = a * b
e = 65537

print("p:", a)
print("q" , b)
print("n" , n)

