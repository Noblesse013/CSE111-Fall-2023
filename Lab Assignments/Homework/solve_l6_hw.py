# -*- coding: utf-8 -*-
"""Solve L6 HW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kHmJmDtjp1ajLXybnnYusUKTwE5S5PxQ
"""

#TASK1
class Student:
  ID=0
  def __init__(self,name,department,age,cgpa):
    self.name=name
    self.department=department
    self.age=age
    self.cgpa=cgpa
    Student.ID+=1
  def showDetails(self):
    print(f'ID: {Student.ID}\nName: {self.name}\nDepartment: {self.department}\nAge: {self.age}\nCGPA : {self.cgpa}')
  @classmethod
  def from_String(cls,info):
    name,dept,age,cg=info.split('-')
    return cls(name,dept,age,cg)

s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()

print('========================================================================================================================================')
print('Answer of Q5:')
print('''A class variable is a variable defined inside a class and outside of any method. It is shared by all instances of that class and is accessed using the class name. They are useful for storing data that is common to all objects of the class.
An instance variable, on the other hand, is a variable that is specific to each instance of the class. It is defined inside the constructor method (___init___) of the class and is accessed using the self keyword. They are used to store data that varies from one object to another.
''')
print('Answer of Q6:')
print('''An instance method is a method that is defined inside a class and is called on an instance of that class. It takes the instance itself (self) as the first argument and can access the instance variables and methods.
 On the other hand, class method is a method that is defined inside a class and is called on the class itself. It takes the class itself (cls) as the first argument and can access the class variables and methods.
''')

#task2
class Passenger:
  count=0
  def __init__(self,name):
    self.name=name
    self.fare=450
    Passenger.count+=1
  def set_bag_weight(self,w):
      if w <= 20:
        self.fare = 450
      elif 21 < w < 50:
        self.fare += 50
      else:
        self.fare += 100
  def printDetail(self):
    print(f'Name:{self.name}\nBus Fare:{self.fare} taka')

print('Total Passenger:', Passenger.count)
p1 = Passenger('Jack')
p1.set_bag_weight(90)
p2 = Passenger('Carol')
p2.set_bag_weight(10)
p3 = Passenger('Mike')
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print('Total Passenger:', Passenger.count)

#task3
class Travel:
  count = 0
  def __init__(self,f,t):
    self.source = f
    self.destination = t
    self.time = 1
    Travel.count += 1

  def set_source(self,s):
    self.source = s

  def set_destination(self,t):
    self.destination = t

  def set_time(self,ti):
    self.time = ti
  def display_travel_info(self):
    return f'Source:{self.source}\nDestination:{self.destination}\nFlight Time: {self.time}:00'

print('No. of Traveller =', Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print('No. of Traveller =', Travel.count)

#task4
class NikeBangladesh:
    branches_opened = []
    total_stock = {"Air Jordan": 0, "Cortez": 0, "Zoom Kobe": 0}
    total_sold = 0

    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.stock = {"Air Jordan": 0, "Cortez": 0, "Zoom Kobe": 0}
        self.sold = 0
        NikeBangladesh.branches_opened.append(branch_name)

    @classmethod
    def status(cls):
        print("Nike Bangladesh Status:")
        print("Branches Opened: ", cls.branches_opened)
        print("Currently Stocked")
        print(cls.total_stock)
        print("Sold:", cls.total_sold)

    def details(self):
        print(f"{self.branch_name} outlet:")
        print("Products Currently Stocked: ")
        print(self.stock)
        print("Sold:", self.sold)

    def restockProducts(self, restock_dict):
        for product, quantity in restock_dict.items():
            self.stock[product] += quantity
            NikeBangladesh.total_stock[product] += quantity

    def productSold(self, sold_dict):
        for product, quantity in sold_dict.items():
            if self.stock[product] >= quantity:
                self.stock[product] -= quantity
                NikeBangladesh.total_stock[product] -= quantity
                self.sold += quantity
                NikeBangladesh.total_sold += quantity
            else:
                print(f"Error: Insufficient stock of {product} in {self.branch_name} outlet.")


print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts({"Air Jordan": 1200, "Cortez": 200, "Zoom Kobe": 200})
chittagong.restockProducts({"Air Jordan": 1000, "Cortez": 250, "Zoom Kobe": 100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan": 760, "Cortez": 90})
chittagong.productSold({"Air Jordan": 520, "Zoom Kobe": 70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()

#task 5
class Student:
  ts = 0
  bracUs = 0
  ois = 0
  def __init__(self,name, dept,uni = 'BRAC University'):
     self.name = name
     self.dept = dept
     self.uni = uni
     Student.ts += 1
     if self.uni == 'BRAC University':
       Student.bracUs += 1
     else:
       Student.ois += 1
  @classmethod
  def printDetails(cls):
    print(f'Total Student(s):{cls.ts}\nBRAC University Student(s): {cls.bracUs}\nOther Institution Student(s): {cls.ois}')
  @classmethod
  def createStudent(cls,a,b,c = 'BRAC University' ):
    return cls(a,b,c)
  def individualDetail(self):
    print(f'Name: {self.name}\nDepartment:{self.dept}\nInstitutions:{self.uni}')



Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

#task6
class SultansDine:
  branches = 0
  sell = 0
  lst = []
  def __init__(self,name):
    self.name = name
    SultansDine.branches += 1
  def sellQuantity(self,num):
     self.quantity = num
     if num < 10:
       self.quantity = num*300
     elif num <20:
       self.quantity = num*350
     else:
       self.quantity = num*400
     SultansDine.sell += self.quantity
  def  branchInformation(self):
    print(f'Branch name:{self.name}\nBranch Sell:{self.quantity} taka')
    SultansDine.lst.append(self.name)
    SultansDine.lst.append(self.quantity)



  @classmethod
  def details(cls):
     print(f'Total Number of branch(s):{cls.branches}\nTotal sell:{cls.sell}')
     for i in range(0,len(cls.lst),2):
       print(f'Branch Name:{cls.lst[i]} Branch sell:{cls.lst[i+1]}')
       print(f"Branch consists of total sell's:{(cls.lst[i+1]/cls.sell)*100:.2f}%")




SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()