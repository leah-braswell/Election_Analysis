# Get the data we need to retrieve.
# Add dependencies.
import csv
import os

# Assign a filename variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')

#Assign a filename variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Assign total_votes variable and set to zero.
total_votes = 0

#Declare new list for candidate_options.
candidate_options = []

#Create dictionary for candidate names and votes.
candidate_votes = {}

#WINNING CANDIDATE AND WINNING COUNT TRACKER
#Declare variable to hold empty string value for winning candidate.
winning_candidate = ""

#Assign a variable for winning count and set to zero.
winning_count = 0

#Assign a variable for winning_percentage and set to zero.
winning_percentage = 0


#OPEN the election results and read the file.
with open(file_to_load) as election_data:

    #READ and analyze data here.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #loop through each row in the CSV file.
    for row in file_reader:
       #increment total_votes by 1 for each loop
        total_votes +=1

        #Retrieve the candidate name for each row using the colum index.
        candidate_name = row[2]

        #Check to see if candidate_name is already in candidate_options list.
        if candidate_name not in candidate_options:
            #Add candidate_name to candidate_options list.
            candidate_options.append(candidate_name)

            #Begin tracking votes by adding candidate_name as a key in candidate_votes.
            candidate_votes[candidate_name] = 0

        #increase value for candidate_votes by taking it OUT of the if statement
        candidate_votes[candidate_name] +=1

 #Write results to text file
with open(file_to_save, 'w') as txt_file:
    election_results = (
        f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-------------------------\n')
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)

        

    #loop through dictionary to get candidate's name
    for candidate_name in candidate_votes:

        #Retrieve values for each candidate_name from candidate_votes{}
        votes = candidate_votes[candidate_name]

        #calculate percentage and return as a floating decimal
        vote_percentage = float(votes) / float(total_votes) * 100

        #create variable for candidate results
        candidate_results = (f"{candidate_name}:  {vote_percentage: .1f}% ({votes:,})\n")

        #print candidate_results to terminal and txt file
        print(candidate_results)
        txt_file.write(candidate_results)
                        
        #Determine if the vote count is greater than winning_count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
             #if true set winning_count = votes, winning_percentage = vote_percentage, winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

            #Print winning candidate summary
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------')
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
   
                        

#Close the file.
election_data.close()
