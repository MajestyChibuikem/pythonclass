bakeryList = ["bread", "cake", "donuts", "cookies", "muffins", "strawberry cake"]

# classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", " chisom", "irene", "pascal", "jude", "daniel" ]

# # function check through my list for strawberry cake
def checkStock(pastry):
    counter = 0
    for item in pastry:
        if item != "strawberry cake":
          counter += 1
          # print(counter, " loop")
          continue
        else:
            return "we have strawberry cake in stock"
checkStock(bakeryList)

# def add2():
#     num1 = 10
#     num2 = 20
#     sum = num1 + num2
#     return sum

# theSum = add2()
# print(theSum)