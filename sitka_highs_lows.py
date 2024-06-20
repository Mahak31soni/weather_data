from pathlib import Path
import csv
from datetime import datetime
from matplotlib import pyplot as plt


path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index , header_column in enumerate(header_row):
    print(index, header_column)

dates,highs, lows = [],[],[]
for row in reader:
    high = int(row[4])
    low = int(row[5])
    date = datetime.strptime(row[2],'%Y-%m-%d')
    highs.append(high)
    dates.append(date)
    lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)

ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title("Daily High Temperature and Low Tempearture, 2021", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()
