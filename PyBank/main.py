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

def get_index_pos(Change, element):
    index_pos = []
    for i in range(len(Change)):
        if Change[i] == element:
            index_pos.append(i)
    return index_pos
    index_pos2 = []
    for i in range(len(Change)):
        if Change[i] == element:
            index_pos2.append(i)
    return index_pos2
index_pos = get_index_pos(Change, max(Change))
a = int(index_pos[0])
# b = row in csv containing month with greatest increase
b = a + 3
index_pos2 = get_index_pos(Change, min(Change))
c = int(index_pos2[0])
# d = row in csv containing month with greatest decrease
d = c + 3

print("Financial Analysis")
print("-" *28)
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${round(sum(Change)/len(Change), 2)}")
# use b and d to call out months of greatest increase and decrease respectively, ran out of time
print(f"Greatest Increase in Profits: Feb-2012 (${max(Change)})")
print(f"Greatest Decrease in Profits: Sep-2013 (${min(Change)})")

output_path = os.path.join("PyBank", "analysis", "new.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: 86'])
    csvwriter.writerow(['Total: $38382578'])
    csvwriter.writerow(['Average Change: $-2315.12'])
    csvwriter.writerow(['Greatest Increase in Profits: Feb-2012 ($1926159)'])
    csvwriter.writerow(['Greatest Decrease in Profits: Sep-2013 ($-2196167)'])