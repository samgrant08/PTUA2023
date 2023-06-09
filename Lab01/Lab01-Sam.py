x = "hello world"
y = ["hello world!", 3, [2,4]]
print(y)
x,y,z = "Orange", 2, [1,3,4]
print(1+2, [x+"apple",4])
z = [1,2]
z.append(3)
print(z)
del z[0]
print(z)

##Define a dictionary. This is key based! 1 is assigned to hello, 3 is assigned to bye. Keys and values.
x5 = {1: " hello e", 3: "bye"}
print(x5[1].strip()) ##note that we index by 1 here becaues its a dictionary.
print(x5[1])
a= "Hello world!"
print("string 'a' is: ", a)
b = a.lower()
print(b)
c= a.upper
print(c)


##String functions. Remove white space from words
d = "  a   Hello World    b    "
e=d.strip().split() ##removes white spaces and puts words in a list
print(e)

x=6
y=x
print(y)

##More about dictionaries. You cant copy a dictionary simply by typing dict2 =dict1, because: dict2 will only be a referenence
# to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are way to make a copy, one way is to use the built-in dictionary method copy()

cardict = {
    "brand": "Honda",
    "model": "Accord",
    "year": 2015
}
print("cardict is:", cardict)

##now reassign the year
cardict["year"] = 2007
print(cardict)
cardict[2]= 2001
print(cardict)
del cardict[2]
print(cardict) 


### if, elif and else commands
a = 100
b = 50
if b>a:
    print("hello")
elif  a==b:
    print("bye")
else:
    print("hi")

##################LOOPS!
# Two types of loops. For loops: iterating over a sequency ( a list, tuple, a dictionary, a set, or a string)   
# 
# 
students = ["bob", "kat", "jon", "tracy"] 
for x in students:
    print(x)
    if x == "bob":
        print("this is bob")
    else:
        print("this is not bob, this is", x)  

##you can use  a break statement within your for loops - this helps with debugging

for x in students:   ##for this loop, if x!=kat it breaks. For the first iteration x==kat hence it prints kat. For the second iteration the if statement is satisfied so code breaks
     if x =="kat":
         break
     print(x)

for x in students:   ##for this loop, if x!=bob it breaks. For the first iteration x==bob hence it prints bob. For the second iteration the if statement is satisfied so code breaks
     if x =="bob":
         continue
     print(x)

##loop between 0 and 4
for x in range(5):
    print(x)

## loop starts at 2 and ends at 4   
for x in range(2,5):
    print(x)

    
# loop starts at 2, ends at 20, goes up by 5
for x in range(2,20,5):
    print(x)

##WHILE LOOPS: continues to execute a loop while statement is true

i = 1
while i<6:
    print(i)
    i+=1  #this is another way of writing i = i+1  
    
 ##FUNCTIONS  
 ##use "def" to define a function

def testfunction(a):
    if a >4:
        print("hello world")
    else: print("Hello, ", a)

x = testfunction(1)


##you can also write functions with default parameters
def testfunction1(a=3):
    print("hello")

testfunction1()

##Helloooo




 ##MODULES 
 import random as rn

rn.randint(1,5)

rn.random()


