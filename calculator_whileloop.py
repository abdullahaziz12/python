number1=float(input("Enter Number:"))
while True:
    opt=str(input("Enter Operator(+,-,/,*,= for stop)"))
    if opt=="=":
        print("Total = ",number1)
        break
    number2=float(input("Enter Number:"))
    if opt=="+":
        number1+=number2
    elif opt=="-":
        number1-=number2
    elif opt=="/":
        number1/=number2
    elif opt=="*":
        number1*=number2
    else:
        print("invalid operator")
