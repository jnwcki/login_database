class DBReader:

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.account = self.get_user(name, password)
        self.user_data = None

    def read_file(self, input=None):
        with open("login_db") as infile:
            return [line.split(',') for line in infile.readlines()]

    def filter_by_name(self, name):
            return [line for line in self.read_file() if line[0].lower() == name.lower()]

    def get_by_name(self, name):
        results = self.filter_by_name(name)
        if len(results) > 1:
            raise Exception("Found more than one record for {}".format(name))

    def get_user(self, name, password):
        self.get_by_name(name)
        return [line for line in self.read_file() if line[0].lower() == name.lower() and line[1] == password]

    def __repr__(self):
        return str(self.account)

    def write_to_file(self, new_user=None):

        with open("login_db", "a") as outfile:
            outfile.write('\n' + new_user)
