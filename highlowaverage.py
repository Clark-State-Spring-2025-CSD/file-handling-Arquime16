#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

#How many numbers in the file

count = 0

file = open("numbers.txt", "r")
for line in file:
    for eachNumbers in line.split():
        if eachNumbers.isnumeric():
            count += 1

file.close()          
print(f"Total numbers:", count)

#Total of all the number

total_sum = 0

total = open("numbers.txt", "r")
for line in total:
    for numbers in line.split():
        if numbers.isnumeric():
            total_sum += int(numbers)

total.close()
print("Total sum of numbers:", total_sum)

#Average


myFile = open("numbers.txt")

sum = 0
myBudget = 0
myMoney = 0
myResult = 0
myBank = 0
myNumbers = 0

for petLine in myFile:
    veLine = int(petLine)
    myBudget += 1 
    sum += veLine
    if veLine % 2 == 0:
        myBank += 1
    else:
        myNumbers += 1
    if veLine == 1:
        myMoney += 1
    if veLine == 493:
        myResult += 1

myFile.close()

avg = sum / count 

print(f"The average is {avg}.")

#Highest number

myFile = open("numbers.txt")

maxValue = None
minValue = None


for line in myFile:
    line = int(line.strip())
    if maxValue is None or line > maxValue:
        maxValue = line
    if minValue is None or line < minValue:
        minValue = line

print(f"Number of Highest Value {maxValue}") 
print(f"Number of Lowest Value {minValue}")  

myFile.close()
    












