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
