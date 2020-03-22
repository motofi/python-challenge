
import csv
import os

counter = 0
candidates = {}
mostVotes = 0
winner = ''

csvpath = os.path.join('.', 'election_data.csv')

with open(csvpath, newline='') as file:


    reader = csv.reader(file,delimiter=',')
    header = next(reader)
    for row in reader:
        counter +=1
        if row[2] not in candidates:
            candidates[row[2]] = {
                'name': row[2],
                'votes': 1
            }
        else:
            candidates[row[2]]['votes'] += 1
    print('Election Results\n-------------------------\nTotal Votes:',counter,'\n-------------------------')
    for candidate in candidates:
        print("{0}: {1:.2f}% ({2})".format(candidates[candidate]['name'],(candidates[candidate]['votes']/counter)*100,candidates[candidate]['votes']))
        if(candidates[candidate]['votes']>mostVotes):
            mostVotes = candidates[candidate]['votes']
            winner = candidates[candidate]['name']

    print('-------------------------\nWinner: {0}\n-------------------------'.format(winner))
