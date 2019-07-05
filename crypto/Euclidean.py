p = 97
x = 30

max = p
min = x

max2 = 0
min2 = 1
print(max,min2,max2)
print(min,max2,min2)
while(max % min != 0):	
	q = max // min
	max, min = (min, max%min)

	max2, min2 = (min2, max2 - (q * min2))
	print(min,max2,min2)
if(min2 < 0):
	print(p+min2)
	u = p+min2
	print((u*x)%p)
else:
	print(min2) 
	print((min2*x)%p)

