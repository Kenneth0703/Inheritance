

class Person:

    def __init__(self,name,address,telephone_number):
        self.name = name
        self.address = address
        self.telephone_number = telephone_number

    def print_person(self):
        print(self.name)
        print(self.address)
        print(self.telephone_number)

class Customer(Person):

    def __init__(self,customer_number,mailing_list):
        Person.__init__(self,customer_number)

        self.mailing_list = mailing_list
        



    def print_person(self):
        print(self.name)
        print(self.address)
        print(self.telephone_number)

    def get_customer_number(self):
        return customer_number

        


