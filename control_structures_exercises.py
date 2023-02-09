#Do your work for this exercise in a file named 
#control_structures_exercises.py.

#Conditional Basics

#1 prompt the user for a day of the week, print out whether the day 
#is Monday or not
day_of_week = input("enter the day of week ")
if day_of_week.lower() == 'monday':
    print("The day of week is "  + day_of_week)
else:
    print('The day of the week is not Monday')


#2 prompt the user for a day of the week, print out whether the day 
#is a weekday or a weekend
from datetime import datetime
  
# Get Day Number from weekday
weekno = datetime.today().weekday()
 
if weekno < 5:
    print("Today is a Weekday")
else:  
    # 5 Sat, 6 Sun
    print("Today is a Weekend")
###### above pulls is based on the current day of the week

day_of_week = input('enter a day ')
if day_of_week.lower() in ['saturday','sunday']:
    print('This is a weekend')
else:
    print('This is a weekday')
#3 create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours

num_hours_week = 100
hourly_rate = 50.00
ot_hourly_rate = 1.5
ot_hours_week = 20
paycheck_ot = (ot_hours_week * (hourly_rate * ot_hourly_rate)) + paycheck_r
paycheck_r = hourly_rate * 40
if num_hours_week > 40:
    print(str(paycheck_ot) + " Overtime check")
else:
    print(str(paycheck_r) + ' Regular check')
    35000


#Loop Basics
#4
#While
#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, 
# then increment i by one.
i = 5
while i <= 15:
  print(i)
  i += 1

#5 Create a while loop that will count by 2's starting with 0 and 
#ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    print('\n')
    i += 2
#6 Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    print('\n')
    i -= 5
#7 Create a while loop that starts at 2, and displays the number 
#squared on each line while the number is less than 1,000,000. 
#Output should equal:
i = 2 
while i <= 1000000:
    print(i)
    i = i ** 2
#8 Write a loop that uses print to create 100 subtract 5 until you reach
#number 5
i = 100
while i >= 5:
    print(i)
    i-=5

#For Loops
#9 Write some code that prompts the user for a number, 
#then shows a multiplication table up through 10 for that number.

# user input
# i in range (1 - 11) = x *(1-10)
# changed string x to int(x) x i

x = input('enter number')
print(x)
for i in range(1, 11):
      print(f" {x} x {i} = {int(x)*i}")

#10 Create a for loop that uses print to create the output shown below.
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

for x in range(1,10):
    print(x * str(x))

#break and continue

#11 Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the 
#user entered down to 1.
while True:
    number = input('enter posistive number')

    if number.isdigit() == True:
        print('this is a digit')
        if int(number) > 0:
            print('this is positive')
            break
number = int(number)
for x in range(number, 0, -1):
    print(x)
#12 The input function can be used to prompt for input and use that 
#input in your python code. Prompt the user to enter a positive number 
#and write a loop that counts from 0 to that number. 
#(Hints: note that the input function returns a string, so 
#you'll need to convert this to a numeric type.)
while True:
    number = input('Enter a posistive number')

    if number.isdigit() == True:
        print('this is a digit')
        if int(number) > 0:
            print('this is posisitive')
            break
for x in range(int(number + 1)):
    print(x)

#13 Prompt the user for an odd number between 1 and 50. 
#Use a loop and a break statement to continue prompting the user 
#if they enter invalid input. (Hint: use the isdigit method on 
#strings to determine this). Use a loop and the continue statement 
#to output all the odd numbers between 1 and 50, except for the number 
#the user entered.

while True:
    number = input('Enter odd number 1 - 50:  ')
    if number.isdigit() == True:
        print('this is a digit')
        if int(number) % 2 == 1:
            print('this is odd')
            if (int(number) > 1) and (int(number) < 50):
                print('this number is in range')
                break
number = int(number)

for x in range (1, 50):
    if x == number:
        continue
    if x % 2 == 1:
            print(x)

#14 Fizzbuzz
#One of the most common interview questions for entry-level 
# programmers is the FizzBuzz test. Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional 
# logic skills.
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print 
# "FizzBuzz".

for x in range(1, 101):
    if x % 15 == 0:
        print('FizzBuzz')
        continue
    if x % 3 == 0:
        print('Fizz')
        continue
    if x % 5 == 0:
        print('Buzz')
        continue
    print(x)
#15 Display a table of powers.
#Prompt the user to enter an integer
#Display a table of squares and cubes from 1 to the value entered
#Ask if the user wants to continue
#Assume that the user will enter valid data
#Only continue if the user agrees to
    while True:
        number = input("Enter an integer ")
        number = int(number)
    
        for x in range(1, number+1):
            print(f'{x} |{x**2} |{x**3}')
        user_question = input('Would you like to continue? y/n: ')
        if user_question.lower() != 'y':
            break
#Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100
#Display the corresponding letter grade
#Prompt the user to continue
#Assume that the user will enter valid integers for the grades
#The application should only continue if the user agrees to
#Grade Ranges:
#A : 100 - 88
#B : 87 - 80
#C : 79 - 67
#D : 66 - 60
#F : 59 - 0

grade = input ('Enter a grade 0 - 100 ')
grade = int(grade)

if grade >= 88:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 67:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
    

while True:
    grade = input ('Enter a grade 0 - 100 ')
    grade = int(grade)

    if grade >= 88:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 67:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('F')

    user_question = input('Would you like to continue? y/n ')
    if user_question.lower() != 'y':
        break

    
