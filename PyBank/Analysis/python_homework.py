import csv  
file = '../Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv'
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)

    count = 1
    net_profit = int(first_row[1])
    previous_value = int(first_row[1])
    sum_changes = 0

# Total number of months included in the dataset
    for row in csvreader:
        count = count + 1
        net_profit = net_profit + int(row[1])
        changes = int(row[1])-int(previous_value)
        sum_changes = sum_changes + changes
        previous_value = int(row[1])
    
    net_changes = sum_changes/count

    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(net_profit))
    print(str(changes))
    print(str(net_changes))
    print("Greatest Increase in Profits:")
    print("Greatest Decrease in Profits")