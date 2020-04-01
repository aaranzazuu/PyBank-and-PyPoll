import csv  
file = '../PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv'
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    count = 1
    candidate_list = []

    for row in csvreader:
        count = count + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])




    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")
    print(candidate_list)
    print("--------------------")
    print("Winner: ")
    print("--------------------")