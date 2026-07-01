# class Student:
#     def __init__(self,userid,userpass):
#         self.userid=userid
#         self.userpass=userpass
#     def __checkuserpass(self):
#         if self.userid=="123":
#             return True
#         else:
#             return False
#     def printinfo(self):
#         executed=self.__checkuserpass()
#         if executed==True:
#             print(self.userid,self.userpass)
#         else:
#             print("Failed")
   
# S1=Student("1234","2345")
# S1.printinfo()
#-------------Inheritence---------
# class System:
#     def startcar(self):
#         print("Started")
# class Bike(System):
#     def Clutch(self):
#         print("Clutch is pushed")
# class Cycle(Bike):
#     def brake(self):
#         print("Brake is pushed")
# class Car(Cycle,Bike):
#     def model(self):
#         print("civic")
# c1=Cycle()
# car=Car()
# c1.brake()
# c1.Clutch()
# c1.startcar()
# car.brake()
# car.Clutch()
# car.model()
#--------------polymorphism---------
class complexnumbr:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumbr(self):
        print(self.real,self.img)
    def __add__(self, num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complexnumbr(newReal,newImg)
num1=complexnumbr(4,5)
num2=complexnumbr(6,7)
num3=num1+num2
num3.showNumbr()
