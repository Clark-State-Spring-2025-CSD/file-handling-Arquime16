#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

file = open("words.txt")

count = 0

for line in file.readlines():
  line = line.strip()
  if line == ''.join(reversed(line)):
    count += 1
    print(f"{line}")
    
print(f"{count}")
    
file.close()
    
  


 