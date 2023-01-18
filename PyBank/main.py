import os
import csv

#create path to pull in data from csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#set variables for calculations and list storage
TotalMonths = []
TotalPandL = []
MonthlyPChange = []

MonthlyChange = 0
MonthlyTotalChange = 0


#open files in use & ignore header row
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    for row in csvreader:
    #set total month list equal to date values of csv
        TotalMonths.append(row[0])
    #set varialbe and count number of months
        TotalMonthCount = len(TotalMonths)
    #set total profit and losses to p/l values of csv
        TotalPandL.append(float(row[1]))
    #set variable to integer value of p/l values of csv
        MonthlyProfit = int(row[1])
    #set variable to decimal value of monthly profit
        MonthlyChange = float(MonthlyProfit)
    #set variable to sum of monthly total change and monthly change
        MonthlyTotalChange = MonthlyTotalChange + MonthlyChange
    #set monthly profit change list to value of monthly change
        MonthlyPChange.append(MonthlyChange)
    #find max value of monthly profit change list
        GreatestInc = max(MonthlyPChange)
    #index date of max value of monthly profit change list
        GreatestIncIndex = MonthlyPChange.index(GreatestInc)
    #find min value of monthly profit change list
        GreatestDec = min(MonthlyPChange)
    #index date of min value of monthly profit change list
        GreatestDecIndex = MonthlyPChange.index(GreatestDec)
    #set variable to value of monthly total change divided by total month count
        AvgChange = (MonthlyTotalChange/TotalMonthCount)
    #set variable to sum of total p/l
        SumTotalPandL = sum(TotalPandL)

#print to terminal for display
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {TotalMonthCount}')
print(f'Total: ${SumTotalPandL}')
print(f'Average Change: {AvgChange}')
print(f'Greatest Increase in Profits: {TotalMonths[GreatestIncIndex]} ${GreatestInc}')
print(f'Greatest Decrease in Profits: {TotalMonths[GreatestDecIndex]} ${GreatestDec}')

#output to txt file
output = open("FinancialAnalysis.txt", 'w')
output.write(f'''
Financial Analysis
-------------------------
Total Months: {TotalMonthCount}
Total: ${SumTotalPandL}
Average Change: {AvgChange}
Greatest Increase in Profits: {TotalMonths[GreatestIncIndex]} (${GreatestInc})
Greatest Decrease in Profits: {TotalMonths[GreatestDecIndex]} (${GreatestDec})''')

#close txt
output.close()
