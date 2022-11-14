#import modules
import csv
import os

#set path for file
#print(os.path)
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Resources','election_data.csv')
#set the output of the text file
text_path= os.path.join(os.path.dirname(os.path.abspath(__file__)),'Analysis','Output.txt')

# Declaring the Variables 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""

# Open the File
with open(csvpath,'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop to get total count
    for row in csvreader:
        total_votes += 1
        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] = candidate_votes[candidate] + 1

#this loop when it end we should ideally have unique list and corresponding votes

#another with statement to create output
#we are also finding winning candidate
with open(text_path,'w') as file:
    #create header
    election_header = (f"Election Results\n"
        f"-----------------------\n")
    file.write(election_header)
    file.write(f"Total Votes: {total_votes} \n"
        f"-----------------------\n")
    
    #write candidate summary
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        #print(voter_output)
        file.write(voter_output)

    #write winner
    file.write(f"-----------------------\n")    
    winning_summary = (
        f"Winner: {winner}"
    )
    #print(winning_summary)
    file.write(f"{winning_summary} \n")
    file.write(f"-----------------------") 