def USDTR(x):
    return x*73.64
def RTUSD(x):
    return x*0.014
def ETR(x):
    return x*88.88
def RTE(x):
    return x*0.011
def PTR(x):
    return x*103.97
def RTP(x):
    return x*0.0097
def AUDTR(x):
    return x*56.79
def RTAUD(x):
    return x*0.018

while(1):
    print("Operations available:","1.US Dollars to Rupees","2.Rupees to US Dollars","3.Euros to Rupees","4.Rupees to Euros",
          "5.Pound Sterling to Ruppees", "6.Rupees to Pound Sterling", "7.Australian Dollars to Rupees", "8.Rupees to Australian Dollars",sep="\n")
    print("Choose a number from above to perform an operation:")
    x=input()
    if x=='1':
        y=float(input("Enter amount in US Dollars: "))
        print(y,"US Dollars is equal to",USDTR(y),"Rupees",sep="\t")
    elif x=='2':
        y=float(input("Enter amount in Rupees: "))
        print(y,"Rupees is equal to",RTUSD(y),"US Dollars",sep="\t")
    elif x=='3':
        y=float(input("Enter amount in Euros: "))
        print(y,"Euros is equal to",ETR(y),"Rupees",sep="\t")
    elif x=='4':
        y=float(input("Enter amount in Rupees: "))
        print(y,"Rupees is equal to",RTE(y),"Euros",sep="\t")
    elif x=='5':
        y=float(input("Enter amount in Pounds: "))
        print(y,"Pounds is equal to",PTR(y),"Rupees",sep="\t")
    elif x=='6':
        y=float(input("Enter amount in Rupees: "))
        print(y,"Rupees is equal to",RTP(y),"Pounds",sep="\t")
    elif x=='7':
        y=float(input("Enter amount in Australian Dollars: "))
        print(y,"Australian Dollars is equal to",AUDTR(y),"Rupees",sep="\t")
    elif x=='8':
        y=float(input("Enter amount in Rupees: "))
        print(y,"Rupees is equal to",RTAUD(y),"Australian Dollar",sep="\t")
    else:
        print("Invalid Input")
    a=input("Click 0 to stop and 1 to continue, Temperature_Calculator: ")   
    if a=='0':
        break
    elif a=='1':
        continue