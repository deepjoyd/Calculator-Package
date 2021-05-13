def KTD(x):
    return x-273.15
def DTK(x):
    return x+273.15
def FTD(x):
    return (x-32)*(5/9)
def DTF(x):
    return  (x*9)/5+32
def KTF(x):
    y=KTD(x)
    return DTF(y)
def FTK(x):
    y=FTD(x)
    return DTK(y)
while(1):
    print("Operations available:","1.Kelvin to Degree","2.Degree to Kelvin","3.Fahrenheit to Degree","4.Degree to Fahrenheit",
          "5.Kelvin to Fahrenheit", "6.Fahrenheit to Kelvin",sep="\n")
    print("Choose a number from above to perform an operation:")
    x=input()
    if x=='1':
        y=float(input("Enter temperature in Kelvin: "))
        print(y,"Kelvin is equal to",KTD(y),"Degree",sep="\t")
    elif x=='2':
        y=float(input("Enter temperature in Degree: "))
        print(y,"Degree is equal to",DTK(y),"Kelvin",sep="\t")
    elif x=='3':
        y=float(input("Enter temperature in Fahrenheit: "))
        print(y,"Fahrenheit is equal to",FTD(y),"Degree",sep="\t")
    elif x=='4':
        y=float(input("Enter temperature in Degree: "))
        print(y,"Degree is equal to",DTF(y),"Fahrenheit",sep="\t")
    elif x=='5':
        y=float(input("Enter temperature in Kelvin: "))
        print(y,"Kelvin is equal to",KTF(y),"Fahrenheit",sep="\t")
    elif x=='6':
        y=float(input("Enter temperature in Fahrenheit: "))
        print(y,"Fahrenheit is equal to",FTK(y),"Kelvin",sep="\t")
    else:
        print("Invalid Input")
    a=input("Click 0 to stop and 1 to continue, Temperature_Calculator: ")   
    if a=='0':
        break
    elif a=='1':
        continue