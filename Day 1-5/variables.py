#a variable is a name assigned to data (a value) to serve as an identifier. it also allows for the programmer to manipulate the data stored in that variable.
name1 = "Prince"
print(name1)

name2 = input("what is your name?")
print(name2)

#find length of string with len()
print(len(name2))

username = input("please enter your name: \n")
uname_length = str(len(username))

print(username + " " + "your name length is: " + uname_length)

print(len(input("What is thy name? ")))