#  Description:  Analyze the votes and calculates each of the following:
#
#   (1) Total number of votes cast
#   (2) A complete list of candidates who received votes
#   (3) The percentage of votes each candidate won
#   (4) The total number of votes each candidate won
#   (5) The winner of the election based on popular vote.
#
# Analysis should look similar to the one below:
#
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#
#   Input file name (Poll data): election_data.csv. 
#   Description: The dataset is composed of three columns: Voter ID, County, and Candidate. 

import os
import csv

#  User defined functions
 
def createoutput(txtfile, reccount, results_table):

#  Write Election Report information/report to terminal and output file.

    electionrpt = ""
    writetotextfiles(electionrpt)
    writetotextfiles(electionrpt)

    electionrpt = "Election Results"
    writetotextfiles(electionrpt)

    electionrpt = "-------------------------"
    writetotextfiles(electionrpt)

    electionrpt =  f"Total Votes: {reccount}"
    writetotextfiles(electionrpt)

    electionrpt = "-------------------------"
    writetotextfiles(electionrpt)


    #  Election info passed via results_table.  Sort by value in vote_count
    #    and pass along to print the formatted output of the election results.

    # sorted_results_table = {}

    sorted_results_table = {k: v for k, v in sorted(results_table.items(), key=lambda x: x[1], reverse=True)}
    order_name = []

    for name, count in sorted_results_table.items():
        electionrpt = (f'{name}: {(count/reccount) * 100:.3f}% ({count})')
        writetotextfiles(electionrpt)
        order_name.append(name)

    electionrpt = "-------------------------"
    writetotextfiles(electionrpt)

    electionrpt =  f"Winner: {order_name[0]}"
    writetotextfiles(electionrpt)

    electionrpt = "-------------------------"
    writetotextfiles(electionrpt)

    electionrpt = ""
    writetotextfiles(electionrpt)
 
   
def writetotextfiles(electionrpt):

    print(electionrpt)
    txtfile.write(str(electionrpt) + '\n')

# Path to collect data from the Resources folder.
#  Open input/output files and extract header prior to processing (not needed).

csvpath = os.path.join('C:\\Users\\sbell\\python-challenge\\PyPoll\\Resources\\election_data.csv')
txtpath = os.path.join('C:\\Users\\sbell\\python-challenge\\PyPoll\\Resources\\Election_Report.txt')
txtfile =  open(txtpath, "w", encoding="utf-8") 
    
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
 
#  Summary counters, work fields/variables defined and initialized.

    reccount = 0
    results_table = {}
    election_info = []

# File layout - {Voter ID,	County,	Candidate}.

    for election_info in csvreader:
 
#  Increment line count and move election data to their respective variables

        reccount += 1
        key = str(election_info[2])
     
        if key in results_table:
            results_table[key] += 1
        else:
            results_table[key] = 1
        
            
    # print(results_table)


#  Print Election Report report to the terminal
    createoutput(txtfile, reccount, results_table)  
    print("Task ending....")
    