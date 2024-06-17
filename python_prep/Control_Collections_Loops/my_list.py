"""
 you should write code that creates a new list with one element
 for each number in my_list.
 If the original number is an even,
 then the corresponding element in the new list
 should contain the string 'even'; otherwise,
 the element should contain 'odd'.
"""

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

#using a for loop:
for number in my_list: 
	if number % 2 == 0: 
		new_list.append('even') 
	else: 
		new_list.append('odd') 

print(new_list) 

#using a while loop:
newer_list = [] 
index = 0 

while index < len(my_list): 
	if my_list[index] % 2 == 0: 
		newer_list.append('even') 
	else: 
		newer_list.append('odd')
	index += 1  
print(new_list) 
