#Program to find the nth fibonaci series.

def fib(num):
	a=0
	b=1
	for i in range(num):
		print(a)
		c=a+b
		a=b
		b=c

num=int(input("Enter a number: "))
fib(num)