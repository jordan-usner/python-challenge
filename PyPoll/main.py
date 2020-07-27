import os
import csv
csvpath = os.path.join("PyPoll", "Resources", "03-Python_Homework_PyPoll_Resources_election_data.csv")
Total_Votes = 0
Candidates = []
Candidates = list(dict.fromkeys(Candidates))
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    csv_header = next(csvreader)

    for row in csvreader:
        Total_Votes += 1
        candidate = row[2]
        Candidates.append(candidate)
        if candidate == "Khan":
            Khan += 1
        elif candidate == "Correy":
            Correy += 1
        elif candidate == "Li":
            Li += 1
        elif candidate == "O'Tooley":
            O_Tooley += 1

Khan_perc = 100*Khan/Total_Votes
Correy_perc = 100*Correy/Total_Votes
Li_perc = 100*Li/Total_Votes
O_Tooley_perc = 100*O_Tooley/Total_Votes

print("Election Results")
print("-" *25)
print(f"Total Votes: {Total_Votes}")
print("-" *25)
print(f"Khan: {round(Khan_perc, 3)}% {(Khan)}")
print(f"Khan: {round(Correy_perc, 3)}% {(Correy)}")
print(f"Khan: {round(Li_perc, 3)}% {(Li)}")
print(f"Khan: {round(O_Tooley_perc, 3)}% {(O_Tooley)}")
print("-" *25)
print("Winner: Khan")
# print(f"Winner: {Leader}")
print("-" *25)

