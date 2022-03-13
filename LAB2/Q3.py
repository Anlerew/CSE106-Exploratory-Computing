import pandas as pd

weather_data = pd.read_csv('weather_data.txt')

print("(A)\n")
weather_data = pd.read_csv("weather_data.txt")
find = weather_data.sort_values(by = "actual_precipitation")
date = find["date"][0]
print(date)

print("(B)\n")
average = weather_data.loc[0:30,"actual_max_temp"].mean()
print(average)

print("(C)\n")
findHot= weather_data.loc[weather_data['actual_max_temp'] == weather_data['record_max_temp'],'date']
print(findHot)

print("(D)\n")
precipitation = weather_data.loc[92:122, "actual_precipitation"].sum()
print(precipitation)

print("(E)\n")
same = weather_data.loc[(weather_data['actual_max_temp'] > 90) & (weather_data['actual_min_temp'] < 60),'date']
print(same)
