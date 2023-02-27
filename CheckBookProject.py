with open('checkbook.rtf')as f:
    data = f.read()
    f.close()


user_input = 1,2,3,4

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
        bal = str(currentbal)
        print(f'Your current balance is {bal}')
        print('\n')
    
   
        
    elif user_input == '2':
            debit_input = input('How much is the debit? ')
            print('\n')
            currentbal = int(currentbal) - int(debit_input)
            print(f'Your current balance is {currentbal}')
            print('\n')
    
    elif user_input == '3':
            deposit_input = input('How much is the deposit? ')
            print('\n')
            currentbal = int(currentbal) + int(deposit_input)
            print(f'Your current balance is {currentbal}')
            print('\n')
    
    elif user_input == '4':
        print('Thank you have a nice day!')

        break
    
    else:
        
        print('Incorrect response, please try again ')
        print('\n')
    