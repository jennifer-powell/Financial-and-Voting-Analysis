import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    month_count= 0

    for row in csvreader:
    #    print(row)

# *The total number of months included in the dataset
    # for row in csvreader:
    
        month_count +=1
    print(f"Total Months:  {month_count}")
 
    # extracting each data row one by one 
#     for row in csvreader: 
#         rows.append(row) 
  
#     # get total number of rows 
#     # print("Total no. of rows: %d"%(csvreader.line_num)) 


# # *The net total amount of "Profit/Losses" over the entire period
#         for i in range(len(profit_loss)+1):
#         total.append(profit_loss[i+1]+profit_loss[i])


# *The average of the changes in "Profit/Losses" over the entire period
#average_change.append(profit_loss[i+1] - profit_loss[i])
# for i in range(len(profit_loss)-1):
#         change.append(profit_loss[i+1]-profit_loss[i])




# *The greatest increase in profits (date and amount) over the entire period


# *The greatest decrease in losses (date and amount) over the entire period
