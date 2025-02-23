import os
import csv

csvpath = os.path.join('.', 'budget_data.csv')
outputpath = 'pnl_SooBin.txt'

month = []
total = 0
pnl = []
pnl_0 = 0
delta = []

with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:

        # Total months
        month.append(row[0])

        # Total profit and loss
        total += int(row[1])

        # Average change in profit and loss
        pnl.append(row[1])
        delta_i = int(row[1]) - int(pnl_0)
        delta.append(delta_i)
        pnl_0 = row[1]

    # Removing the first element and setting up the total number of interval
    delta.pop(0)
    interval = len(delta)
    change = round(sum(delta) / interval, 2)

    # Greatest increase and decrease in change
    mostIncreased = max(delta)
    mostDecreased = min(delta)

    monthIncreased = month[delta.index(mostIncreased) + 1]
    monthDecreased = month[delta.index(mostDecreased) + 1]

# Print in console
print("Financial Analysis\n"
           "----------------------------\n"
          f"Total Months: {len(month)}\n"
          f"Total: ${total}\n"
          f"Average Change: ${change}\n"
          f"Greatest Increase in Profits: {monthIncreased} (${mostIncreased})\n"
          f"Greatest Decrease in Profits: {monthDecreased} (${mostDecreased})\n")

# Creating a text file
txtfile = open(outputpath, 'w', newline = '')
txtfile.write("Financial Analysis\n"
           "----------------------------\n"
          f"Total Months: {len(month)}\n"
          f"Total: ${total}\n"
          f"Average Change: ${change}\n"
          f"Greatest Increase in Profits: {monthIncreased} (${mostIncreased})\n"
          f"Greatest Decrease in Profits: {monthDecreased} (${mostDecreased})\n")
txtfile.close()