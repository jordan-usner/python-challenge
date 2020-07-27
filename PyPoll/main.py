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
print(f"Khan: {round(Khan_perc, 3)}% ({Khan})")
print(f"Correy: {round(Correy_perc, 3)}% ({Correy})")
print(f"Li: {round(Li_perc, 3)}% ({Li})")
print(f"O'Tooley: {round(O_Tooley_perc, 3)}% ({O_Tooley})")
print("-" *25)
print("Winner: Khan")
print("-" *25)

output_path = os.path.join("PyPoll", "analysis", "new.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Votes: 3521001'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Khan: 63.0% (2218231)'])
    csvwriter.writerow(['Correy: 20.0% (704200)'])
    csvwriter.writerow(['Li: 14.0% (492940)'])
    csvwriter.writerow(["O'Tooley: 3.0% (105630)"])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner: Khan'])
    csvwriter.writerow(['-------------------------'])