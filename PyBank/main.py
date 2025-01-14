# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
before_profit = None
net_change_list = []
dates = []
greatest_inc = {"date": "", "amount": 0}
greatest_dec = {"date": "", "amount": 0}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Extract date and profit/loss
        date = row[0]
        profit = int(row[1])  # Convert profit/loss value to an integer

        # Track the total months and total net
        total_months += 1
        total_net += profit

        # Calculate changes and track the date
        if before_profit is not None:
            net_change = profit - before_profit
            net_change_list.append(net_change)
            dates.append(date)

            # Check for greatest increase and decrease
            if net_change > greatest_inc["amount"]:
                greatest_inc["amount"] = net_change
                greatest_inc["date"] = date

            if net_change < greatest_dec["amount"]:
                greatest_dec["amount"] = net_change
                greatest_dec["date"] = date

        # Update previous profit
        before_profit = profit

# Calculate the average net change
avg_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc['date']} (${greatest_inc['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_dec['date']} (${greatest_dec['amount']})\n"
)

# Print the output to the terminal
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
