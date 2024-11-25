temperatures = [2, 14, 18, 4, 12, 10, 20, 16, 7]

temperatures_fahrenheit = []

for temp in temperatures:
    fahrenheit = (temp * 9 / 5) + 32
    temperatures_fahrenheit.append(fahrenheit)

print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
