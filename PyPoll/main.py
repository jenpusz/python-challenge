import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]

# total all votes
    for row in csvreader:
        total_votes += 1

# total Khan votes
        if row[2] == candidates[0]:
            khan_votes += 1
        #total Correy votes
        elif row[2] == candidates[1]:
            correy_votes += 1
        # total Li votes
        elif row[2] == candidates[2]:
            li_votes += 1
        # total O'Tooley votes
        elif row[2] == candidates[3]:
            otooley_votes += 1

# list of all total votes
    candidate_votes = [khan_votes, correy_votes, li_votes, otooley_votes]
    
# find the winner of the election
    winner = candidate_votes.index(max(candidate_votes))
    winner = candidates[winner]

# calculate percentages
    khan_percentage = khan_votes / total_votes
    correy_percentage = correy_votes / total_votes
    li_percentage = li_votes / total_votes
    otooley_percentage = otooley_votes / total_votes

candidate_percentages = ["{:.3%}".format(khan_percentage), "{:.3%}".format(correy_percentage), 
"{:.3%}".format(li_percentage), "{:.3%}".format(otooley_percentage)]

print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------")
print(f"Khan: {candidate_percentages[0]} ({candidate_votes[0]})")
print(f"Correy: {candidate_percentages[1]} ({candidate_votes[1]})")
print(f"Li: {candidate_percentages[2]} ({candidate_votes[2]})")
print(f"O'Tooley: {candidate_percentages[3]} ({candidate_votes[3]})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

output_path = os.path.join("Analysis", "analysis.txt")

with open(output_path, 'w') as t:
    t.write("Election Results")
    t.write('\n')
    t.write("------------------------------")
    t.write('\n')
    t.write(f"Total Votes: {total_votes}")
    t.write('\n')
    t.write("------------------------------")
    t.write('\n')
    t.write(f"Khan: {candidate_percentages[0]} ({khan_votes})")
    t.write('\n')
    t.write(f"Correy: {candidate_percentages[1]} ({correy_votes})")
    t.write('\n')
    t.write(f"Li: {candidate_percentages[2]} ({li_votes})")
    t.write('\n')
    t.write(f"O'Tooley: {candidate_percentages[3]} ({otooley_votes})")
    t.write('\n')
    t.write("------------------------------")
    t.write('\n')
    t.write(f"Winner: {winner}")
    t.write('\n')
    t.write("------------------------------")
    t.write('\n')