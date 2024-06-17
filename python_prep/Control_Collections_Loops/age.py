current_age = int(input("How old are you? ")) 

print(f"You are {current_age} years old.") 
#print(f"In 10 years, you will be {current_age + 10} years old.") 
#print(f"In 20 years, you will be {current_age + 20} years old.") 
#print(f"In 30 years, you will be {current_age + 30} years old.")
#print(f"In 40 years, you will be {current_age + 40} years old.")
 
for time in range(10,50,10): 
	print(f'In {time} years, you will be {current_age + time} years old.') 

