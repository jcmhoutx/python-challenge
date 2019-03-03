import os
import csv
import sys

# Path to collect data from the Resources folder
votingCSV = os.path.join('..', 'Resources', 'election_data.csv')

# Create lists to hold candidate names and vote totals
candidate_names = []
candidate_votes = []

# Initialize variables to track votes and candidates
most_votes = 0
total_votes = 0
current_index = 0
current_votes = 0
current_candidate = ""
winning_candidate = ""

# Read in the CSV file
with open(votingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        current_candidate = row[2]

        # Determine if candidate is in list and add name and/or vote to totals at same index
        if current_candidate in candidate_names:
            current_index = candidate_names.index(current_candidate)
            candidate_votes[current_index] = str((int(candidate_votes[current_index])) + 1)
        else:
            candidate_names.append(row[2])
            candidate_votes.append("1")

# Loop through results to determine winning candidate and total vote count
for results in candidate_votes:
    current_votes = int(results)
    current_index = candidate_votes.index(results)
    total_votes = total_votes + current_votes
    if current_votes > most_votes:
        most_votes = current_votes
        winning_candidate = candidate_names[current_index]

# Function to print results to screen and file
def print_results():
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes:  {total_votes}")
    print("-----------------------------")
    for candidate in candidate_names:
        current_index = candidate_names.index(candidate)
        print(f"{candidate_names[current_index]}:  {round(int(candidate_votes[current_index]) / total_votes * 100, 3)}%  ({int(candidate_votes[current_index])})")
    print("-----------------------------")
    print(f"Winner:  {winning_candidate}")
    print("-----------------------------")

# Print results to the screen
print_results()

# Print results to a text file
sys.stdout = open("PyPollOutput.txt", "w")
print_results()
sys.stdout.close()
