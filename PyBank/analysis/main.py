# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""
"""
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
"""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("..","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net_revenue = 0
net_change_list= []

months= []

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstRow = next(reader)

    # Track the total and net change
    total_months+= 1
    total_net_revenue+= float(firstRow[1])
    
    # prious revenue to track change
    previousRevenue= float(firstRow[1])

    # Process each row of data
    for row in reader:

        # Track the total months and revenue (index 1)
        total_months+= 1
        total_net_revenue+= float(row[1])
        # Track the net change
        netchange =  float(row[1])- previousRevenue
        net_change_list.append(netchange)
        #month where change occured
        months.append(row[0])

        previousRevenue = float(row[1])
        
        

# Calculate the average net change across the months
MonthlyAvgChange= sum(net_change_list)/len(net_change_list)
# Calculate the greatest increase in profits (month and amount)
Greatest_increase = [months[0], net_change_list[0]]

# Calculate the greatest decrease in losses (month and amount)
Greatest_decrease = [months[0], net_change_list[0]]


for m in range(len(net_change_list)):
    if (net_change_list[m]> Greatest_increase[1]):
        Greatest_increase[1] = net_change_list[m]
        Greatest_increase[0]= months[m]
    if (net_change_list[m]< Greatest_decrease[1]):
        Greatest_decrease[1] = net_change_list[m]
        Greatest_decrease[0]= months[m]
# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total months= {total_months}\n"
    f"Total = {total_net_revenue:,.2f}\n"
    f"Average Change: = {MonthlyAvgChange:,.2f}\n"
    f"Greatest Increase in Profits= {Greatest_increase[0]} (${Greatest_increase[1]})\n"
    f"Greatest Decrease in Profits = {Greatest_decrease[0]} (${Greatest_decrease[1]})"

)
# Print the output to terminal and file
print(output)

with open(file_to_output, "w") as txt_file:  
    txt_file.write(output)
