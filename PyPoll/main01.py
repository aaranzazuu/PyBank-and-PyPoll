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
        #The total number of votes cast
        count = count + 1
        #Create a list of all the votes
        votes_list.append(row[2])
    #Create a dictionary that counts all the votes. Candidates as key, total number of votes for each candidate as value.
    for candidates in votes_list:
        if candidates in votes_dictionary:
            votes_dictionary[candidates] += 1
        else:
            votes_dictionary[candidates] = 1
    
    #Transform dictionary into lists for printing
    candidates_list = list(votes_dictionary.keys())
    candidate_votes = list(votes_dictionary.values())

    #Percentage of votes each candidate won
    for candidates in votes_dictionary:
        votes_percentage = "{0:.2%}".format(votes_dictionary[candidates]/count)
        votes_percentage_list.append(votes_percentage)
    


    #Winner of the election 

    #Print the analysis to terminal
    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")
    print(candidates_list[0])
    print(candidate_votes[0])
    #print(votes_dictionary)
    print(votes_percentage_list[0])
    # print((candidate_list[1]) + ":" + "{:.2%}".format(percentage_Khan)+ "("+str(votes_Khan)+")")
    #print((candidate_list[2])+ ":" + "{:.2%}".format(percentage_Correy) + "("+str(votes_Correy)+")")
    #print((candidate_list[3])+ ":" + "{:.2%}".format(percentage_Li) + "("+str(votes_Li)+")")
    #print((candidate_list[4])+ ":" + "{:.2%}".format(percentage_OTooley)+ "("+str(votes_Otooley)+")")
    #print("--------------------")
    #print("Winner:)

    #Export a text file with the results