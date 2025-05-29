# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature =[]
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperature.append(int(row[1]))
#     print(temperature)

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_in_list = data["temp"].tolist()
# #
# # series = data["temp"]
# # #
# # # largest = series.nlargest(n=1)
# # # print(largest)
# #
# # monday = data[data.temp == "monday"]
# # monday_temp

import pandas
import pyarrow

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_in_a_list = squirrel_data["Unique Squirrel ID"].tolist()

squirrel_number = len(squirrel_in_a_list)

squirrel_color_in_a_list = squirrel_data["Primary Fur Color"].tolist()

squirrel_in_black = squirrel_color_in_a_list.count("Black")
squirrel_in_gray = squirrel_color_in_a_list.count("Gray")
squirrel_in_cinnamon = squirrel_color_in_a_list.count("Cinnamon")

# creating a new data frame with the derived data

new_data = {
    "fur": [],
    "color": ["gray", "black", "cinnamon"],
    "count": [squirrel_in_gray, squirrel_in_black, squirrel_in_cinnamon]
}

derived_data_frame = pandas.DataFrame(new_data)
derived_data_frame.to_csv("new_file")
