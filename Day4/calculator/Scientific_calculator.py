import math
while(1):
    print("Operations available:","1.Sin","2.Cos","3.Tan","4.Factorial",
          "5.nth Power","6.nth Root","7. log with any base",sep="\n")
    print("Choose a number from above to perform an operation:")
    x=input()
    if(x=='1'):
        y=float(input("Enter angle in Radians: "))
        print("Required value is: ",math.sin(y))
    elif(x=='2'):
        y=float(input("Enter angle in Radians: "))
        print("Required value is: ",math.cos(y))
    elif(x=='3'):
        y=float(input("Enter angle in Radians: "))
        print("Required value is: ",math.tan(y))
    elif(x=='4'):
        y=float(input("Enter a number less than 100001: "))
        print("Required value is: ",math.factorial(y))
    elif(x=='5'):
        y=float(input("Enter the number: "))
        z=float(input("Enter its power: "))
        print("Required value is: ",math.pow(y,z))
    elif(x=='6'):
       y=float(input("Enter the number: "))
       z=float(input("Enter the root to calculate: "))
       print("Required value is: ",y**(1/z))
    elif(x=='7'):
        y=float(input("Enter the number: "))
        z=float(input("Enter the base: "))
        print("Required value is: ",math.log(y,z))
    else:
        print("Invalid Input")
    a=input("Click 0 to stop and 1 to continue, Scientific_Calculator: ")   
    if a=='0':
        break
    elif a=='1':
        continue