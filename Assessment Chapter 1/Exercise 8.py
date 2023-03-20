print("Enter three numbers:")
a = int(input())
b = int(input())
c = int(input())
if (a > b):
    if (a > c):
      print(str(a) + "is the largest number")
    else:
        print(str(c) + "is the largest number")
elif (b > c ):
    print(str(b) + "is the largest number")
else:
        print(str(c) + "is the largest number")