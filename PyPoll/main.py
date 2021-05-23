import os
import csv

# Setting path for input csv file and output txt file
election_csv = os.path.join(".", "Resources", "election_data.csv")
analysis_txt = os.path.join(".", "Analysis", "analysis.txt")

# Opening csv file
with open(election_csv, encoding='utf-8-sig') as csvfile:

    # reading with csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading csv header
    csv_header = next(csvreader)

    # Initialising variables required
    vote_count = 0
    cand_list = {}

    # Read each row of data after the header
    for row in csvreader:

        # Finding total votes
        vote_count += 1    

        # Finding candidates
        if row[2] not in cand_list:
            cand_list[row[2]] = 1
        else:
            cand_list[row[2]] += 1

# Writing to console
print("\nElection Results")
print("--------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------")

# Opening analysis file in write mode
with open(analysis_txt, "w") as txtfile:
    winner = ""
    max_vote = 0

    # Writing to analysis file
    txtfile.write("\nElection Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write("--------------------------\n")

    # Finding percentage of vote and winner
    for key, value in cand_list.items():
        percent_vote = (value / vote_count) * 100
        print(f"{key}: ${percent_vote:.3f}% ({value})")
        txtfile.write(f"{key}: ${percent_vote:.3f}% ({value})\n")
        if max_vote < value:
            max_vote = value
            winner = key

    # Writing to analysis file
    txtfile.write("--------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("--------------------------\n")

# Writing to console
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
