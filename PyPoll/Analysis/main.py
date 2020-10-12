import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    vote_count= 0
    candidate_list = []
    Number_votes= []
    for row in csvreader:
        #print(row)

# * The total number of votes cast
    
            vote_count +=1
    # print(f"Total Votes:  {vote_count}")

# * A complete list of candidates who received votes
    
    # candidate_list = []
    # for row in csvreader:

            candidate = row[2]
            candidate_list.append(candidate)

            #print(str(candidate_list))
            if candidate in Number_votes:
                Number_votes[candidate]= Number_votes[candidate] +1
            else:
                Number_votes[candidate]=1

            print(Number_votes[candidate])




# * The total number of votes each candidate won
    #total number of times a canidate was mentioned
# * The percentage of votes each candidate won
    #number of votes for each canidate/ "votecount"



# * The winner of the election based on popular vote.
    #

 #print(candidate:, candidate %, (candidate's total vote count))