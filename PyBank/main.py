import os
import csv
import sys

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

#counter to count the number of rows in the dataset
counter = 0
#total of profit/losses column
net = 0
# the profit/loss from the previous month
lastMonth = 0
# the current month profit/loss - lastmonth
changes = 0
# the greatest increase of profit/loss
greatestIncrease = 0
# the greatest decrease of profit/loss
greatestDecrease = 0
# the month of greatest decrease in profit/loss
decreaseMonth = ''
# the month of greatest increase in profit/loss
increaseMonth = ''

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:

        net += int(row[1])
        #changes += int(row[1]) + lastMonth
        changes += int(row[1]) - lastMonth

        if changes>greatestIncrease:
            greatestIncrease = int(row[1]) - lastMonth
            increaseMonth = row[0]
            #lastMonth = int(row[1])

        if changes<greatestDecrease:
            greatestDecrease = int(row[1]) - lastMonth
            decreaseMonth = row[0]
            #lastMonth = int(row[1])

        lastMonth = int(row[1])
        counter += 1

# file = open('hw1.txt', 'w')
# sys.stdout = file

sys.stdout = open('hw1.txt', 'w')

print("Total Months:",counter)
print("Total:",net)
print('change Total:',changes)
print("average:",changes/counter)
print('The month of greatest increase in profits was in',increaseMonth,'the increase was',greatestIncrease)
print('The month of greatest decrease in profits was in',decreaseMonth,'the decrease was',greatestDecrease)
# file.close()

# print("Total Months:",counter, "Total:",net, 'change Total:',changes, "average:",changes/counter, 'The month of greatest increase in profits was in',increaseMonth,'the increase was',greatestIncrease, 'The month of greatest decrease in profits was in',decreaseMonth,'the decrease was',greatestDecrease, sys.stdout = open('hw1.txt', 'w'))



# Loop through each difference between months
# and store that value in an array

# #add each stored value in the array
# with open(csvpath, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)
#     for row in csvreader:
#         net += int(row[1])
#         # += Add AND
#         # It adds right operand to the left operand
#         # and assign the result to left operand
#         # c += a is equivalent to c = c + a
#         #changes += int(row[1]) + lastMonth
#         changes += int(row[1]) - lastMonth
#         #changes += lastMonth + int(row[1])
#         #changes += lastMonth - int(row[1])
#         if changes>greatestIncrease:
#             greatestIncrease = int(row[1]) - lastMonth
#             increaseMonth = row[0]
#             #lastMonth = int(row[1])
#         if changes<greatestDecrease:
#             greatestDecrease = int(row[1]) - lastMonth
#             decreaseMonth = row[0]
#             #lastMonth = int(row[1])
#         lastMonth = int(row[1])
#         counter += 1
#         monthlychange = []
#         for changes in monthlychange:
#             monthlychange.append(changes)
#             print map(int.changes)

# averagechanges = sum(changes in monthlychanges)
#
# print([map(monthlychange)])
