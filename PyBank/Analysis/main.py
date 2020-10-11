import os

import csv

csvpath = "C:\\Users\\jenzy\\Desktop\\Python--Challenge\\PyBank\\Resources\\budget_data.csv"

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    month_count= 0
    #Check out your line 18
    profit_loss= []
    total_profit_loss= 0.0
    for row in csvreader:

        #print(row)

# *The total number of months included in the dataset
            month_count +=1
    
# # *The net total amount of "Profit/Losses" over the entire period, 

            profit_loss= float(row[1])
            total_profit_loss = total_profit_loss + profit_loss
    print(f"Total Months:{month_count}")      
    print(f"Total: ${profit_loss}")

# #The average of the changes in "Profit/Losses" over the entire period
    
    
    finances= []
    average_change= []
    for i in range(len(finances)):
        average_change.append(finances[i+1]-finances[i])


    print(finances)



# *The greatest increase in profits (date and amount) over the entire period

#greatest_inc_profits
# *The greatest decrease in losses (date and amount) over the entire period
#greatest_dec_losses