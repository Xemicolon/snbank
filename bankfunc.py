import os
import random
from datetime import datetime
import json


def createAccount(username, account_name, opening_balance, account_type, account_number, account_email):
    customer_info = []
    customer_details = {
        username: [
            {
                'Account Name': account_name.title(),
                'Account Number': account_number,
                'Opening Balance': opening_balance,
                'Account Type': account_type,
                'Account Email': account_email
            },
        ],
    }

    if os.stat('customer.txt').st_size == 0:
        customer_info.append(customer_details)
        with open('customer.txt', 'w') as customer:
            json.dump(customer_info, customer)
        customer_name = customer_details[username][0]['Account Name']
        customer_account_number = customer_details[username][0]['Account Number']
        print(
            f'\nNew bank account created. Details below\n\nAccount name: {customer_name}\nAccount Number:{customer_account_number}')
    else:
        with open('customer.txt') as customer:
            customer_info = json.load(customer)
        customer_info.append(customer_details)
        with open('customer.txt', 'w') as customer:
            json.dump(customer_info, customer)
        customer_name = customer_details[username][0]['Account Name']
        customer_account_number = customer_details[username][0]['Account Number']
        print(
            f'New bank account created. Details below\n\nAccount name: {customer_name}\nAccount Number: {customer_account_number}')


def fetchAccountDetails(account_number):
    check_account = {
        'Account Number': account_number
    }
    with open('customer.txt') as customer:
        customer_info = json.load(customer)
        for user_data in customer_info:
            for user_data_key in user_data.keys():
                for user_details in user_data[user_data_key]:
                    if check_account['Account Number'] in user_details.values():
                        for key, value in user_details.items():
                            print(f'{key} - {value}')


def login(username, password):
    # check if details matches staff.txt file
    with open('staff.txt', 'r') as staff:
        staff_details = json.load(staff)
        # check if the username and password matches details in staff.txt
    while (username != staff_details['Staff']['Username']) or (password != staff_details['Staff']['Password']):
        print(f'Incorrect username or password!')
        username = input(f'Enter your username: ')
        password = input(f'Enter your password: ')
    login_time = datetime.now()
    login_time = login_time.strftime("%m/%d/%Y at %H:%M %p")

    # store user's
    session = {
        'User': username,
        'Time of Login': login_time
    }

    # store the user's active session
    with open('session.txt', 'w') as user_session:
        json.dump(session, user_session, indent=2)

    print(f'\n\tHello {username} 😉, welcome to SNBANK. What do you want to do today?\n\n\tUse 1, 2 or 3 to select the options below')


def loginchoice(login_choice):
    while (login_choice != 1) and (login_choice != 2):
        login_choice = int(input(
            f'\n\tInvalid input! Enter 1 or 2:\n\t1 - Staff Login\n\t2 - Close app\n\n\tChoice: '))


def bankchoice(bank_choice):
    while (bank_choice != 1) and (bank_choice != 2) and (bank_choice != 3):
        bank_choice = input(
            f'Invalid input! Enter 1, 2 or 3 below\n1 - Create a new bank account\n2 - Check Account Details\n3 - Logout')


def accountType(account_type):
    while (account_type != 1) and (account_type != 2):
        account_type = int(input(
            f'Invalid input! Select account type below using 1 or 2\n\t1 - Savings\n\t2 - Current\nChoice: '))
        if account_type == 1:
            account_type = 'Savings'
        elif account_type == 2:
            account_type = 'Current'
        else:
            continue
        print(f'Account Type: {account_type} account')


def logout():
    os.remove('session.txt')
    print(f'\nYou have successfully logged out of SNBANK')
