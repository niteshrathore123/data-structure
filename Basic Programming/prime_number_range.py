#Find prime number within a given range
import math

def isPrime(low,high):
	
	
	for i in range(low,high+1):
		count=0
		n=int(math.sqrt(i))
		for j in range(2,n+1):
			if(i%j==0):
				count=1
		if(count==0):
			print(i)


isPrime(2,5)


