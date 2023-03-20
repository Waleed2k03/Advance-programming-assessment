with open("bio.txt", "r") as file_handler:
   	lines = file_handler.readlines()
 
name = []
age = []
gender = []
 

for l in lines:
	data = l.split('|')
	
name.append((data[0]))
age.append((data[1]))
gender.append((data[2].replace("\n", "")))
 
print("Name list \n", name)
print("Age list \n", age)
print("home town \n", gender)























