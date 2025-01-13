import os
import csv

# File paths relative to the script's directory
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")

# Debugging: Print the resolved file paths
print(f"Loading data from: {file_to_load}")
print(f"Saving results to: {file_to_output}")

# Initialize variables to track election data
total_votes = 0
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open and process the CSV file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip the header

    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Save the results to a text file
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        f"-------------------------\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)

print(f"Election analysis complete. Results saved to {file_to_output}")

