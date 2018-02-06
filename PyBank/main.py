import os
import csv


csvpath = os.path.join('budget_data_1.csv')

#Print to terminal
print("\nFinancial Analysis \n ----------------------------------\n")


totalMonths = 0
totalRevenue = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        
        totalMonths += 1
        if row[1] != "Revenue":
            totalRevenue += int(row[1])
        

print ("\nNumber of Months: ", totalMonths, "\nTotal Revenue: $", totalRevenue, "\nAverage Revenue Change: ", "\nGreatest Increase in Revenue: ", "\nGreatest Decrease in Revenue: ", sep='')