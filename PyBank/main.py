import os
import csv
import sys

# Path to collect data from the Resources folder
budgetCSV = os.path.join('..', 'Resources', 'budget_data.csv')

# Initalize variables for total months, profit/loss, and greatest increase and decrease
months = 0
total_amount = 0
most_profits = 0
most_profits_month = ""
most_losses = 0
most_losses_month = ""

# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Add each month to the total
        months = months + 1

        # Calculate profit or loss for the month
        total_amount = total_amount + float(row[1])
        
        # Determine if profits are highest yet
        if(int(row[1]) > most_profits):
            most_profits_month = row[0]
            most_profits = int(row[1])
        
        # Determine if losses are lowest yet
        if(int(row[1]) < most_losses):
            most_losses_month = row[0]
            most_losses = int(row[1])

def print_results():
    print("Financial Information")
    print("--------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${int(total_amount)}")
    print(f"Average Change: ${int(total_amount / months)}")
    print(f"Greatest Increase in Profits: {most_profits_month} $({int(most_profits)})")
    print(f"Greatest Decrease in Profits: {most_losses_month} $({int(most_losses)})")

# Print results to the screen
print_results()

# Print results to a text file
sys.stdout = open("PyBankOutput.txt", "w")
print_results()
sys.stdout.close()
