import getpass
class UserInterface:
    username = input("Enter your username : ")
    password = getpass.getpass("Enter your password : ")
    #print(password)

    def __init__(self, username, password):
        self.username = username
        self.password = password
