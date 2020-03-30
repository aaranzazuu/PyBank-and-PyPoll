import csv  
file = '../Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv'
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    count = 0 
    net_profit = 0

# Total number of months included in the dataset
    for row in csvreader:
        count = count + 1
    print("Dataset has " + str(count) + " number of rows")

# The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        net_profit = net_profit + row[1]
    print("The net total amount of profit for the entire period is " + str(net_profit))

        



