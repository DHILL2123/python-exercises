#1
#Create a file named function_exercises.py for this exercise. 
#After creating each function specified below, 
# write the necessary code in 
#order to test your function.

#Define a function named is_two. 
#It should accept one input and return True if 
#the passed input is either the number or the string 2, 
# False otherwise.

def is_two(num):
    return num == 2 or num == '2'

print(is_two(2))

#2
#Define a function named is_vowel. It should return True if 
#the passed string is a vowel, False otherwise.

def is_vowel(str):
    if str in ('a','A', 'E','e', 'I','i', 'O','o','U', 'u'):
        return(True)
    else:
        return(False)

print(is_vowel('x'))

#3
#Define a function named is_consonant. It should return 
# True if the passed 
#string is a consonant, 
#False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(str):
    if str in ('a','A', 'E','e', 'I','i', 'O','o','U', 'u'):
            return(False)
    else: 
        return(True)

print(is_consonant('d'))

#4
#Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of 
#the word if the word starts with a consonant.

def my_word(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word
       
print(my_word('soup'))

#5
#Define a function named calculate_tip
#It should accept a tip percentage
#(a number between 0 and 1) and the bill total,
#And return the amount to tip.

def calculate_tip(my_bill, my_tip=.2):
    return my_bill * my_tip

print(calculate_tip(20, .10))

#6
#Define a function named calculate_tip
#It should accept a tip percentage
#(a number between 0 and 1) and the bill total,
#and return the amount of tip

def apply_discount(orig_price, disc_prcnt=0):
    
    discount_value = orig_price * disc_prcnt
    
    new_price = orig_price - discount_value
    
    return new_price

print(apply_discount(20, .10))

#7
#Define a function named handle_commas
#It should accept a string that is a number that contains
#commmas in it as input,
#and return a number as output.

def remove_commas(string_num):
    num = string_num.replace(',', '')
    return int(num)

print(remove_commas('8,000,000,000,000'))

#8
#Define a function named get_letter_grade
#It should accept a number and return the letter grade
#associated with that number (A-F)

def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'
    else:
        return 'F'
    
print(get_letter_grade(92))

#9
#Define a function named remove_vowels that accepts a 
#string and returns a string with all the vowels removed

def remove_vowels(words):
    no_vowels = ''
    for n in words:
        if is_vowel(n):
            continue
        else:
            no_vowels += n
    return no_vowels
    
print(remove_vowels('Hello there good work'))

#10
#Define a function named normalize_name
#It should accept a string and return a valid python identifier
#steps I want to take
#make lowercase,
#string method: .lower()
#remove whitespace,
#string method .strip()
#establish valid identifier
#in 'abcdefghijklmnopqrstuvwxyz1234567890'
#cheat: 'abcdefg'.isidentifier()

def normalize_name(my_var):
    my_new_var = ''
    
    for let in my_var:
        if let.isdigit() or let.isalpha() or let == '':
            my_new_var += let
    return my_new_var.strip().lower().replace('','_')

print(normalize_name('WHAT IS GOING ON'))

#11
#Write a function named cumulative_sum that accepts a list of numbers and returns a list
#that is the cumulative sum of the numbers in the list
#cumulative_sum ([1,1,1]) returns [1,2,3]
#cumulative_sum([1,2,3,4]) returns [1,3,6,10]

def cumulative_sum(some_list):
    counting_sum = 0
    new_list = []
    
    for i in some_list:
        counting_sum += i
        new_list.append(counting_sum)
    return new_list
    
    
print(cumulative_sum([1, 2, 3, 4, 5]))