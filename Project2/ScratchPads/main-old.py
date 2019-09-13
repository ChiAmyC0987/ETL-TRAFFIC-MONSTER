# Import csv file
import csv

# initialize variables to hold integer, strings, lists
row = 0
City_ID = []
ID_Count = 0
Weather = [[]]


file_name = "Resources/cities.csv"

# Open the cities.csv
with open(file_name, newline='') as csv_file:
    csvreader = csv.reader(csv_file)  # Read each line of Data as row

    for row in csvreader:
        Weather.append(row[1])
        ID_Count += 1  # Find number of cities
    print('ID_Count:', ID_Count)

    j = 2 # Calculate Sum
    while j < ID_Count:
        Value = Profit_Loss[j]
        Value2 = Profit_Loss[j-1]
        Sum_Profit = int(Value) + int(Value2)
        print(Sum_Profit)
        j += 1

    i = 2  # Calculate change in Profit
    while i < Month_Count:
        Profit_Loss_Now = Profit_Loss[i]
        Profit_Loss_Past = Profit_Loss[(i - 1)]
        Diff = int(Profit_Loss_Now) - int(Profit_Loss_Past)
        print(Profit_Loss_Now, Profit_Loss_Past, Diff)
        Delta_Profit.append(Diff)
        i += 1

    print(' Sum Value:   ',Sum_Profit)  # Find current value
    print(' Max profit:   ',max(Delta_Profit))  # Find greatest increase
    print(' Min profit:   ',min(Delta_Profit))  # Find greatest decrease
    print(' Average profit:   ',int(sum(Delta_Profit)/Month_Count))  # Calculate average month to month change

output_file = "Resources/cities_output.csv"
with open(output_file, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(Delta_Profit)
