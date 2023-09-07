#------------------------ csv without pandas ------------------------
import csv

with open(r"C:\Users\Himisha\OneDrive\Desktop\Python\day 25\weather_data.csv") as f:
    d =  csv.reader(f)
    temperature = []
    for line in d:
        if line[1] != "temp":
            temperature.append(int(line[1]))

    print(temperature)
