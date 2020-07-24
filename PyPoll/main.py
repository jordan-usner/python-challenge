import os
import csv
csvpath = os.path.join("PyPoll", "Resources", "03-Python_Homework_PyPoll_Resources_election_data.csv")
Total_Votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    csv_header = next(csvreader)

    for row in csvreader: 
        Total_Votes += 1

print("Election Results")
print("-" *25)
print(f"Total Votes: {Total_Votes}")
print("-" *25)
# print(Leader: % (#))
# print(2nd: % (#))
# print(3rd: % (#))
# print(4th: % (#))
print("-" *25)
print("Winner: ")
# print(f"Winner: {Leader}")
print("-" *25)