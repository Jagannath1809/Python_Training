#privileged Customer

class OverdrawException(Exception):
    pass
class LimitReachedException(Exception):
    pass

class Account:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type=account_type
        self.__balance=balance
        self.__min_balance=min_balance
    def get_account_type(self):
        return self.__account_type
    def set_balance(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def get_min_balance(self):
        return self.__min_balance


class customer:
    def __init__(self,id,name,age,account):
        self.__id=id
        self.__name=name
        self.__age=age
        self.__account=account
    def withdraw(self,ammount):
        balance=Account.get_balance(self.__account)
        min_balance=Account.get_min_balance(self.__account)
        new_balance=balance-ammount
        if ammount>balance:
            raise OverdrawException
        elif new_balance<min_balance:
            raise LimitReachedException
        Account.set_balance(self.__account,new_balance)

    def take_card(self):
        print("Take card out from the ATM")

    def get_customer_id(self):
        return self.__id
    def get_customer_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_account(self):
        return self.__account


class PrivilegedCustomer(customer):
    def __init__(self,id,name,age,account,bonus_points):
        super().__init__(id,name,age,account)
        self.__bonus_points=bonus_points

    def increase_bonus(self):
        Account=self.get_account()
        balance=Account.get_balance()
        if balance>1000:
            self.__bonus_points+=10
        else:
            self.__bonus_points+=2

    def withdraw(self,ammount):
        customer.withdraw(self,ammount)
        self.increase_bonus()

    def get_bonus_points(self):
        return self.__bonus_points

a = Account("Savings",1000,500)
c = customer("100","Gopal",43,a)
p = PrivilegedCustomer("c101","Sudarshan",22,a,100)

try:
    print("Customer Id: "+str(c.get_customer_id()))
    print("Customer Name: "+c.get_customer_name())
    print("Age: "+str(c.get_age()))
    print("Account Type: "+a.get_account_type())
    print("Account Balance: "+str(a.get_balance()))
    print("Account minimum: "+str(a.get_min_balance()))
    p.withdraw(400)
    print("Account Balance after withdraw: "+str(a.get_balance()))
    print("Bonus Points: "+str(p.get_bonus_points()))
except OverdrawException:
    print("amount to be withdrawn is greater than account balance.")
except LimitReachedException:
    print("balance amount is less than minimum account balance.")
finally:
    c.take_card()


