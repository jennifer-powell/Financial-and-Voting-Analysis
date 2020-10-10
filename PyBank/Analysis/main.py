import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

# *The total number of months included in the dataset
    for row in csvreader:


# *The net total amount of "Profit/Losses" over the entire period


# *The average of the changes in "Profit/Losses" over the entire period
average_change.append(profit_loss[i+1] - profit_loss[i])

# *The greatest increase in profits (date and amount) over the entire period


# *The greatest decrease in losses (date and amount) over the entire period
