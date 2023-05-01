def input(weight, height):
    # Here we create our function followed by the formular
    bmi = weight / (height ** 2)
    return bmi



def bmi_result(bmi):
    # Here we create the conditions for the result
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

# Ask for the users input
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

# Calculate calculate the input and put it in the right category
bmi = input(weight, height)
category = bmi_result(bmi)

#Show category
print(category)
