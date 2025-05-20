temp_c = float(input("Enter temperature in Celsius: "))

if temp_c > 0:
    fahrenheit = (temp_c * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
else:
    kelvin = temp_c + 273.15
    print("Temperature in Kelvin:", kelvin)
