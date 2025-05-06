class SimpleClass:
   var1 = 2
   def method(self):
       print(self.var1)

object_one =SimpleClass()
object_two =SimpleClass()

object_one.vara=3
object_one.vara=5

# print(object_one.vara)
# print(object_two.vara)

class Transport:
    def __init__(self,air,water):
        self.air=air
        self.water=water
obj_transport= Transport(air= "Beluga", water="sevt")
# print(obj_transport.air,obj_transport.water)

# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         # print(self.fname,self.lname)
# x = Person(fname="Jane",lname="Doe")
# # x.printname()
class ShoppingCart:
    def __init__(self):
        self.items=[]
    def add_item(self ,item_name, qty):
        self.items.append(item_name)
    def remove_item(self, item_name):
        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break
    def calculate_total(self):
        total=0
        for item in self.items:
            total += item[1]
        return total

cart = ShoppingCart()

cart.add_item(item_name="banana",qty="80")
cart.add_item(item_name="strawberries",qty="100")
cart.add_item(item_name="potatoes",qty="200")

print("Current items in the cart")
for item in cart.items:
    print(item[0]," ", item[4])

total_qty=cart.calculate_total()
print("Total Quantity:",total_qty)