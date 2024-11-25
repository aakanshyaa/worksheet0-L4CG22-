temperatures = [5, 6, 7, 5, 4, 6, 8, 9, 12, 13, 14, 12, 15, 10, 11, 14, 18, 20, 19, 17, 16, 15, 14, 13]

night = []  
evening = []  
day = []  

for hour, temp in enumerate(temperatures):
    if 0 <= hour < 8:  
        night.append(temp)
    elif 8 <= hour < 16:  
        evening.append(temp)
    elif 16 <= hour < 24:   
        day.append(temp)

average_day_temp = sum(day) / len(day) if day else 0  
print("Night temperatures:", night)
print("Evening temperatures:", evening)
print("Day temperatures:", day)
print(f"Average day-time temperature: {average_day_temp:.2f}°C")
