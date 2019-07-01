import csv
import os

rowcnt = 1
maxchg = 0
minchg = 0
NumOfMonths = 0
Tot_ProfitLoss = 0
tot_delta = 0

# Store filepath in a variable
csvpath = "Resources/budget_data.csv"

# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
# budget_df = pd.read_csv(budgetfile, encoding="ISO-8859-1")

# Method 2: Improved Reading using CSV module
#csvpath = os.path.join('../../', 'Resources', 'budget_data.csv')
with open(csvpath, newline="") as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)

# Prepare a list to store budget data rows
    budget_data = list(csvreader)

# Count the number of months in this csv file
    NumOfMonths = len(budget_data)

# The net total amount of "Profit/Losses" over the entire period
    Tot_ProfitLoss = sum(float(r[1]) for r in budget_data)

# The average of the changes in "Profit/Losses" over the entire period 
#--------------------------------------------------------------------------------------
# Add column to budget_data list to store delta (1 month profit loss change)
    budget_data = [x + [0] for x in budget_data]

# Calculate Delta and store it in the last column of each row in budget_data list
    index = 0
    hld_curr = 0
    for index, row in enumerate(budget_data):
        if index == 0: 
            hld_last = float(row[1])
            index += 1
        else:
            hld_curr = float(row[1])
            delta = hld_curr - hld_last
            row[2] = delta
            tot_delta += delta
# Check for min and max monthly delta's 
            if  delta < minchg:
                minDate = row[0]
                minchg = delta
            elif delta > maxchg:
                maxDate = row[0]
                maxchg = delta
            hld_last = hld_curr
            hld_curr = 0    
            

# Determine average change for the period    
avgchg = tot_delta/(NumOfMonths - 1)

#Report Analysis Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {NumOfMonths}")
print(f"Total: ${int(round(Tot_ProfitLoss))}")
print(f"Average  Change: ${round(avgchg, 2)}")
print(f"Greatest Increase in Profits: {maxDate} (${int(round(maxchg))})")
print(f"Greatest Decrease in Profits: {minDate} (${int(round(minchg))})")

f = open('main_Results.txt', 'w')
f.write("%s\n" % "Financial Analysis")
f.write("%s\n" % "----------------------------")
Total_Months = "Total Months: " + str(NumOfMonths) + "\n"
f.write(Total_Months)
tot_pl = "Total: $" + str(int(round(Tot_ProfitLoss))) + "\n"
f.write(tot_pl)
delta_chg = "Average  Change: $" + str(round(avgchg, 2)) + "\n"
f.write(delta_chg)
max_info = "Greatest Increase in Profits: " + str(maxDate) + "  ($" + str(round(maxchg, 0)) + ")\n"
f.write(max_info)
min_info = "Greatest Decrease in Profits: " + str(minDate) + "  ($" + str(round(minchg, 0)) + ")\n"
f.write(min_info)

f.close()


        
        


        

        
        
        
        
        
        
