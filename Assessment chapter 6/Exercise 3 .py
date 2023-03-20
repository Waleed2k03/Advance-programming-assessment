def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def modulus(a, b):
    return a % b

def greater(a, b):
    return a > b


print("Choose your option:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Check greater Number")

while True:
    # User input
    choice = input("Enter choice(1,2,3,4,5,6): ")

    # Options check
    if choice in ('1', '2', '3', '4','5','6'):
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

        elif choice == '5':
            print(num1, "/", num2, "=", modulus(num1, num2))
        
        elif choice == '6':
            print(num1, "/", num2, "=", greater(num1, num2))
        
        #For calculating again
        next_calculation = input("Do you want to quit? (press Q): ")
        if next_calculation == "Q":
          break
    else:
        print("Invalid Input")