

class Person:

    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    
    def print_person(self):
        print("Name:",self.name)
        print("Address:",self.address)
        print("Phone Number:",self.phone)

class Customer(Person):

    def __init__(self,name,address,phone,customer_number,mailing_list):
        Person.__init__(self,name,address,phone)

        self.customer_number = customer_number
        self.__mailing_list = mailing_list
        
    def print_person(self):
        Person.print_person(self)          # does the same as tje last three lines                                                             
        # print("Name: ", self.name)
        # print("Address: ", self.address)
        # print("Phone Number: " ,self.phone)
        print("METHOD 2")
        print()
        print(f"Name:{Person.get_name(self)}")
        print(f"Address: {Person.get_address(self)}")
        print(f"Phone: {Person.get_phone(self)}")
        print("Customer Number: ", self.customer_number)   # do this for everyone
        if self.customer_number:
            print("On mailing list: Yes")
        else:
            print("On mailing list: no")



    def get_customer_number(self):
        return self.customer_number

        


