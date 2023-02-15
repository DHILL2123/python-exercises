currentbal = 0
debitbal = 0
creditbal = 0
debitbal = currentbal - debitbal
user_input = 0


while user_input == '1' or '2' or '3' or '4':
    print("~~~ Welcome to your terminal checkbook! ~~~")
    print('\n')
    print('What would you like to do?')
    print('\n')
    print('1) view current balance')
    print('2) record a debit(withdraw)')
    print('3) record a credit(deposit)')
    print('4) exit')
    print('\n')
    
    user_input = input('Please make a selection: ')
    print('\n')
    
    if user_input == '1':
        print(f'Your current balance is {currentbal}')
        print('\n')
        
    elif user_input == '2':
            debit_input = input('How much is the debit? ')
            print('\n')
            currentbal = currentbal - int(debit_input)
            print(f'Your current balance is {currentbal}')
            print('\n')
    
    elif user_input == '3':
            deposit_input = input('How much is the deposit? ')
            print('\n')
            currentbal = currentbal + int(deposit_input)
            print(f'Your current balance is {currentbal}')
            print('\n')
    
    elif user_input == '4':
            print('Thank you have a nice day!')
            print('\n')
    
    else:
        print('Incorrect response, please try again')
        print('\n')
        
        
    
        
        
        





#print(f'Your current balance is {currentbal}.')

    
    #if user_input == '2':
        #debit_input = input('How much is the debit? ')
        #currentbal = currentbal - int(debit_input)
        #print(f'Your current balance is {currentbal}')
     