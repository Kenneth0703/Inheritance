import personClass as p

name = "John"
address = "102"
phone= "123-213"
customer_number = 3123
mailing_list = True

person1 = p.Person(name,address,phone)

customer1 = p.Customer(name,address,phone,customer_number,mailing_list)

person1.print_person()

print()
print()
print()

customer1.print_person()