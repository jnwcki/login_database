from db_model import DBReader


while True:
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    user_account = DBReader(username, password)
    if not user_account.account:
        print("Sorry, Mr. Hacker. That login info is incorrect. Go hack someone else.")
    else:
        print("Your account: \n" + str(user_account.account))
        if input("Would you like to create a user or log out? C/l").lower() == 'c':
            new_user = ''
            new_user += str(input("Enter a user name: "))
            new_user += ',' + str(input("Enter a password: "))
            new_user += ',' + str(input("Enter your favorite color: "))
            new_user += ',' + str(input("Enter your favorite food: ") + '\n')
            for line in DBReader().read_file():
                if new_user.split(',')[0] == line[0]:
                    print("Sorry, That User Name Is Already Taken.")
                    new_user = None
                    break


            if new_user:
                DBReader().write_to_file(new_user)
                print("Success! New User Created.")
        else:
            print("Goodbye!")
