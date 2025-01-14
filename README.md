# Python-Challenge
module 3

# Used the concepts I have learned from class to complete two projects: PyBank and PyPoll
both tasks present real-world situations

# PyBank
tasked with creating a Python script to analyze the financial records of company 
given a financial dataset called budget_data.csv
the dataset is composed of two columns: "Date" and "Profit/Losses"

had to create a Python script that analyzes the records to calculate each of the following values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

# PyPoll
tasked with helping a small, rural town modernize its vote-counting process.
given a set of poll data called election_data.csv
the dataset is composed of three columns: "Voter ID", "County", and "Candidate"

had to create a Python script that analyzes the votes and calculates each of the following values:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

# References
used Python3_reference_cheat_sheet.pdf for guidance 

additionally, used Google Generative AI for help formatting a string calculation to display only two decimal places
what it gave me as an example:

num1 = 10.12345
num2 = 5.6789

result = num1 / num2

formatted_result = f"{result:.2f}"

print(formatted_result)
Execution output:

1.78
Explanation:

f-string: The f"{result:.2f}" syntax uses an f-string to format the result variable.
.2f: This format specifier tells Python to display the number as a floating-point number with two decimal places.
