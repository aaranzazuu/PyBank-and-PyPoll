import csv  

file = '../PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv'
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    count = 0
    votes_list = []
    votes_dictionary = {}
    results = 0
    votes_percentage_list = []

    for row in csvreader:
        count = count + 1
        votes_list.append(row[2])
    for candidates in votes_list:
        if candidates in votes_dictionary:
            votes_dictionary[candidates] += 1     
        else:
            votes_dictionary[candidates] = 1
    for candidates in votes_dictionary:
        votes_percentage = votes_dictionary[candidates]/count
        votes_dictionary.update(candidates:votes_percentage)
        #votes_percentage_list.append(votes_percentage)


    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")
    print(votes_dictionary)
    #print(votes_percentage_list)
    # print((candidate_list[1]) + ":" + "{:.2%}".format(percentage_Khan)+ "("+str(votes_Khan)+")")
    #print((candidate_list[2])+ ":" + "{:.2%}".format(percentage_Correy) + "("+str(votes_Correy)+")")
    #print((candidate_list[3])+ ":" + "{:.2%}".format(percentage_Li) + "("+str(votes_Li)+")")
    #print((candidate_list[4])+ ":" + "{:.2%}".format(percentage_OTooley)+ "("+str(votes_Otooley)+")")
    #print("--------------------")
    #print("Winner: ")