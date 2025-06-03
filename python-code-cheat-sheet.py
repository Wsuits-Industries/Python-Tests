#FREE CHEAT SHEET OOHH PLEASE LIKE SHARE FOR WSUITS INDUSTRIES
#Varibales are containes for storing Data
Company = "wsuits Industries"
Ceo = "Alhassan Osman Wunpini"

#the print statement is used for Printing Out data into the terminal
print("The greatest company in the world id " + Company)
print(f"{Ceo} is the CEO of {Company}")

#Casting is used to specify the data type of a Variable
name = str("Osman")
#str() is use to specify the string Data Types
age = int(18)
#int() is used to specify integer data types
btcPerHour = float(9.9)
#float() is used to specify float Data Types

#print out the values in the varibles using concatination
print(f"{name} is {age} years old and he earns {btcPerHour} BTC per hour")

#TO get the type of data stord in a Varibale we use the type() fuction
money = "500+ billion USD"
age = 18
#printing out the type of data stored in the variables
print(type(money))
print(type(money))

#assigning Multiple Values
x,y,z = 11,22,33
print(x,y,z)

#asingning one value to multiple Variables
x = y = z = "One Value is this ahah"
print(x,y,z)

#outputing Varibale Values
xx = 33
yy = 44
zz = 55
#Adding all the values since htey are all Intergers and can be added to eachother
print(xx + zz + zz)

#FUNCTIONS IN PYTHON
def fuction(name):
    #this fuction will say hello when you call it with your name
    print("hello " + name)

#calling the function
fuction("osman")

#GLOBAL VARIBALES
varname = "hello"
#varna,e is a global fuciton becuase it is outside a fuction
def newfunc(name):
    print(varname + name)
#callin the fuciton
newfunc("Wunpini")

#LOCAL VARIABLES
def localfunc(name):
    localvariable = "Hello"
    #this is a local fuction cause it is declared ina fuction
    print(localvariable + name)

#calling the fuction
localfunc("Maltiti")

#LISTS IN PYTHON

#a list is a collection of any types of data
newList = ["name", "another", 4.5, 123, 3.2, "blahblah", "hope you get it now"]
print(newList)

#Printing Out the elemtn of a list
#note hte first element of the list starts with a 0 index
print("The First ELement is: "+newList[0])
print("The Second Element is:" + newList[1])
print("The Third Item is:" + str(newList[2]))


#python loops
#===============================
#===============================
#===============================

#for loops
#===============================
passwordsList = ["123","admin","Admin","Root","root"]

for password in passwordsList:
    print(f"Trying Password {password}")


#while Loops

password = ""
attempts = 0
correct_password = "root"

while password != correct_password:
    password = input("Enter password: ")
    attempts += 1

print(f"Access granted after {attempts} attempts!")
