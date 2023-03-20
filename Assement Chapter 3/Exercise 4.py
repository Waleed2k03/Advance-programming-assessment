def calc():
    while True:
     print("1 Addition")
     print("2 Subtract")
     print("3 Multiply")
     print("4 Divide")
     print("5 Modulus")

     option = int(input("Choose the operation from 1 to 5:"))
     if option == 1:
        res = 'y'
        e1 = int(input("Enter your first value:"))
        e2 = int(input("Enter your second value:"))
        a = e1 + e2
        print ("The answer is:",a)
        res = str(input("Do you want to try again? (y/n) :"))
        if res in 'n':
            break
        
     elif option == 2:
         res = 'y'
         e1 = int(input("Enter your first value:"))
         e2 = int(input("Enter your second value:"))
         a = e1 - e2
         print ("The answer is:",a)
         res = str(input("Do you want to try again? (y/n) :"))
         if res in 'n':
            break
     elif option == 3:
         res = 'y'
         e1 = int(input("Enter your first value:"))
         e2 = int(input("Enter your second value:"))
         a = e1 * e2
         print ("The answer is:",a)
         res = str(input("Do you want to try again? (y/n) :"))
         if res in 'n':
            break
     elif option == 4:
         res = 'y'
         e1 = int(input("Enter your first value:"))
         e2 = int(input("Enter your second value:"))
         a = e1 / e2
         print ("The answer is:",a)
         res = str(input("Do you want to try again? (y/n) :"))
         if res in 'n':
            break
     elif option == 5:
         res = 'y'
         e1 = int(input("Enter your first value:"))
         e2 = int(input("Enter your second value:"))
         a = e1 % e2
         print ("The answer is:",a)
         res = str(input("Do you want to try again? (y/n) :"))
         if res in 'n':
            break

calc()
        
