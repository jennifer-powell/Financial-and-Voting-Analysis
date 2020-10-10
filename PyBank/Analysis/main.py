import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    month_count= 0
    profit_loss= [1]
    total_profit_loss= 0.0
    for row in csvreader:
    #    print(row)

# *The total number of months included in the dataset
            month_count +=1
    print(f"Total Months:  {month_count}")
 
    
# # *The net total amount of "Profit/Losses" over the entire period
profit_loss= float(row[1])
total_profit_loss+= profit_loss
    
        
print(f"Total: ${profit_loss}")
## *The average of the changes in "Profit/Losses" over the entire period
#average_change.append(profit_loss[i+1] - profit_loss[i])
# for i in range(len(profit_loss)-1):
#         change.append(profit_loss[i+1]-profit_loss[i])




# *The greatest increase in profits (date and amount) over the entire period


# *The greatest decrease in losses (date and amount) over the entire period
