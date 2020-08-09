# Election_Analysis
PyPoll Project for BootCamp Week 3 using Python

## Project Overview
A Colorado Board of Elections employee has asked me to perform the following tasks in order to certify a Congressional Election.

1.  Calculate the total number of votes cast in the election.
2.  Provide a complete list of candidates who received votes.
3.  Calculate the total number of votes each candidate received.
4.  Calculate the percentage of the total votes each candidate received.
5.  Determine the winning candidate based on popular vote.

## Challenge Overview
The Colorado Board of Elections employee has requested further information on the election results to complete their audit.  They would like the following additional information:

1.  The number of votes cast in each county in the election.
2.  The percentage of votes from each county out of the total vote count.
3.  The county with the highest number of votes cast.

## Resources
 - Data Source:  election_results.csv
 - Software:  Python 3.7.6 (64 bit), Visual Studio Code
 
## Results
The analysis of the election showed that:
- There were 369,711 total votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGett
  - Raymon Anthony Doane
  
- The candidates results were:
  - Charles Casper Stockham recieved 23% of the vote and 85,213 total votes.
  - Diana DeGett recieved 73.8% of the vote and 272,892 total votes.
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 total votes.
  
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 votes.
  
The additional analysis of the election showed that:
- There were 369,711 total votes cast in the election.

- The results from each county were as follows:
	- 38,855 votes were cast in Jefferson County, accounting for 10.5% of the total vote.
	- 306,055 votes were cast in Denver County, accounting for 82.8% of the total vote.
	- 24,801 votes were cast in Arapahoe County, accounting for 6.7% of the total vote.

- The county with largest number of votes cast was Denver County.

### Examples of Code
To begin my analysis I needed to import the csv and os dependencies.  This allowed me to access the data contained in the files the Board of Elections provided me.  I then created variables for the files I would need to open to retrieve the data and save to record the results.
- `file_to_load = os.path.join(...)`
- `file_to_save = os.path.join(...)`

I then created lists and dictionaries to hold the various pieces of information the Board requested.
- Examples are:
	- `candidate_options[]` and `county_list[]`: lists to hold the names of the candidates and counties
	- `candidate_votes{}` and `county_totals{}`:  dictionaries to hold the total votes cast for each candidate and in each county

I initialized variables set to zero to reflect the total numbers and percentages of votes cast.
- Examples initialized before loops are:
	- `total_votes = 0`:  overall number of votes cast in the election
	- `winning_count = 0`:  number of votes for winning candidate
	- `largest_turnout = 0`: largest number of votes cast in a county

- Examples initialized during loops are:
	- `county_votes = county_totals[county_name]`:  value for number of votes cast in each county
 - `vote_percentage = float(votes) / float(total_votes) * 100`:  floating decimal for the percentage of votes earned by each candidate

I used `with open()` to access the election data and looped throgh each row to retrieve total votes, candidate names `row[2]` and county names `row[1]`.  Using `dictionay[key]` I increased the value to calculate votes for each candidate, and votes cast in each county.  I used conditional statements such as `if county_name not in county_list` to determine if candidate and county names were already included in the lists created and used `.append` to add them to the appropriate list if they were not already there.  I also used conditional staements such as `if county_votes > largest_turnout` to determine the county with the largest number of votes cast and the candidate with the greatest number of votes earned.

I used `txt_file.write` to record my results in the text file requested by the Board and `print()` to print results to the terminal.

The use of f-strings `(f" ")` allowed me to easily write text in a readable format.  I used `: .1f` and ": ," to format percentages and vote totals to be easily read by the Board.


## Challenge Summary
This script could easily be used in other elections due to the use of variables and indexes.  If the data set contained more information, it would be simple to add a variable to break down votes per precinct within each County as well as analyze other demographic data such as gender, race, and political party.  I would suggest using the total number of registered voters in each county to provide a more accurate measure of voter turnout.  Denver County may have had significantly more registerd voters than the other counties which would result in a greater number of votes cast, however we do not know what percentage of registered voters in this county cast a vote in the election.  Simply reporting the total number of votes cast is not the same as "voter turnout" which is usually calcluated as (total number of votes cast / total number of registered voters).  The availability of more specific demographic data could be of use to future candidates, policital parites, and Supervisors of Elections in future elections.  This would help with increasing voter turnout, adequate staffing of polling places, and informing future platforms.


