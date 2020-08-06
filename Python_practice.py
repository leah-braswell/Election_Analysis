print("Hello World")

counties = list()
counties.append("Arapahoe")
counties.append("Jefferson")
counties.append("Denver")
print(counties[1])
if counties[2] =='Denver':
    print(counties[2])
if "El Paso" in counties:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not in the list of counties.')
if 'Arapahoe' in counties or 'El Paso' in counties:
    print('Arapahoe or El Paso is in the list of counties.')
else:
    print('Arapahoe and El Paso are not in the list of counties.')

#Example of for loop
for county in counties:
    print(county)

#using range() to loop through list of strings
for i in range(len(counties)):
    print(counties[i])

counties_dict = {}
counties_dict['Arapahoe'] = 422829
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
counties_dict


for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

voting_data = []

voting_data.append({'county':'Arapahoe' , 'registered_voters' : 422829})
voting_data.append({'county':'Denver', 'registered_voters' :463353})
voting_data.append({'county': 'Jefferson', 'registered_voters': 432438})


for counties_dict in voting_data:
    print(counties_dict)

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for counties_dict in voting_data:
    print(counties_dict['county'])

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input('What is the total votes in the election?'))
print (f'I received {my_votes/total_votes * 100}% of the total votes.')

candidate_votes = int(input('How many votes did the candidate get in the election?'))
total_votes = int(input('What is the total number of votes in the election?'))
message_to_candidate = (
    f'You received {candidate_votes:,} number of votes.'
    f'The total number of votes in the election was {total_votes: ,}.'
    f'You received {candidate_votes / total_votes * 100: .2f}% of the total votes.')
print(message_to_candidate)

for counites_dict in voting_data:
    for county, voters in counties_dict:
        print(f'{'county'} has {'voters':,} registered voters.')
