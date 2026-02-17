number=float(input("Enter Number:"))
opt=str(input("Enter Operator(+,-,/,*):"))
number2=float(input("Enter Number2:"))
if(opt=="+"):
    print("Sum = ",number+number2)
elif(opt=="-"):
    print("Subtract = ",number-number2)
elif(opt=="*"):
    print("Product = ",number*number2)
elif(opt=="/"):
    print("Divide = ",number/number2)
else:
    print("Invalid")
