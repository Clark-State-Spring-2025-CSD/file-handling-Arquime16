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

total_sum = 0

total = open("numbers.txt", "r")
for line in total:
    for numbers in line.split():
        if numbers.isnumeric():
            total_sum += int(numbers)

total.close()
print("Total sum of numbers:", total_sum)








