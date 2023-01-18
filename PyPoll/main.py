import os
import csv

#create path to pull in data from csv file
election_csv = os.path.join('Resources', 'election_data.csv')

#set variables for lists and calculations
TotalBallots = []
Candidate_List = {}
Candidates = ""
BallotTotal = 0
WinningVotes = 0

#open files & ignore header row
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    for row in csvreader:
#get total votes
        TotalBallots.append(row[0])
        TotalVoteCount = len(TotalBallots)
        Candidates = row[2]
        if Candidates in Candidate_List:
            Candidate_List[Candidates] += 1
        else:
            Candidate_List[Candidates] = 1
            
        for Candidates in Candidate_List:

#Calculating percentage of candidates vote
            Percentage = (Candidate_List[Candidates]/TotalVoteCount)*100
            PercentageFormatted = "{:.3f}".format(Percentage)
#Find Winner
            if Candidate_List[Candidates] > WinningVotes:
                WinningVotes = Candidate_List[Candidates]
                Winner = Candidates
            
print(f'Election Results')
print('----------------------')
print(f'Total Votes: {TotalVoteCount}')
print('----------------------')
print(f'{Candidates}: {PercentageFormatted}% ({Candidate_List[Candidates]})')
print('----------------------')
print(f'Winner: {Winner}')
print('----------------------')

#output to txt file
output = open("Analysis/ElectionAnalysis.txt", 'w')
output.write(f'''
Election Results
----------------------
Total Votes: {TotalVoteCount}
----------------------
{Candidates}: {PercentageFormatted}% ({Candidate_List[Candidates]})
----------------------
Winner: {Winner}''')

output.close()
