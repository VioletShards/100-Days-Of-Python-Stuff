# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)