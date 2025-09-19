class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printFullname(self):
        print(self.fname + " "+ self.lname)
    


class Student(Person):
    def printLname(self):
        print(self.lname)

me = Person("majesty", "chibuikem")
me.printFullname()
sanctus = Student("sanctus", "cisco")
sanctus.printFullname()
sanctus.printLname




def myfunc():
  global x
  x = 300
  print(x)

print(x)

myfunc()


