from db_model import DBReader

def main_login():
    while True:
        username = input("Please enter your user name: ")
        password = input("Please enter your password: ")
        try:
            user_account = DBReader(username, password)
        except:
            print("More than one account with that username.")
            main_login()
        if not user_account.account:
            print("Sorry, Mr. Hacker. That login info is incorrect. Go hack someone else.")
        else:
            print("Your account: \n" + str(user_account.account))
            if input("Would you like to create a user or log out? C/l").lower() == 'c':
                new_user = ''
                new_user += str(input("Enter a user name: "))
                new_user += ',' + str(input("Enter a password: "))
                new_user += ',' + str(input("Enter your favorite color: "))
                new_user += ',' + str(input("Enter your favorite food: "))
                for line in user_account.read_file():
                    if new_user.split(',')[0] == line[0]:
                        print("Sorry, That User Name Is Already Taken.")
                        new_user = None
                        break


                if new_user:
                    user_account.write_to_file(new_user)
                    print("Success! New User Created.")
            else:
                print("Goodbye!")
main_login()