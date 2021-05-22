import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

with open(budget_csv, encoding='utf-8-sig') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    no_of_months = 0
    total_profit = 0
    change_profit = []
    profit = 0
    max_change = 0
    min_change = 0
    max_date = ''
    min_date = ''

    # Read each row of data after the header
    for row in csvreader:
 
        if(total_profit != 0):
            change_profit.append(int(row[1]) - profit)
            if(min_change == 0 and max_change == 0):
                min_change = change_profit[no_of_months-1]
                max_change = change_profit[no_of_months-1]
            elif (min_change > change_profit[no_of_months-1]):
                min_change = change_profit[no_of_months-1]
                min_date = row[0]
            elif (max_change < change_profit[no_of_months-1]):
                max_change = change_profit[no_of_months-1]
                max_date = row[0]

        profit = int(row[1])

        total_profit += int(row[1])
        no_of_months += 1 
    average = sum(change_profit) / len(change_profit)
    
    print('''Financial Analysis
--------------------''')
    print(f"Total Months: {no_of_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average:.2f}")
    print(f"Greatest Increase in Profits: {max_date} {max_change}")
    print(f"Greatest Decrease in Profits: {min_date} {min_change}")


       