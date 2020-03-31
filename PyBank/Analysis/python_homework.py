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
        net_profit = net_profit + int(row[1])
    
    def average (profits):
        avg = count/net_profit
        return avg
    net_list=row[1]
    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(net_profit))
    print("Average Change: $" + str(avg(net_list)))
    print("Greatest Increase in Profits:")
    print("Greatest Decrease in Profits")

        



