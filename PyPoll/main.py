import csv

# csvpath
csvpath = r"C:\Users\RyanF\Downloads\Starter_Code (2)\Starter_Code\PyPoll\Resources\election_data.csv"

#Variables 

#Total votes and candidate dictionary
total_votes = 0
candidate_votes={}

#winner and winner's votes
winner=""
winner_votes= 0

#open/read csv file and skips header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip Header
    next(csvreader)

    #loop for total votes, candidate names, and candidate votes
    for row in csvreader:
        #total votes
        total_votes += 1
        #candidate names
        candidate_names = row[2]
        if candidate_names not in candidate_votes:
            candidate_votes[candidate_names]= 0
        #canditate votes
        candidate_votes[candidate_names]+= 1
    
#Print
print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
#loop to print candidate name, percentages, and total votes 
for candidate_names, votes in candidate_votes.items():
        percentage = (votes/total_votes)*100
        print(f"{candidate_names}: {percentage:.3f}% ({votes})")
        if votes>winner_votes:
            winner = candidate_names
            winner_votes = votes
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")
