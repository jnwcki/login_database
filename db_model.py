class DBReader:

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.account = self.get_user(name, password)

    def read_file(self):
        with open("login_db") as infile:
            return [line.split(',') for line in infile.readlines()]

    def get_user(self, name, password):
        my_read_file = self.read_file()
        print(my_read_file)
        for item in my_read_file:
            if name == item[0]:
                print(item)
                return [line for line in self.read_file() if line[0].lower() == name.lower()]
            else:
                break

    def __repr__(self):
        return str(self.account)

    def write_to_file(self, new_user=None):
        with open("login_db", "a") as outfile:
            outfile.write(new_user)