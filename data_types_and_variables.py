##5. You have rented some movies for your kids:

#The Little Mermaid for 3 days 
#Brother Bear for 5 days
#Hercules for 1 day
#If the daily fee to rent a movie is 3 dollars, how much will you have to pay?
little_mermaid = 3
brother_bear = 5
hercules = 1
daily_fee = 3
little_mermaid * daily_fee + brother_bear * daily_fee + hercules * daily_fee
27

#6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

#They pay you the following hourly rates:
#Google: 400 dollars
#Amazon: 380 dollars
#Facebook: 350 dollars
#This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_rate = 400
amazon_rate = 380
facebook_rate = 350
fb_hrs = 10
go_hrs = 6
amaz_hrs = 4
google_rate * go_hrs + amazon_rate * amaz_hrs + facebook_rate * fb_hrs
7420

#How much will you receive in payment for this week?
# 10 * 350 + 6 * 400 + 4 * 380 = 7420

#7. A student can be enrolled to a class only if the class is not full 
#and the class schedule does not conflict with her current schedule.

enrolled_class = True
class_not_full = False
class_schedule_conflict = False

class_not_full == class_schedule_conflict
print(enrolled_class)

#8. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
#Premium members do not need to buy a specific amount of products.

regular_member_buy_two = True
offer_expired = False
premium_members_buy_two = False
product_offer = offer_expired != regular_member_buy_two and premium_members_buy_two != regular_member_buy_two
print(product_offer)

offer_expired != regular_member_buy_two 
print(product_offer)

premium_members_buy_two != regular_member_buy_two
print(product_offer)



#9. Continue working in the data_types_and_variables.py file. Use the following code to follow the instructions below:


username = 'codeup'
password = 'notastrongpassword'

password = 'jackrabbit'
username = 'BuggsBunny'

min_password_length = len(password)>= 5
max_username_length = len(username)<= 20

password_username_unique = password != username
valid_credentials = min_password_length and max_username_length and password_username_unique
print(valid_credentials)
#Create a variable that holds a boolean value for each of the following conditions:

#The password must be at least 5 characters
#The username must be no more than 20 characters
#The password must not be the same as the username
#Bonus Neither the username or password can start or end with whitespace