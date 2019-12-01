import os
import csv
import pprint
import numpy

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csv_header = next(csvfile)
    row_count = sum(1 for row in csvfile)
with open(csvpath, newline="") as csvfile2:
    csv_header = next(csvfile2)
    profit_losses = sum(int(r[1]) for r in csv.reader(csvfile2))
    average_changes = int(profit_losses / row_count)

min_max = np.genfromtxt(csvpath, delimiter=",", skip_header=True)
    print ("min value element : ", min_max.min(axis=0)[1])
    print ("max value element : ", min_max.max(axis=0)[2])

    print("Financial Analysis", file=open("output.txt", "a"))
    print("Total Months:", row_count, file=open("output.txt", "a"))
    print("Total: $", profit_losses, file=open("output.txt", "a"))
    print("Average Change: $", average_changes, file=open("output.txt", "a"))
    print("Greatest Increase in Profits:", file=open("output.txt", "a"))
    print("Greatest Decrease in Profits:", file=open("output.txt", "a"))

results_file = open
# csvreader = csv.reader(csvfile, delimiter=",")

# print(csvreader)


# print(f"CSV Header: {csv_header}")

# for row in csvreader:

#     print(row)
