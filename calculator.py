def cal_sum(a,b):
    return a+b
def cal_divide(a,b):
    return a/b
def cal_multiply(a,b):
    return a*b
def cal_subtract(a,b):
    return a-b
while True:
    try:
        number1=float(input("Enter Number:"))
        break
    except Exception as e:
        print(f"Error Occurred {e}")
while True:
    operator=input("+,-,/,*,= for end Enter Choice:")
    if operator=="=":
        print("total =",number1)
        break
    if operator not in ("+","-","/","*"):
        print("Invalid input")
        continue
    while True:
        try:
            number2=float(input("Enter Number:"))
            break
        except Exception as e:
            print(f"Error Occurred {e}")
    if operator=="+":
        number1=cal_sum(number1,number2)
    elif operator=="-":
        number1=cal_subtract(number1,number2)
    elif operator=="/":
            if number2==0:
                raise ZeroDivisionError("Cannot divide by zero")
            number1=cal_divide(number1,number2)
    elif operator=="*":
        number1=cal_multiply(number1,number2)

