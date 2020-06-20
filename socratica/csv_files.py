# Socratica tutorial
# CSV files in python

import csv
from datetime import datetime

path = "c:/Users/David/Documents/Scripts/Python/socratica/google_stock_data.csv"
# file = open(path)
# for line in file:
#    print(line)

# lines = [line for line in open(path)]

#print(lines[0].strip().split(','))
#print(lines[1].strip().split(','))

#dataset = [line.strip().split(',') for line in open(path)]

#print(dataset[0])
#print(dataset[5])

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
#data = [row for row in reader]
data = []
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj, Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

# print(header)
# print(data[0])
# Compute and store daily stock returns
returns_path = "c:/Users/David/Documents/Scripts/Python/socratica/google_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[1]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
