def sum(a):
    if(a==0):
        return 0
    return sum(a-1)+a
cal_sum=sum(5)
print(cal_sum)