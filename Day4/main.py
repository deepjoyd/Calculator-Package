while(1):
    print("Choose from modules available:","1.Basic Calculator","2.BMI Calculator","3.Temperature Calculator",
             "4.Currency Calculator","5.Scientific Calculator", sep="\n")
    ch=input()
    if(ch=='1'):
        from calculator import Basic_calculator
    elif(ch=='2'):
        from calculator import BMI_calculator
    elif(ch=='3'):
        from calculator import Temperature_calculator
    elif(ch=='4'):
        from calculator import Currency_calculator
    elif(ch=='5'):
        from calculator import Scientific_calculator
    b=input("Click n to exit and y to choose another calculator: ")   
    if b=='y' or b=='Y':
        continue
    elif b=='n' or b=='N':
        break
print("*****Rate your Experience on a scale of 1 to 5*****")
rate=input()
print("THANK YOU...HOPE YOU LIKED IT")