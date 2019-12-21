#  Analyze the financial records of your company. 
#  Input file - financial data -  budget_data.csv. (The dataset is composed of two columns: Date and Profit/Losses)
#    Calculates each of the following:
#     (1) total number of months included in the dataset - number of recs in file,
#     (2) net total amount of "Profit/Losses" over the entire period - summation of values in p/l
#  	  (3) average of the changes in "Profit/Losses" over the entire period
#	  (4) greatest increase in profits (date and amount) over the entire period
# 	  (5) greatest decrease in losses (date and amount) over the entire period
#
#    Analysis will look similar to the one below:
#
#       Financial Analysis
#       ----------------------------
#       Total Months: 86
#       Total: $38382578
#       Average  Change: $-2315.12
#       Greatest Increase in Profits: Feb-2012 ($1926159)
#       Greatest Decrease in Profits: Sep-2013 ($-2196167)
#
#    Print the analysis above to the terminal and export a text file with the results.

import os
import csv

#  User defined functions

def procavgchg(reccount, prev_profit_loss_amt, profit_loss_amt, amt_chg):

#  Set or increase/decrease amount of change using profit loss information and return updated amount of change.

    if reccount == 1:
        amt_chg = profit_loss_amt - profit_loss_amt
    else:
        amt_chg += prev_profit_loss_amt - profit_loss_amt 

    return(amt_chg)
 
def writetotextfile(txtfile, reccount, total_profit_loss, fin_amt_chg, high_date, high_profit, low_date, low_profit):

#  Write financial analysis information/report to terminal and output file.

    finrpt = "Financial Analysis"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')


    finrpt = "----------------------------"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')

    finrpt =  f"Total Months: {reccount}"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')
    
    finrpt =  f"Total: ${total_profit_loss}"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')

    finrpt =  f"Average  Change: ${fin_amt_chg:.2f}"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')
    
    finrpt =  f"Greatest Increase in Profits: {high_date} (${high_profit})"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')
    
    finrpt =  f"Greatest Decrease in Profits: {low_date} (${low_profit})"
    print(finrpt)
    txtfile.write(str(finrpt) + '\n')



# Path to collect data from the Resources folder.
#  Open input/output files and extract header prior to processing (not needed).

csvpath = os.path.join('C:\\Users\\sbell\\python-challenge\\PyBank\\Resources\\budget_data.csv')
txtpath = os.path.join('C:\\Users\\sbell\\python-challenge\\PyBank\\Resources\\Financial_Analysis_Rpt.txt')
txtfile =  open(txtpath, "w", encoding="utf-8") 
    
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print('\n\n')
 
#  Summary counters, work fields/variables defined and initialized.

    reccount = 0
    amt_chg = 0
    total_profit_loss = 0
    budget_info = []
    prev_profit_loss_amt = 0

# File layout - {budget_date, profit_loss_amt}.

    for line in csvreader:

        budget_info = line
        
#  Increment line count and move budget data to their respective variables

        reccount += 1
        budget_date = str(budget_info[0])
        profit_loss_amt = int(budget_info[1])
        
#  Add profit/loss amt from this row to the total profit loss amt accumlator variable,
#   call function to process information for average change amount, and determine if entry
#   may be either the highest entry for profit/loss or the lowest entry for profit/loss.

        total_profit_loss += profit_loss_amt
        
        amt_chg = procavgchg(reccount, prev_profit_loss_amt, profit_loss_amt, amt_chg)
        prev_profit_loss_amt = profit_loss_amt 

        if reccount == 1:
            high_profit = profit_loss_amt
            high_date = budget_date
            low_profit = profit_loss_amt
            low_date = budget_date

        elif profit_loss_amt > high_profit:
            high_profit = profit_loss_amt
            high_date = budget_date

        elif profit_loss_amt < low_profit:
            low_profit = profit_loss_amt
            low_date = budget_date


#  After processing entire file generate information/values required for Financial Analysis Report, displaying the report
#   on the terminal and storing on newly generated text file.

    fin_amt_chg = amt_chg / (reccount + 1)

#  Print financial analysis report to the terminal
    writetotextfile(txtfile, reccount, total_profit_loss, fin_amt_chg, high_date, high_profit, low_date, low_profit)  

    print("\n \n" + "Task ending....")
    