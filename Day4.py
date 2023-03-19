#nearest pallindrome

import sys

def next_smallest_pallindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(next_smallest_pallindrome(99))
print(next_smallest_pallindrome(1221))

# ------------------------------------------------------------------------------------------

# max visited speciality
def max_visited_speciality(pateient_medical_speciality_list,medical_specilaity):
    # max_visit=0
    P=pateient_medical_speciality_list.count('p')
    O=pateient_medical_speciality_list.count('O')
    E=pateient_medical_speciality_list.count('E')
    if P>E and P>O:
        speciality =medical_specilaity['P']
    elif E>O:
        speciality=medical_specilaity['E']
    else:
        speciality=medical_specilaity['O']
    return speciality
pateient_medical_speciality_list=[101,'P',102,'O',302,'P',305,'P']
medical_specilaity={"P":"pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(pateient_medical_speciality_list,medical_specilaity)
print(speciality)

# ------------------------------------------------------------------------------------------

# finding the common letters from the two given strings

s1=input().replace(" ",'')
s2=input().replace(" ",'')
a,b,c=[],[],[]
for i in s1:
    a.append(i)
for i in s2:
    b.append(i)
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
d=''
for i in c:
    d+=i
print(d)
# ------------------------------------------------------------------------------------------

#OOPS concept

class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
# ------------------------------------------------------------------------------------------
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
# ------------------------------------------------------------------------------------------
class customer:
    def __init__(self):
        self.cust_id=100
c1=customer()
print(c1.cust_id)
# ------------------------------------------------------------------------------------------
class customer:
    def __init__(self,id):
        self.id=100
c1=customer(200)
print(c1.id)
# ------------------------------------------------------------------------------------------

class Book:
    def __init__(self):
        self.title=None
my_fav_book=Book()
my_fav_book.title="Head first Programming"
your_fav_book=Book()
your_fav_book.title="Learn python the hard way"
my_fav_book.title="Learning python"

print(my_fav_book.title)
print(your_fav_book.title)
# ------------------------------------------------------------------------------------------
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print(s1.price,s1.material)
# ------------------------------------------------------------------------------------------
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print("The unique id of s1 is:",id(s1))

# ------------------------------------------------------------------------------------------
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "shoe with price: "+str(self.price)+"and material: "+self.material
s1=shoe(1000,"canvas")
print(s1)
# ------------------------------------------------------------------------------------------
class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
mobile().purchase()
mobile().purchase()
# ------------------------------------------------------------------------------------------

class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.Total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.Total_price=self.price-self.price*(discount/100)
        print("Total price of ",self.brand,"mobile is:",self.Total_price)
    def amount_returned(self):
        return self.price-self.Total_price
mob1=mobile("Apple",20000)
mob2=mobile("samsung",10000)
mob1.purchase()
print("Amount returned ",mob1.amount_returned())
mob2.purchase()
print("Amount returned ",mob2.amount_returned())
# ------------------------------------------------------------------------------------------
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.age=age
        self.name=name
        self.__wallet_balance=wallet_balance
    def set_balance(self,ammount):
        if ammount<50000 and ammount>0:
            self.__wallet_balance+=ammount
    def show_balance(self):
        print("the Wallet balance is: ",self.__wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24,1000)
c1.set_balance(50000)
c1.show_balance()
print(c1.get_wallet_balance())

# ------------------------------------------------------------------------------------------
class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name",dam1.name)
print("Dam Length:",dam1.get_length())

# ------------------------------------------------------------------------------------------

class table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top):
            rate=30000
        else:
            rate=0
        return rate
dining_table=table()
rate=dining_table.identify_rate(False,True)
print(rate)

# ------------------------------------------------------------------------------------------

class Table:
    def __init__(self):
        self.no_of_legs = 4
        self.__glass_top = None
        self.__wooden_top = None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)