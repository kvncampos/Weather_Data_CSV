import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

total_per_color = data.groupby(['Primary Fur Color']).size()
print("The Total Squirrels were:\n")
print(total_per_color)

with open("squirrel_count.txt", "w") as count:
    count.write("The Total Squirrels were:\n")
    count.write(total_per_color.to_string(header=True, index=True))
