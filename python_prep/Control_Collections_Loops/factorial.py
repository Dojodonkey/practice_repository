"""
Write a function that computes and returns the factorial of a number
 by using a for or while loop.
 The factorial of a positive integer n, signified by n!,
 is defined as the product of all integers between 1 and n,
 inclusive:

n!	Expansion	Result
1!	1	1
2!	1 * 2	2
3!	1 * 2 * 3	6
4!	1 * 2 * 3 * 4	24
5!	1 * 2 * 3 * 4 * 5	120
"""



number = int(input("Pick a number: "))
"""
#using a for loop:  
result = 1 
for i in range (1, number + 1): 
	result *= i 
print(result)
"""

#using a while loop: 

result = 1 
while number > 0:
	result *= number
	number -= 1 
print(result)  
