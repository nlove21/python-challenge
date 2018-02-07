import os
import csv

csvpath = os.path.join('budget_data_1.csv')

totalMonths = 0
totalRevenue = 0
monthsList = []
revenueList = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        totalMonths += 1
        monthsList.append(row[0])            
        revenueList.append(int(row[1]))
        
        if row[1] != "Revenue":
            totalRevenue += int(row[1])
            
greatInc = revenueList[0] 
greatDec = revenueList[0]

for x in range(len(revenueList)):        
    if revenueList[x] >= greatInc:            
        greatInc = revenueList[x]            
        greatIncMonth = monthsList[x]        
    elif revenueList[x] <= greatDec:            
        greatDec = revenueList[x]            
        greatDecMonth = monthsList[x]
        
avgChange = round(totalRevenue/totalMonths, 2)  
        
        
#print to terminal
print ("\nFinancial Analysis \n-------------------------------------\n", "\nNumber of Months: ", totalMonths, "\nTotal Revenue: $", totalRevenue, "\nAverage Revenue Change: $", avgChange, "\nGreatest Increase in Revenue: $", greatInc,  "\nGreatest Decrease in Revenue: $", greatDec, sep='')

#print to file
with open(Financial Results, 'w') as writefile:        
    writefile.writelines("\nFinancial Analysis \n-------------------------------------\n", "\nNumber of Months: ", totalMonths, "\nTotal Revenue: $", totalRevenue, "\nAverage Revenue Change: $", avgChange, "\nGreatest Increase in Revenue: $", greatInc,  "\nGreatest Decrease in Revenue: $", greatDec, sep='')
