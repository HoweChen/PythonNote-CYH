import csv


file_name = './CSVHandling/sitka_weather_07-2014.csv'
with open(file_name) as fopen:
    reader = csv.reader(fopen)
    header_row = next(reader)
    print(header_row)
