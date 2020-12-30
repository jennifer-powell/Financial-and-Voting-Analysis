import os

import csv

csvpath = "C:\\Users\\jenzy\\Desktop\\Python--Challenge\\PyBank\\Resources\\budget_data.csv"

month_count= 0
month_changepls= []
month_of_change =[]
total_profit_loss= 0
greatest_inc_profits=['', 0]
greatest_dec_profits= ['', 9999999999999999999]

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    first_row= next(csvreader)
    last_monthpl= int(first_row[1])
   
    month_changepl= 0
    month_count +=1
    total_profit_loss += int(first_row[1])
    
    
    for row in csvreader:

        #print(row)

# *The total number of months included in the dataset
        month_count +=1
    
# # *The net total amount of "Profit/Losses" over the entire period, 

        total_profit_loss += int(row[1])
           
# #The average of the changes in "Profit/Losses" over the entire period
    # finding the month to month changes then averaging them

        month_changepl=int(row[1]) - last_monthpl
        last_monthpl = int(row[1])
        month_changepls += [month_changepl]
        month_of_change += [row[0]]
        

  
        sum_changes= sum(month_changepls)
        average_change= (sum_changes/len(month_changepls))
    

# *The greatest increase in profits (date and amount) over the entire period

        if month_changepl > greatest_inc_profits[1]:
            greatest_inc_profits[0] = row[0]
            greatest_inc_profits[1] = month_changepl
# *The greatest decrease in losses (date and amount) over the entire period

        if month_changepl < greatest_dec_profits[1]:
            greatest_dec_profits[0] = row[0]
            greatest_dec_profits[1] = month_changepl
    print(f"Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_count}")      
    print(f"Total Profit/Loss: ${total_profit_loss}")
    print(f"Average Change: ${round(average_change, 2)}")  
    print(f"Greatest Increase in Profits: {greatest_inc_profits[0]}, ${greatest_inc_profits[1]}")  
    print(f"Greatest Decrease in Profits: {greatest_dec_profits[0]}, ${greatest_dec_profits[1]}")  

    PyBankFile= open("PyBanktext.txt", "a" )