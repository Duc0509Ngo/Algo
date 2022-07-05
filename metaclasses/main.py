# class Test:
#     def hello(self):
#         print("Hello")
#     pass


# MetaTest = type('MetaTest', (Test,), {'x': 1})
# mt = MetaTest()
# mt.hello()

#declare Meta class inherit from type

# class Meta(type):
#     def __new__(cls, class_name, bases, attrs):
#         print('class_name: {}'.format(class_name))
#         print('bases: {}'.format(bases))
#         print('attrs: {}'.format(attrs))
#         a = {}
#         for name, val in attrs.items():
#             if name.startswith('__'):
#                 a[name] = val
#             else:
#                 a[name.upper()] = val
#         print(a)     
#         return type(class_name, bases, a)



# class Dog(metaclass=Meta):
#     x = 5
#     y = 9

#     def hello(self):
#         print("hi")

#metaclass is a class that is used to define the class of a class
# class Animal:
#     def hello(self):
#         print("hi")

# Dog = type('Dog', (Animal,), {'x': 5, 'y': 9})
# dog = Dog()
# dog.hello()

# class Foo:
#     pass
# x = Foo()
# print(type(x))
# #result: <class '__main__.Foo'>
# print(type(Foo))
#result: <class 'type'>

#The type of x is class Foo, as you would expect.
#But the type of Foo, the class itself, is type. In general,
#the type of any new-style class is type.
#In the above case:
#x is an instance of class Foo.
#Foo is an instance of the type metaclass.
#type is also an instance of the type metaclass, so it is an instance of itself.

class Meta():
    def __init__(cls, name, bases, dict):
        print(cls)
        cls.attr = 10


class X(metaclass=Meta):
    pass
class Y(metaclass=Meta):
    pass

X = type('X', (), {})
print(X)
# print('-'*13)

# print(X)





    

