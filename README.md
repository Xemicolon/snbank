# Overview

This is a basic banking system. There are 2 files 'staff.txt' & ''customer.txt'.

## Content of staff.txt
Username
Password
Email
Full Name

## Content of customer.txt


## On program run

You are presented with two options and prompted to select any:

### Staff Login
### Close App


## IF THE USER SELECTS STAFF LOGIN
The user will be asked for their username and password, the program will then check the pre-defined staff.txt file (as seen above) and verify that the username and password are correct. If incorrect, user will see an error message and told to try again. 

After user login is successful, a new file will be created to store the user session and staff is presented with the following options: 

### 1 Create new bank account
### 2 Check Account Details
### 3 Logout
## If staff selects Create bank account

Staff should be made to supply the following:

### Account name
### Opening Balance
### Account Type
### Account email

after which 10 digits account number is automatically generated for the customer and details be saved in the empty customer.txt file created above.

After staff completes creating the account, they will see the account number, and then presented with these options again:

### 1 Create new bank account
### 2 Check Account Details
### 3 Logout

If Staff selects check account details, they'll be asked for an account number to fetch the details of the account from the customer.txt file where all our customer details are saved and display it to the staff. They are then presented with these options again:

### 1 Create new bank account
### 2 Check Account Details
### 3 Logout

If staff selects logout above, the user session that was created earlier will be deleted and staff will be returned back to thIS option:
### Staff Login
### Close App


And finally, if staff selects Close App, the program will end.


