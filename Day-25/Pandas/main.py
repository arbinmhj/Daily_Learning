# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather-data.csv")
# print(type(data))
# print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)
# average = sum(temp_list) / len(temp_list)
# print(average)
print(data.temp.mean())
print(data.temp.max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
max_temp = data.temp.max()
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)
fah = (int(monday.temp) * 1.8) + 32
print(fah)

# Create dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
