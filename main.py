import csv
import datetime as dt
# creating a class to hold users data temporarily
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date_joined = dt.date.today()


# function to take care of login data input
def login():
    # takes data from user
    uname = input('\nUsername: ')
    pword = input('Password: ')
    # creates an object for the user
    existing_user = User(uname, pword)
    # sends details to login_process
    login_process(existing_user)


# function to take care of the login processes
def login_process(user):
    is_member = False
    # opening the already existing data of users
    with open('Data.csv', 'r', newline='') as f:
        reader = enumerate(csv.reader(f))
        # taking each row of the csv file
        for i, row in reader:
            if i > 0:   # ignoring first row. it's only title
                # checking for details match
                if (user.username == row[0]) and (user.password == row[1]):
                    is_member = True
    if is_member:
        print("Details matched. You've logged in successfully")
    # when details do not match
    else:
        print('Username not found. Please try again.')
        login()


# fxn to take data for signup processes
def signup():
    # taking the data
    print('\nPlease enter your details below')
    uname = input('Username: ')
    pword1 = input('Password: ')
    pword2 = input('Confirm Password: ')
    if pword1 == pword2:
        pword = pword1
        # creating an object for the data
        new_user = User(uname, pword)
        # sending the object to signup processes
        signup_process(new_user)
    else:
        print("Passwords do not match. Please try again.")
        signup()


# function taking care of signup processes
def signup_process(user):
    possible = True
    # opening the data file
    with open('Data.csv', 'r', newline='') as f:
        reader = enumerate(csv.reader(f))
        # taking each row one by one
        for i, row in reader:
            # ignoring the first row. It's the headings
            if i > 0:
                # making sure that no user has same name.
                if user.username == row[0]:
                    print("\nUsername already taken. Please try another one.")
                    possible = False
                    break
                # making it possible to use the username if none already exists
                else:
                    possible = True
    if possible:
        with open('Data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([user.username, user.password, f'{dt.date.today():%d-%m-%Y}'])
            print("\nDetails added successfully!\n")
        start()
    else:
        signup()

def start():
    print("Welcome to my Login system!")
    print("-----------------------------------")
    print("Please type in 'Login' to go to the login screen\nor type in 'Signup' to create an account.")
    choice = input("INPUT: ")
    if choice.lower() == 'signup':
        signup()
    elif choice.lower() == 'login':
        login()
    else:
        print("\nInvalid input. Please try again.")
        start()

start()
