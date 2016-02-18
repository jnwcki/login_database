from db_model import DBReader


class Main:
    def __init__(self, username=None):
        pass

while True:
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    user_account = DBReader(username, password)
    if not user_account.account:
        print("Sorry, Mr. Hacker. That login info is incorrect. Go hack someone else.")
    else:
        print("Your account: \n" + str(user_account))
        if input("Would you like to create a user or log out? C/l").lower() == 'c':
            new_user = ''
            new_user += '\n' + str(input("Enter a user name: "))
            new_user += ',' + str(input("Enter a password: "))
            new_user += ',' + str(input("Enter your favorite color: "))
            new_user += ',' + str(input("Enter your favorite food: "))
            DBReader().write_to_file(new_user)
            break
        else:
            print("Goodbye!")
