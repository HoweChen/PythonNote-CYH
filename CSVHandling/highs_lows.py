import csv
from matplotlib import pyplot as plt
from datetime import datetime

# file_name = './CSVHandling/sitka_weather_07-2014.csv'
# file_name = './CSVHandling/sitka_weather_2014.csv'
file_name = './CSVHandling/death_valley_2014.csv'
with open(file_name) as fopen:
    reader = csv.reader(fopen)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    lows = []
    dates = []
    for row in reader:
        try:
            # get the data per row
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError as VE:
            print(current_date, 'miss data')
        finally:
            # append the data to the list
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    print(highs)
    print(dates)

    # draw the figure
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)  # figure with high temperature
    plt.plot(dates, lows, c='blue', alpha=0.5)  # figure with low temperature
    plt.fill_between(dates, highs, lows, facecolor='blue',
                     alpha=0.1)  # fill between two temperatures

    # set up the graph
    # plt.title("Daily high and low temperatures, July 2014", fontsize=24)
    plt.title(
        "Daily high and low temperatures - 2014\nDeath Valley, CA",
        fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
