import os
import csv

# Setting path for input csv file and output txt file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")
analysis_txt = os.path.join(".", "Analysis", "analysis.txt")

# Opening csv file
with open(budget_csv, encoding='utf-8-sig') as csvfile:

    # reading with csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading csv header
    csv_header = next(csvreader)

    # Initialising variables required
    months = 0
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
            # Creating the list of change in profit
            change_profit.append(int(row[1]) - profit)

            # Finding minimum and maximum profit and corresponding date
            if(min_change == 0 and max_change == 0):
                min_change = change_profit[months-1]
                max_change = change_profit[months-1]
            elif (min_change > change_profit[months-1]):
                min_change = change_profit[months-1]
                min_date = row[0]
            elif (max_change < change_profit[months-1]):
                max_change = change_profit[months-1]
                max_date = row[0]

        profit = int(row[1])

        # Adding profit to find total
        total_profit += int(row[1])
        months += 1 
    
    # Finding average of change in profit
    average = sum(change_profit) / len(change_profit)
    
    # Opening analysis file in write mode
    with open(analysis_txt, "w") as txtfile:
        # Writing to analysis file
        txtfile.write("Financial Analysis\n")
        txtfile.write("------------------\n")
        txtfile.write(f"Total Months: {months}\n")
        txtfile.write(f"Total: ${total_profit}\n")
        txtfile.write(f"Average Change: ${average:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {max_date} (${max_change})\n")
        txtfile.write(f"Greatest Decrease in Profits: {min_date} (${min_change})\n")

    # Writing to console
    print("\nFinancial Analysis")
    print("------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average:.2f}")
    print(f"Greatest Increase in Profits: {max_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_change})")



       