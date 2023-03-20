import math
def menu():
    
    print("[1] Calculate the area of a square")
    print("[2] Calculate the area of a circle")
    print("[3] Calculate the area of a triangle")

menu()
option = int(input("Pick your option:"))

while option == 3:
    
    a = float(input("Enter first number"))
    b = float(input("Enter second number"))
    c = float(input("Enter third number"))

    s = (a+b+c)/2
    area2 = (s*(s-a)* (s-b)*(s-c)) **0.5
    print('the area is of triangle if : %0.d'%area2)
    
    if option == 1:

        p = float(input("Enter the value of side:"))
        t = p*p
        print("Area of square is =",t)

    elif option == 2 :
        
        radius=float(input("Enter the radius of the circle:"))
        area = math.pi * radius * radius
        print("The area of the circle is:{0}".format(area))

    else:
        print("invalid option")

    




