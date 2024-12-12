# We are going to be building a Celsius to Fahrenheit Converter
# Firstly we take input in Celsius
temp_in_celsius = float(input("Please enter the temperature in celsius: "))
temp_scales = {"Celsius":"°C", "Fahrenheit":"°F"}

# Then we calculate it in Fahrenheit
temp_in_fahrenheit = temp_in_celsius * ((9/5) + 32)
print("The temperature in fahrenheit = ", temp_in_fahrenheit, temp_scales["Fahrenheit"])