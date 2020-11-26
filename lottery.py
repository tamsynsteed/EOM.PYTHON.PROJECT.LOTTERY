import random

userNumbers = []
#we want the user to input 6 numbers
for i in range(0,6):

    number = int(input("Please enter a number between 1 and 49:"))
    while (number in userNumbers or number<1 or number>49): #make sure user is not entering a same number or numb out of range. use while loop
        print("invalid number, try again")
        number = int(input("Please enter a number between 1 and 49:")) # put this into while loop

#if number is valid it will be appended to list of users.
    userNumbers.append(number)

#---------------------------------------------------------------------


lot_num = [] #intialize empty list

for i in range (0,6): #used a for loop that repeats 6 times, to generate r random numbers.
  number = random.randint(1,49)

  while number in lot_num:
    number= random.randint(1,49)
#make sure these numbers are unique, using a while loop this checks if the number is already in the list,
#if it is,then we need to create a new random number, do it again until we find a unique number


  lot_num.append(number) #once we have a new number, we append it to our list.

#sort list in ascending order.
lot_num.sort()

#-----------------------------------------
#Display list

#display user selection.
print("These are your chosen lottery numbers:")
print(userNumbers)

print(">>>Todays lottery numbers are:")
print(lot_num)

#--------------------------------------------------------------
#now we are comapring both lists to see if we have won anything
#count hw many of the numbers appear in both lists

#we use a counter, and initialize it to zero

counter= 0
#for each number from the userNUmbers, if the number is in the lottery list, the counter will increment by 1.
for number in userNumbers:
    if number in lot_num:
        counter +=1

print("You guessed:" + str(counter) + " number(s) correctly") #convert counter to string
