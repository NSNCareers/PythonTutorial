import csv

with open("BackEndAutomation/utilities/loanadd.csv") as csvFile:
    csvReader = csv.reader(csvFile)
    for rows in csvReader:
        print(list(rows))

with open("BackEndAutomation/utilities/loanadd.csv", "a") as wFile:
    csvWriter = csv.writer(wFile)
    csvWriter.writerow(["Linus", "Rejected"])

if __name__ == "__main__":
    pass
