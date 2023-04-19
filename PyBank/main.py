import csv

# csvpath
csvpath = r"C:\Users\RyanF\Downloads\Starter_Code (2)\Starter_Code\PyBank\Resources\budget_data.csv"

# Variables

# Total number of months and dates list 
total_months = 0
dates = []
# Net total amount of Profit/Losses and profit changes list
total_profit = 0
previous_profit = 0
profit_changes = []

#open/read csv file and skips header row 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop for total months, total profit, and profit changes
    for row in csvreader:
        # Total months
        total_months += 1
        # Total profit
        total_profit += int(row[1])
        # Profit change
        profit_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        # Append profit change and date to their respective lists
        profit_changes.append(profit_change)
        dates.append(row[0])

# Exclude the first element from profit_changes as it doesn't represent a change
profit_changes = profit_changes[1:]

# Calculate average change in profit/losses
average_change = sum(profit_changes) / len(profit_changes)

# Calculate greatest increase in profit
greatest_increase = max(profit_changes)
greatest_increase_date = dates[profit_changes.index(greatest_increase)]

# Calculate greatest decrease in profit
greatest_decrease = min(profit_changes)
greatest_decrease_date = dates[profit_changes.index(greatest_decrease)]

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
with open("financial_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit}\n")
    textfile.write(f"Average Change: ${round(average_change, 2)}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
