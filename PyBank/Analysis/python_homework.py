import csv  
file = '../Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv'
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)

    count = 1
    net_profit = int(first_row[1])
    previous_value = int(first_row[1])
    previous_month = first_row[0]
    sum_changes = 0
    greatest_value = int(first_row[1])
    greatest_value_month = first_row[0]
    lowest_value = int(first_row[1])
    lowest_value_month = first_row[0]
    list_changes = []

# Total number of months included in the dataset
    for row in csvreader:
        count = count + 1
        net_profit = net_profit + int(row[1])
        changes = int(row[1])-int(previous_value)
        list_changes.append(changes)
        if int(greatest_value) > int(row[1]):
            greatest_value = greatest_value
            greatest_value_month = greatest_value_month
        else: 
            greatest_value = int(row[1])
            greatest_value_month = row[0]
        if int(lowest_value) < int(row[1]):
            lowest_value = lowest_value
            lowest_value_month = lowest_value_month
        else: 
            lowest_value = int(row[1])
            lowest_value_month = row[0]
        sum_changes = sum_changes + changes
        previous_value = int(row[1])
    average_changes = sum_changes/(count-1)
    greatest_increase = max(list_changes)
    greatest_decrease = min(list_changes)
    
    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(net_profit))
    print("Average Change: $ "+ str(average_changes))
    print("Greatest Increase in Profits:" + greatest_value_month + "($" + str(greatest_increase)+ ")")
    print("Greatest Decrease in Profits:" + lowest_value_month + "($" + str(greatest_decrease)+ ")")