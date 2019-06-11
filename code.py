# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?
print('City : ', data['info']['city'])
print('Venue: ', data['info']['venue'])

# Which are all the teams that played in the tournament ? How many teams participated in total?
print('Teams Played : ', data['info']['teams'])
print('No of teams participated : ', len('teams'))

# Which team won the toss and what was the decision of toss winner ?
print('The team which won the toss : ', data['info']['toss']['winner'])
print('Decision of toss winner : ', data['info']['toss']['decision'])

# Find the first bowler and first batsman who played the first ball of the first inning
print('First bowler of the match: ', data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
print('First batsman who played the first ball : ', data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])


# How many deliveries were delivered in first inning ?
print('No of deliveries delivered in the first innings : ',
len(data['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print('No of deliveries delivered in second innings : ', 
len(data['innings'][1]['2nd innings']['deliveries']))

# Which team won and how ?
#print(data)
print(data['info']['outcome']['winner'] + 'won the match' + " " + "by" + 
str(data['info']['outcome']['by']['runs']))



