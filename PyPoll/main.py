import os
import csv

election_csv = os.path.join(".", "Resources", "election_data.csv")
analysis_txt = os.path.join(".", "Analysis", "analysis.txt")

with open(election_csv, encoding='utf-8-sig') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    vote_count = 0
    cand_list = {}

    # Read each row of data after the header
    for row in csvreader:
        vote_count += 1    
        if row[2] not in cand_list:
            cand_list[row[2]] = 1
        else:
            cand_list[row[2]] += 1

print("\nElection Results")
print("--------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------")

with open(analysis_txt, "w") as txtfile:
    winner = ""
    max_vote = 0
    txtfile.write("\nElection Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write("--------------------------\n")
    for key, value in cand_list.items():
        percent_vote = (value / vote_count) * 100
        print(f"{key}: ${percent_vote:.3f}% ({value})")
        txtfile.write(f"{key}: ${percent_vote:.3f}% ({value})\n")
        if max_vote < value:
            max_vote = value
            winner = key

    txtfile.write("--------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("--------------------------\n")

print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
