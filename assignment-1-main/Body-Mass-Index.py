w = float(input("enter your weight in KG:"))
h = float(input("enter your height in M:"))

bmi = w / h**2

if bmi<18.5:
    print("BMI:" , bmi , "underweught")
elif bmi>=18.5 and bmi<=24.9:
      print("BMI:" , bmi , "normal")
elif bmi>=25 and bmi<=29.9:
     print("BMI:" , bmi , "overweight")
elif bmi>=30 and bmi<=34.9:
     print("BMI:" , bmi , "obese")
elif bmi>=35:
     print("BMI:" , bmi , "extremely obese")

    