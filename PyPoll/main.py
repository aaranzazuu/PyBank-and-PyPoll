import csv  
file = '../PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv'
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    count = 1
    candidate_list = []
    votes_Khan = 0
    votes_Correy = 0
    votes_Li = 0
    votes_Otooley = 0

    for row in csvreader:
        count = count + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] == "Khan":
            votes_Khan = votes_Khan + 1
        elif row[2] == "Correy":
            votes_Correy = votes_Correy + 1
        elif row[2] == "Li":
            votes_Li = votes_Li + 1
        elif row[2] == "O'Tooley":
            votes_Otooley = votes_Otooley + 1
    
    percentage_Khan = votes_Khan/count
    percentage_Correy = votes_Correy/count
    percentage_Li = votes_Li/count
    percentage_OTooley = votes_Otooley/count


    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")
    print(candidate_list)
    print([str(percentage_Khan), str(votes_Khan), str(percentage_Correy), str(votes_Correy), str(percentage_Li), str(votes_Li), str(percentage_OTooley), str(votes_Otooley)])
    print("--------------------")
    print("Winner: ")
    print("--------------------")