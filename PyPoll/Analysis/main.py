import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    vote_count= 0
    for row in csvreader:
        #print(row)

# * The total number of votes cast
    
            vote_count +=1
    print(f"Total Votes:  {vote_count}")
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:
