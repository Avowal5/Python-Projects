number1 = int(input("Please type in a temperature (F)" ))
converted_number = (number1 - 32) * 5/9

print(f"{number1} degrees Fahrenheit equals {converted_number} degrees Celsius")


if converted_number < 0:
    print("Brr! It's cold in here!")
