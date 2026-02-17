tuple=(1,2,3,4,5,6)
number=int(input("Enter Number:"))
count=len(tuple)-1
while count>=1:
    if(number==tuple[count]):
        print("Number Exsist at index:",count)
    count-=1