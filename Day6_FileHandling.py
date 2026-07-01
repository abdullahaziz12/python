file=open("admin.txt","w")
file.write("123,abdcd,3,false")
file.close()
with open("admin.txt", "r") as file:
    line=file.readline()
    print(line)
