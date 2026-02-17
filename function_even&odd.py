def number(a):
    if(a%2==0):
        str="Even"
        return str
    elif a==0:
        str="0"
        return str
    elif(a%2!=0):
        str="odd"
        return str
    else:
        return "Ivalid Number"
a=int(input("Enter Number:"))
str=number(a)
print(str)