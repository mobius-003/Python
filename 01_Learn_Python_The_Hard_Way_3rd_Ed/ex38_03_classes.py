#Inheritance
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak (self):
#         print("Meow")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.name = age
#
#     def speak(self):
#         print("Bark")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

class Cat(Pet):
    def speak (self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.show()
c.speak()
d = Dog("Jill", 25)
d.show()
d.speak()
