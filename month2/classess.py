class User:
    # firstname = "majesty"
    # lastname = "chibuikem"
    # age = 30
    # sex = "gay"
    # nationality = "ibiza"
    # email = "chichi@gmail.com"
    # phone = "77"
    def __init__(self,firstname, lastname, age, sex, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.email = email
        self.phone = phone
#object of the class User
user1 = User("majesty", "chibuikem", 30, "gay", "ibiza", "chichi@gmail.com", 7777)
print(user1.firstname)



# print(user1.firstname)
# print(user1.lastname)
# print(user1.age)
# print(user1.sex)
# print(user1.nationality)
# print(user1.email)
# print(user1.phone)

