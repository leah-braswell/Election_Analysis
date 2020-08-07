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

#print out total_votes
print(total_votes)

#Close the file.
election_data.close()



#Using the with statement open the file as a text file.
with open(file_to_save, 'w') as txt_file:

    #write some data to the file.
    txt_file.write('Counties in the Election\n-------------\nArapahoe\nDenver\nJefferson')

#Close the file

# 1. The total number of votes cast.

# 2. A complete list of candidates who received votes in the election.

# 3. The total number of votes each candidate won.

# 4. The percentage of votes for each candidate.

# 5. The winner of the election based on popular vote.
