#NOTE: len() func does not accept int
print(len("banana"))
#anything wrapped in quotes is a str
# Type Checking
print(type("booboo"))
print(type(2.555))
print(type(203))
print(type(True))

#Type Conversion
print(int("123") + int("654"))

print(float("2.55") * float("2.55"))

print(int("10") * int("6"))

user_name = input("Enter your name?") #assign var to input and name length
name_length = len(user_name)

print(type("Number of letters in your name: ")) #prints the "len" of the contents of the name var
print(type(name_length))

print("Number of letters in your name: " + str(name_length))

#NOTE: YOU CANNOT CONCATENATE INT + STR. ONLY STR TO STR