# Vehicle Details and Premium ammount

class vehicle:
    def __init__(self,id,type,cost):
        self.__id=id
        self.__type=type
        self.__cost=cost
        self.__premium_amount=0

    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_type(self,type):
        if type =="Four Wheeler" or type=="Two wheeler":
            self.__type=type
        else:
            print("Invalid Input")
    def get_type(self):
        return self.__type

    def set_cost(self,cost):
        self.__cost = cost
    def get_cost(self):
        return self.__cost

    def premium_amount(self):
        if self.__type=="Two Wheeler":
            self.__premium_amount=0.02*self.__cost
        elif self.__type=="Four Wheeler":
            self.__premium_amount=0.06*self.__cost
        return self.__premium_amount

    def display(self):
        print(self.__id,self.__type,self.__cost,self.__premium_amount)

v=vehicle(101,"Two Wheeler",90000)
# v.set_id(200)
v.premium_amount()
v.display()

# ------------------------------------------------------------------------------------------

# Admission process and course selection of a student in a university

class student:
    def __init__(self):
        self.__id=None
        self.__marks=None
        self.__age=None
        self.__course=None
        self.__discount_price=0

    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_course(self,course):
        self.__course=course
    def get_course(self):
        return self.__course

    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False

    def validate_age(self,):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if (self.validate_marks()==True and self.validate_age()==True and self.__marks>=65):
            return True
        else:
            return False

    def course_selection(self,):
        if self.check_qualification()==True:
            if self.__marks>85:
                if self.__course==1001:
                    self.__discount_price=25575-25575*0.25
                elif self.__course==1002:
                    self.__discount_price = 15500 - 15500 * 0.25
            else:
                if self.__course == 1001:
                    self.__discount_price = 25575
                elif self.__course == 1002:
                    self.__discount_price = 15500
        return self.__discount_price

    def display(self):
        if self.check_qualification()==False:
            print("Student having id: ",self.__id," is not eligible for admission")
        else:
            print("Student having id: ",self.__id," is qualified and the course price is",self.__discount_price)

s1=student()
s1.set_id(101)
s1.set_age(22)
s1.set_marks(87)
s1.set_course(1001)

s1.validate_age()
s1.validate_marks()
s1.course_selection()
s1.display()
# ------------------------------------------------------------------------------------------

# pizza service-->In person and Home delivery service
types=["small","medium","Small","Medium"]
class customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and customer.validate_quantity(self.__customer):
            if self.__pizza_type.title()=="Small":
                self.pizza_cost=150*customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=35*customer.get_quantity(self.__customer)
            if self.__pizza_type.title()=="Medium":
                self.pizza_cost=200*customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=50*customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id=self.__pizza_type[0]+str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms
        Pizzaservice.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                distance=1
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost+=5
                    if distance in range(6,11):
                        self.pizza_cost+=7
                    distance+=1
        else:
            self.pizza_cost=-1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms

c = customer("Asha",5)
p1 = Pizzaservice(c,"MEDIUM",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1=Doordelivery(c,"MEDIUM",True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())








