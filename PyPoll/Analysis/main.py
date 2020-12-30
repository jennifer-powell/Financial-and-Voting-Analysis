import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

vote_count= 0
candidate_votes =[]
candidates= []
Number_votes= []
vote_percent= 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
   
    for row in csvreader:
        #print(row)

# * The total number of votes cast
    
            vote_count +=1

# * A complete list of candidates who received votes
            candidate_votes.append(row[2])

    for candidate in set(candidate_votes):
        candidates.append(candidate)
        votes= candidate_votes.count(candidate)
        Number_votes.append(votes)
        # percent= (votes/vote_count)*100
        # vote_percent.append(percent)
        percent= (votes/vote_count)*100
    winning= max(Number_votes)
    winner= candidates[Number_votes.index(winning)]
    
    #         if candidate_votes in candidate:
    #             candidate.append(candidate_votes)
    #             set_candidate_votes= set(candidate_votes)
    #             Number_votes= len(set_candidate_votes)
    
    # print(candidate)
            # if candidate in Number_votes:
            #     Number_votes[candidate]= Number_votes[candidate] +1
            # else:
            #     Number_votes[candidate]=1

            # print(Number_votes[candidate])




# * The total number of votes each candidate won
    #total number of times a canidate was mentioned
# * The percentage of votes each candidate won
    #number of votes for each canidate/ "votecount"



# * The winner of the election based on popular vote.
    #

 #print(candidate:, candidate %, (candidate's total vote count))

print(f"Election Results")
print("---------------------")
print(f"Total Votes: {vote_count}") 
print("---------------------")
print(f"{candidates[0]}: {round((Number_votes[0]/vote_count)*100, 3)}% ({Number_votes[0]})")
print(f"{candidates[1]}: {round((Number_votes[1]/vote_count)*100, 3)}% ({Number_votes[1]})")
print(f"{candidates[2]}: {round((Number_votes[2]/vote_count)*100, 3)}% ({Number_votes[2]})")
print(f"{candidates[3]}: {round((Number_votes[3]/vote_count)*100, 3)}% ({Number_votes[3]})")

print("---------------------")
print(f"winner: {winner}")
                 