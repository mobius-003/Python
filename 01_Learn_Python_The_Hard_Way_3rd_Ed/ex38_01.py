# def hello ():
#   print ("hello")
#
# x =1
# print(type(x))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#
#     def bark():
#         print ("bark")
# d = Dog()
# print(type(d))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#
#     def bark(self):
#         print ("bark")
# d = Dog()
# d.bark()
# print(type(d))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#
#     def meow(self):
#         return " meow "
#     def bark (self):
#         print("bark")
#
#
# d = Dog()
# d.bark()
# print(type(d))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#
#     def add_one(self, x):
#         return x +1
#     def bark (self):
#         print("bark")
#
#
# d = Dog()
# d.bark()
# print(d.add_one(5))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         print(name)
#
#     def add_one(self, x):
#         return x + 1
#
#     def bark(self):
#         print("bark")
#
# d = Dog("Tim")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         print(name)
#
#     def add_one(self, x):
#         return x + 1
#
#     def bark(self):
#         print("bark")
#
# d = Dog("Tim")
# d2 = Dog("Bill")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name (self):
#         return self.name
#
# d = Dog("Tim")
# print(d.get_name())
# d2 = Dog("Bill")
# print(d2.get_name())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
#
#     def get_name (self):
#         return self.name
#
# d = Dog("Tim", 34)
# print(d.get_name())
# d2 = Dog("Bill", 12)
# print(d2.get_name())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
#
#     def get_name (self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
# d = Dog("Tim", 34)
# d.set_age(23)
# print(d.get_age())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
#
#     def get_name (self):
#         return self.name
#
#     def get_age(self):
#         return self.age
# 
#     def set_age(self, age):
#         self.age = age
#
# dog1_name = "Tim"
# dog2_age = 34
