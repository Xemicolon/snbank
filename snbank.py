from bankfunc import login, logout, loginchoice, bankchoice, createAccount, accountType, generateAcct, fetchAccountDetails
import random

# Main program
while True:
    print(f'\n\t\tWELCOME TO SNBANK')
    login_choice = int(input(
        f'\n\tPlease select any of the options below by inputing 1 or 2\n\t1 - Staff Login\n\t2 - Close app\n\n\tChoice: '))

    loginchoice(login_choice)

    # end app
    if login_choice == 2:
        print(f'\n\tThank you for banking with us! 👍\n')
        break
    #  login
    else:
        username = input(f'Enter your username: ')
        password = input(f'Enter your password: ')
        login(username, password)

    # Banking system

    while True:
        bank_choice = int(input(
            f'\n1 - Create a new bank account\n2 - Check Account Details\n3 - Logout\nChoice: '))
        bankchoice(bank_choice)
        if bank_choice == 1:
            print(f'I\'m going to need some information from you. Let\'s proceed...')
            account_name = input(f'Enter name of bank account: ')
            while True:
                try:
                    opening_balance = int(
                        float(input(f'How much do you want to open this account with: ')))
                    opening_balance = '{:.2f}'.format(opening_balance)
                except ValueError:
                    print(
                        f'Invalid input for opening balance! Make sure you enter numbers')
                    continue
                else:
                    break
            account_type = int(input(
                f'Select account type below using 1 or 2\n\t1 - Savings\n\t2 - Current\nChoice: '))
            accountType(account_type)
            account_email = input(
                f'Enter your email to be associated with your account: ')
            account_number = ''.join(random.choices('0123456789', k=10))
            createAccount(username, account_name, opening_balance,
                          account_type, account_number, account_email)
            continue

        if bank_choice == 2:
            account_number = (input(
                f'Please enter account number to get account details: \n'))
            fetchAccountDetails(account_number)
            continue

        if bank_choice == 3:
            logout()
            break
