import os

import csv

csvpath = "C:\\Users\\jenzy\\Desktop\\Python--Challenge\\PyBank\\Resources\\budget_data.csv"

month_count= 0
month_changepls= []
month_of_change =[]
total_profit_loss= 0
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    
    #current_monthpl= 0
    first_row= next(csvreader)
    last_monthpl= int(first_row[1])
   
    month_changepl= 0
    month_count +=1
    # profit_loss= []
    total_profit_loss += int(first_row[1])
    
    
    for row in csvreader:

        #print(row)

# *The total number of months included in the dataset
        month_count +=1
    
# # *The net total amount of "Profit/Losses" over the entire period, 

        total_profit_loss += int(row[1])
           
   

# #The average of the changes in "Profit/Losses" over the entire period
    # finding the month to month changes then averaging them
   # monthly_change
        month_changepl=int(row[1]) - last_monthpl
        last_monthpl = int(row[1])
        month_changepls += [month_changepl]
        month_of_change += [row[0]]
        # month_changepls.append(month_changepl)

  
    sum_changes= sum(month_changepls)
    average_change= (sum_changes/len(month_changepls))
    


#total_change = total_change + profit_loss
# *The greatest increase in profits (date and amount) over the entire period

#greatest_inc_profits
# *The greatest decrease in losses (date and amount) over the entire period
#greatest_dec_losses



    print(f"Total Months:{month_count}")      
    print(f"Total Profit/Loss: ${total_profit_loss}")
    print(f"Average Change:{average_change}")  
    # print(f"Greatest Increase in Profits:{}")  
    # print(f"Greatest Decrease in Profits:{}")  