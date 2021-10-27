#digits of a number.
"""input :- 5678910
output :- 
5
6
7
8
9
1
0
"""


def digitsOfNum(num):
	digitCount=0
	temp=num
	while(temp!=0):
		digitCount+=1
		temp=temp//10
	div=pow(10,digitCount-1)
	print(div)
	while(div!=0):
		q=num//div
		print(q)
		num=num%div
		div=div//10
		
num=int(input("Enter a number: "))
digitsOfNum(num)
