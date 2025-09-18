# dog
# constructor - name, breed
# method Bark - print "woof woof"
"""
dog class
"""
class Dog:
    #contructor
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
    
    #method - woof woof - bark
    def bark(self):
        print("woof woof")

"""
cat class
"""
class Cat:
    #constructor
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
    
    def meow(self):
        print("meow meow")
    
    def printName(self):
        print(self.name)
    def __str__(self):
        # return f"{self.name}, {self.breed}"
        return "this class requires a name and breed\nmajesty"

# myDog = Dog("sparky", "mastiff")
# myDog.bark()
myCat = Cat("Clover", "persian")

myCat.name = "alcatraz"
# del myCat.breed
# myCat.meow()
myCat.printName()
print(myCat.breed)



