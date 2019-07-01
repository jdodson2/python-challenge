import csv
import os

rowcnt = 1
maxchg = 0
minchg = 0
NumOfMonths = 0
Tot_ProfitLoss = 0
tot_delta = 0

# Store filepath in a variable
csvpath = "Resources/election_data.csv"

# Open CSV file
with open(csvpath, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)

# Prepare a list to store election data rows
    election_data = list(csvreader)

# Count the number of months in this csv file
    tot_Votes = len(election_data)

# Sort the election data list by Candidate
    election_data.sort(key=lambda row: (row[2]))
     

# Tally the number of votes each candidate recieved and store in a new list 
#--------------------------------------------------------------------------------------
# first initialize the new list 
election_tally=[] 
    
# cycle through the sorted election data and tally up number of votes per candidate
hld_candidate = ""
vote_cnt = 0
index = 0
for index, row in enumerate(election_data):
    if index == 0: 
        hld_candidate = str(row[2])
        vote_cnt += 1
        index += 1
    elif hld_candidate == str(row[2]):    # Check for candidate name change if the same count the vote   
        vote_cnt += 1
        index += 1
    else:
# On candidate name change append the candidate name, percent of votes and vote count
# to election tally list
# First calculate percent of votes received
        pct_votes = float(round((vote_cnt / tot_Votes) * 100, 3))
# Next append candidate data election tally list
        election_tally.append([hld_candidate, pct_votes, vote_cnt])    
# Now perform housekeeping to prepare tally for next candidate's votes
        hld_candidate = str(row[2])
        vote_cnt = 1
        index += 1

# Calculate percentage of votes for the last candidate 
pct_votes = float(round((vote_cnt / tot_Votes) * 100, 3))
# Append the election_tally list with the last candidate 
election_tally.append([hld_candidate, pct_votes, vote_cnt])    

# Sort the election tally list by number of votes received 
election_tally.sort(key=lambda row: (-row[2]))

#Report Election Results
hld_count = 0
print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_Votes}")
print("-------------------------")
for i, row in enumerate(election_tally): 
    print(f"{row[0]}: {row[1]}% ({row[2]})")
    if hld_count < row[2]:
        winner = str(row[0])
        hld_count = row[2]
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


f = open('main_Results.txt', 'w')
f.write("%s\n" % "Election Results")
f.write("%s\n" % "-------------------------")
Total_Votes = "Total Votes: " + str(tot_Votes) + "\n"
f.write(Total_Votes)
f.write("%s\n" % "-------------------------")
for i, row in enumerate(election_tally):
    candidate_line = str(row[0]) + ": " + str(float(round(row[1], 3))) + "% (" + str(row[2]) + ") \n"
    f.write(candidate_line)
f.write("%s\n" % "-------------------------")
winner_line = "Winner: " + winner + "\n"
f.write(winner_line)
f.write("%s\n" % "-------------------------")


f.close()


        
        


        

        
        
        
        
        
        
