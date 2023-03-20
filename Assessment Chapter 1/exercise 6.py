print("Enter the length of a number")
a=int(input ("First value"))
b=int(input ("second value"))
c=int(input ("third value"))
if a==b==c:
    print("it is equilateral triangle")
elif a==b or b==c or c==a:
    print("it is isosceles triangle")
else:
        print("scalene triangle")
