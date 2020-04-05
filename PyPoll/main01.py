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
    
    #Winner of the election 
    winner_candidate = max(votes_dictionary.keys(), key=(lambda k: votes_dictionary[candidates]))

    #Percentage of votes each candidate won
    for candidates in votes_dictionary:
        votes_percentage = "{0:.2%}".format(votes_dictionary[candidates]/count)
        votes_percentage_list.append(votes_percentage)
    
    #Transform dictionary into lists for printing
    candidates_list = list(votes_dictionary.keys())
    candidates_votes = list(votes_dictionary.values())


    #Print the analysis to terminal
    print("Election Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")
    for i in range(len(candidates_list)):
        print(candidates_list[i] + " : " + votes_percentage_list[i] + " (" + str(candidates_votes[i])+ ")")
    print("--------------------")
    print("Winner: " + winner_candidate)
    print("--------------------")

    #Export a text file with the results