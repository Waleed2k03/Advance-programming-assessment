f_name=(input("Enter your first name:"))
l_name=(input("Enter your last name:"))

f_name = f_name.capitalize()
l_name = l_name.capitalize()

print("your full name is:")
fl = "{first} {last}"
print(fl.format(first=f_name,last=l_name))
