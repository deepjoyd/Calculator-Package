def sum(x,y):
    return x+y
def diff(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y

while(1):
    print("Operations available:","1.Addition","2.Subtraction","3.Multiplication","4.Division","5.Modulo",sep="\n")
    print("Choose a number from above to perform an operation:")
    x=input()
    print("Enter two number on which you want to perform operation:")
    y=float(input())
    z=float(input())
    if x=='1':
        print(sum(y,z))
    elif x=='2':
        print(diff(y,z))
    elif x=='3':
        print(mul(y,z))
    elif x=='4':
        print(div(y,z))
    elif x=='5':
        print(mod(y,z))
    else:
        print("Invalid Input")
    a=input("Click 0 to stop and 1 to continue, Basic_Calculator: ")   
    if a=='0':
        break
    elif a=='1':
        continue
     