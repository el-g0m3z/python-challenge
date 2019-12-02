import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csv_header = next(csvfile)
    row_count = sum(1 for row in csvfile)

with open(csvpath, newline="") as csvfile2:
    csv_header = next(csvfile2)
    profit_losses = sum(int(r[1]) for r in csv.reader(csvfile2))
    average_changes = int(profit_losses / row_count)

with open(csvpath, "r") as csvfile3:
    csv_reader = csv.DictReader(csvfile3)
    data = list(csv_reader)
    maxProfit = max(data, key=lambda x: x["Profit/Losses"])
    minProfit = min(data, key=lambda x: x["Profit/Losses"])

    print("Financial Analysis")
    print("--------------------------")
    print("Total Months:", row_count)
    print("Total: $", profit_losses)
    print("Average Change: $", average_changes)
    print("Greatest Increase in Profits:", maxProfit)
    print("Greatest Decrease in Profits:", minProfit)

    print("Financial Analysis", file=open("output.txt", "w"))
    print("--------------------------", file=open("output.txt", "a"))
    print("Total Months:", row_count, file=open("output.txt", "a"))
    print("Total: $", profit_losses, file=open("output.txt", "a"))
    print("Average Change: $", average_changes, file=open("output.txt", "a"))
    print("Greatest Increase in Profits:", maxProfit, file=open("output.txt", "a"))
    print("Greatest Decrease in Profits:", minProfit, file=open("output.txt", "a"))
