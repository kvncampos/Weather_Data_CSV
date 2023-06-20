# with open("weather_data.csv") as r:
#     data = r.read().splitlines()
#     print(data)

# Using CSV Module
# import csv
#
# with open("weather_data.csv") as r:
#     data = csv.reader(r)
#     temperatures = []
#
#     for row in data:
#         temps = row[1]
#         try:
#             temperatures.append(int(temps))
#         except ValueError:
#             pass
#     print(temperatures)

import pandas
import statistics


def calculate_average(numbers):
    """Using Statistics Import and Mean Module, Round to 2 Decimals"""
    average = statistics.mean(numbers)
    average_rounded = round(average, 2)  # Round to two decimal places
    return average_rounded


def calculate_average_v2(numbers):
    """Calculate Average Integers without Module. Sum/Len and Round to 2 Decimals"""
    average = sum(numbers) / len(numbers)
    average_rounded = round(average, 2)
    return average_rounded


data = pandas.read_csv("weather_data.csv")
average_temp = round(data["temp"].mean(), 2)
# print(f"Average Temp: {average_temp}")
max_temp = data["temp"].max()
# print(f"Max Temp: {max_temp}")

# Print the 'Whole Table'
# print(data)
# Get Data in Columns
# print(data.day)

# Get data in a Row
# print(data[data.day == "Monday"])

# Get Row with MAX Temp
# print(data.nlargest(n=1, columns="temp"))
# OR
# print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]


# print(monday.condition)


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


monday_temp = int(monday.temp.iloc[0])
print(f"Fah = {convert_celsius_to_fahrenheit(monday_temp)}")


# Create Dataframe from Scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")
