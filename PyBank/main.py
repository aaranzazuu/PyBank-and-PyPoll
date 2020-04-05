import csv 

#Open file
file = '../PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv'
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


    for row in csvreader:
        #Total number of months in the dataset
        count = count + 1
        #Net total amount of Profit/Losses over the entire period
        net_profit = net_profit + int(row[1])
        #Calculate changes for the averages
        changes = int(row[1])-int(previous_value)
        list_changes.append(changes)
        #Calculate the month where the greates changes happened
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
        #Reset variable previous_value
        previous_value = int(row[1])
        #Calculations for average
        sum_changes = sum_changes + changes
    
    #Calculate average changes
    average_changes = round(sum_changes/(count-1),2)

    #Calculate greates increase in profits and greatest decrease in losses
    greatest_increase = round(max(list_changes),2)
    greatest_decrease = round(min(list_changes),2)
    
    #Print Analysis to Terminal
    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(net_profit))
    print("Average Change: $ "+ str(average_changes))
    print("Greatest Increase in Profits:" + greatest_value_month + "($" + str(greatest_increase)+ ")")
    print("Greatest Decrease in Profits:" + lowest_value_month + "($" + str(greatest_decrease)+ ")")
    
#Export

output_path = '../PyBank/Analysis/Financial_Analysis.txt'
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Total Months: " + str(count)]) 
    csvwriter.writerow(["Total: $: " + str(net_profit)])
    csvwriter.writerow(["Average Change: $ "+ str(average_changes)])
    csvwriter.writerow(["Greatest Increase in Profits:" + greatest_value_month + "($" + str(greatest_increase)+ ")"])
    csvwriter.writerow(["Greatest Decrease in Profits:" + lowest_value_month + "($" + str(greatest_decrease)+ ")"])