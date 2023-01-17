import os as os
import csv

#Initialize Variables

months = 0 
net_ProfitLoss = 0
ProfitLossarray = []
dates = []


#import CSV

    #Pointing to File 
file = "/Users/bennettnorthcutt/Module 3/python-challenge/PyBank/Resources/budget_data.csv"

with open(file) as file:
    
    
    csv_read=csv.reader(file,delimiter=",")
    
    next(file)
    
    for row in csv_read:
        
        #  Calculate Total Number of Months in the Dataset

        months += 1
        net_ProfitLoss += int(row[1])
        ProfitLossarray.append(int(row[1]))
        dates.append(row[0])


    # Calculate the Net Total of P and L over the entire period
    
    net_profitLoss = sum(ProfitLossarray)
    
   

    #Calculate Changes in Profit/Losses over the entire period and the average 
    
    change_list = [ProfitLossarray[i+1] - ProfitLossarray[i] for i in range(months-1)]
    
    average_change = sum(change_list) / (months-1)
    
    average_change = round(average_change,2)

    #Calculate Greatest increase in profits (date and amount)
    
    max = max(change_list)

    #Calculate Decrease increase in profits (date and amount)

    min = min(change_list)
    
    # Record Max and Min Profit dates in their lists
    
    max_profit_date = dates[change_list.index(max) + 1]
    min_profit_date = dates[change_list.index(min) + 1]

# Output Statements
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_profitLoss}")
print(f"Average Change:  ${average_change} ")
print(f"Greatest Increase in Profits:  {max_profit_date} (${max})")
print(f"Greatest Decrease in Profits: {min_profit_date} (${min})")

#Output to Text File and save in Analysis

with open("financial_analysis_module3.txt", "w") as text_file:
    text_file.write("Financial Analysis - Module 3 \n")
    text_file.write("------------------- \n")
    text_file.write(f"Total Months: {months} \n")
    text_file.write(f"Total: ${net_profitLoss}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {max_profit_date} (${max})\n")
    text_file.write(f"Greatest Decrease in Profits: {min_profit_date} (${min})")
    