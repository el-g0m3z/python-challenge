import os
import csv
import pprint

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)
data = list(csv_reader)

pprint.pprint(data)
