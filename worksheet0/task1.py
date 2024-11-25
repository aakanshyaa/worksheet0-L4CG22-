cold = []
mild = []
comfortable = []

temperatures = [5, 12, 18, 3, 15, 10, 20, 14, 8]

for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp < 20:
        comfortable.append(temp)

print("Cold temperatures:", cold)
print("Mild temperatures:", mild)
print("Comfortable temperatures:", comfortable)
