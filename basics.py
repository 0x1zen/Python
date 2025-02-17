mylist=[1,2,2,2,2,'a',77]
mylist2=['abcd',23895]
mylist.extend(mylist2)
mylist[1]=mylist[5]  #modifying via indexes
print(mylist)
# index=mylist.index('a')
# print(index)

# mytuple=(1,3,4,5)
# mytuple[1]=mytuple[1]+mytuple[2] #will throw error
# print(mytuple) 

mySingleList=[1]

# index=mytuple.index('a')
# print(type(mySingleList))


# print(type(mytuple))

thistuple = ("apple", "banana", "cherry","watermelon","papaya")
(apple,*remainingFruits,papaya)=thistuple

print(remainingFruits)

thisset={1,True,"abc",False,0,23423};
print(thisset)

myset=set({1,2,3,4})
mynewlist=list([2,3,4,'a'])
mynewtuple=tuple((1,))
print(myset,mynewlist,mynewtuple)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# thisset.add("watermelon")

# print(thisset)

# mytuple=(1,2,5,4)
# convertedTuple=list(mytuple)
# print(convertedTuple)
# convertedTuple[0]=convertedTuple[0]+100
# mytuple=tuple(convertedTuple)
# print(mytuple)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

thisset.add("watermelon")

thisset.discard("apple")

print(thisset)

set1 = {1,"a", "b", "c"}
set2 = {1, 2, 3}


# set2=set1.intersection(set2)
set3=set1.symmetric_difference(set2)
print(set3)

myKye='title'
mydict={myKye:'value'}
x=mydict.items()
print(x)

mydict={"name":"raj","email":"rajop"}


def my_function(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} , {value}')

my_function(name="Alice",age=30, location="jersey")

def print_country(country="india"):
    print(country)

print_country("sweden")

def my_lambda(n):
    return lambda a:a*n

mydoubler=my_lambda(2)
mytripler=my_lambda(3)

print(mydoubler(11))
print(mytripler(12))

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return f'my first name is {self.fname} and my last name is {self.lname}'

# p1=Person("John",23)
# print(p1)
# del p1.age
# print(p1.age)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

print(x,x.graduationyear)

mytuple=("apple","banana","cherry")
myit=iter(mytuple)

print(next(myit))

def print_my_tuple(mytuple):
    for item in mytuple:
        print(item)
    

print_my_tuple(mytuple)

class MyNumbers():
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        self.a+=1
        return self.a
        
myobj=MyNumbers()
myit=iter(myobj)
print(next(myit))

class Animal:
    def make_sound(self):
        raise NotImplementedError("subclass must implement abstract method")
    def make_alt_sound(self):
        raise NotImplementedError("subclass must implement abstract method")

class Dog(Animal):
    def make_sound(self):
        return "woof!"
class Cat(Animal):
    def make_sound(self):
        return "mewo!"
    def make_alt_sound(self):
        return "meow2"
def animal_sound(animal):
    print(animal.make_sound())

dog=Dog()

animal_sound(dog)


def myNewFunc():
    
    def myNewFuncNested():
        x="local var"
    myNewFuncNested()
    print(x)
myNewFunc()

from mymodule import myfunc 

myfunc("raj")