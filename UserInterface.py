from PasswordGenerator import PasswordGenerator

class UserInterface:
    @staticmethod
    #password = getpass.getpass("Enter your password : ")

    def user_size():
        size = int(input("Enter the size needed for your new password : "))
        if size < 8:
            while size < 8:
                size = int(input("Please retry with a size highter than 8 : "))   
        return size

    def interface(self):
        print("Welcome to your Password Generator")
        size = UserInterface().user_size()
        password = ""
        generator = PasswordGenerator(size, password) #creation de l'instance
        generator.password_generator() 
        password = generator.final_password()
        print("Password generated : ", password)
        return ''.join(password)

    def send_password():
        response = input("Do you want us to send you the password by email ? [y/n] : ")
        if response == "y":
            email = input("Please enter your email : ")
            

