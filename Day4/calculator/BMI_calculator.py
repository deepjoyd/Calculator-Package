W=float(input("Enter your weight in Kilograms: "))
H=float(input("Enter your height in meters upto two decimal places: "))
ans=W/H**2
print("Your BMI is : ",ans)
if(ans<=18.5):
    print("You are Underweight.")
elif(ans<=24.9):
    print("You are Normal.")
elif(ans<=29.9):
    print("You are Overweight.")
else:
    print("You are Obese.")