
# Import the csv
import os
import csv

#Path for csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Create variables and lists
    total_months = []
    nettotal_pl = []
    netchange_pl = []
    avg_change_pl = 0
    max_increase = 0
    max_decrease = 0
    time_periods = []
    change = []
 

#The total number of months included in the dataset
    for row in csvreader:
        total_months.append(row[0]) 

    #The net total amount of "Profit/Losses" over the entire period
        nettotal_pl.append(row[1])


#Calculate the changes in "Profit/Losses" over the entire period 

nettotal_pl = list(map(int, nettotal_pl))

for i in range(len(nettotal_pl)-1):
        
        monthly_change = change.append(nettotal_pl[i+1]-nettotal_pl[i])
        

#The average of those changes

average_change = sum(change)/len(change)
average_change = round(average_change, 2)

#The greatest increase in profits (date and amount) over the entire period

max_increase = max(change)
max_increase_month = change.index(max_increase) +1
max_increase_month = total_months[max_increase_month]

#The greatest decrease in profits (date and amount) over the entire period
max_decrease = min(change)   
max_decrease_month = change.index(max_decrease) +1
max_decrease_month = total_months[max_decrease_month]


#Create Table
print("Financial Analysis")
print("-------------------------------")
print(f'Total Months: {len(total_months)}')
print(f"Total: ${sum(nettotal_pl)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")


output_path = os.path.join("Analysis", "analysis.txt")

lines = ["Financial Analysis", "-------------------------------", f"Total Months: {len(total_months)}",
f"Total: ${sum(nettotal_pl)}",f"Average Change: ${average_change}",
f"Greatest Increase in Profits: {max_increase_month} (${max_increase})", f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"]

with open(output_path, 'w') as txtfile:
    for line in lines:
        txtfile.write(line)
        txtfile.write('\n')




