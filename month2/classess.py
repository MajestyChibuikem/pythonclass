class User:

    """
    a constructor to get user data
    """
    def __init__(self,firstname, lastname, age, sex, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.email = email
        self.phone = phone

    """
    method to return first name
    """

    def print_firstname(self):
        print(self.firstname)
    

#object of the class User
userMajesty = User("majesty", "chibuikem", 30, "gay", "ibiza", "chichi@gmail.com", 7777)
userDaniel = User("Daniel", "onyenta", 12, "child", "israel", "danielos@gmail.com", 8888)


userMajesty.print_firstname()
userDaniel.print_firstname()


# print(user1.firstname)
# print(user1.lastname)
# print(user1.age)
# print(user1.sex)
# print(user1.nationality)
# print(user1.email)
print(userMajesty.phone)

