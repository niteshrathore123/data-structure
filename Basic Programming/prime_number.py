#Program to check number is prime or not.

import math
def isPrime(num):
	count=0
	n=int(math.sqrt(num))
	for i in range(2,n+1):
		if(num%i==0):
			count=1
			break
	if(count==1):
		print("Number is not Prime")
	else:
		print("Number is Prime")
	

num=int(input("Enter a number: "))
isPrime(num)

