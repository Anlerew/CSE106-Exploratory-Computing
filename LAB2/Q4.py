import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv("weather_data.txt")
min = weather_data["actual_min_temp"]
max = weather_data["actual_max_temp"]

plt.plot(min, color = "blue", label='actual min temp')
plt.plot(max, color = "red", label='actual max temp')
plt.xlabel("days")
plt.ylabel("temp")
plt.title("day vs temp")
plt.legend()
plt.show()

histogram = weather_data["actual_precipitation"].plot(kind = 'hist')
plt.xlabel("precip amount")
plt.ylabel("days")
plt.title("actual precip")
plt.show()