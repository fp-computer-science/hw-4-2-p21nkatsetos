# Author: NJK (AMDG) 10/12/20

height = float(input("what is your height in meters? "))
weight = float(input("what is your weight in kilograms? "))
bmi = int(weight) / int(height ** 2)
print(bmi)

if bmi < 19:
    print("Underweight")
else:
    if bmi >= 19 and bmi < 25:
        print("Healthy")
    else:
        if bmi >= 25 and bmi < 30:
            print("Overweight")
        else:
            if bmi >= 30 and bmi < 40:
                print("Obese")
            else:
                if bmi > 40:
                    print("Extremely obese ")
