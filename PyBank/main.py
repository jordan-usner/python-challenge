import os
import csv
csvpath = os.path.join("PyBank", "Resources", "03-Python_Homework_PyBank_Resources_budget_data.csv")
Total_Months = 0
Total = 0
Change = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    csv_header = next(csvreader)
    first_row = next(csvreader)
    prev_amt = int(first_row[1])
    Total += int(first_row[1])
    Total_Months += 1


    for row in csvreader: 
        Total_Months += 1
        Total += int(row[1])
 
        net_change = int(row[1]) - prev_amt
        prev_amt = int(row[1]) 
        Change.append(net_change)
        
print("Financial Analysis")
print("-" *28)
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${sum(Change)/len(Change)}")
print(f"Greatest Increase in Profits: (${max(Change)})")
print(f"Greatest Decrease in Profits: (${min(Change)})")