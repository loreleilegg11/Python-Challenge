# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File.
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns:
 "Voter ID", "County", and "Candidate". 
 Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote"""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..","analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidateVotes = {}
winner_count = 0
Candidate_winner = 0
# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
   
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
       # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
         # If the candidate is not already in the candidate list, add them
        if row[2] not in candidates:
            candidates.append(row[2])
           
          # Add a vote to the candidate's count
            candidateVotes[row[2]] = 1

        else: 
            candidateVotes[row[2]]+= 1

vote_output = ""
# candidate vote percentages 
for candidates in candidateVotes:
    votes = candidateVotes.get(candidates)
    VotePercent = (float(votes) / float(total_votes))* 100.00
    vote_output += f"{candidates}: {VotePercent:.3f}% ({float(votes):.0f})\n"
 # get winner    
    if votes > winner_count:
     winner_count = votes
     Candidate_winner = candidates
     Candidate_winnerOutput = f"Winner: {Candidate_winner}"

output = (
    f"\nElection Results\n"
    f"---------------------------\n"
    f"Total Votes: = {total_votes:,}\n"
    f"---------------------------\n"
    f"{vote_output}\n"
    f"---------------------------\n"
    f"{Candidate_winnerOutput}\n"       
    f"---------------------------" )

print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

    
