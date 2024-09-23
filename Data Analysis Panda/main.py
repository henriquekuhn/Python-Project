import os
import pandas

DIR = os.getcwd() + "/Data Analysis Panda"
os.chdir(DIR)

# Get CSV data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240307.csv")

# Count GRAY squirrel
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

# Count RED squirrel
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# Count CINNAMON squirrel
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(f"Number of gray squirrel: {gray_squirrel_count}")
print(f"Number of black squirrel: {black_squirrel_count}")
print(f"Number of cinnamon squirrel: {cinnamon_squirrel_count}")

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

new_dataframe = pandas.DataFrame(data_dict)
new_dataframe.to_csv("squirrel_count.csv")