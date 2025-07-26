#bmi = weight(kg) / (height(m))^2

print("Hi! Welcome to the BMI Calculator!✨\n")
weight = float(input("What is your weight(kg)?⚖️\n"))
height = float(input("What is your height(m)?📏\n"))
bmi = weight / height**2

print(f"Your BMI is {bmi}!🧮")