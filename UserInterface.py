import smtplib
import ssl
from PasswordGenerator import PasswordGenerator

class UserInterface:
    @staticmethod

    def user_size():
        size = int(input("Enter the size needed for your new password : "))
        if size < 8:
            while size < 8:
                size = int(input("Please retry with a size highter than 8 : "))   
        return size

    def interface(self):
        print("Welcome to your Password Generator")
        size = UserInterface.user_size()
        password = ""
        generator = PasswordGenerator(size, password) #creation de l'instance
        generator.password_generator() 
        password = generator.final_password()
        print("Password generated : ", password)
        UserInterface.send_password(password)
        return ''.join(password)

    def send_password(password):
        response = input("Do you want us to send you the password by email ? [y/n] : ")
        if response == "y":
            email = input("Please enter your email : ")
            print("Your email adress is : ", email)
            smtp_address = 'smtp.gmail.com'
            smtp_port = 465

            email_address = 'testfortesting050@gmail.com'
            email_password = 'xoxktwiafhexvxib'
            email_receiver = email

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
                server.login(email_address, email_password)
                message = "Subject : Your Generated Password\n\nThere is the password you generated : " + password + "\nThank you for using our software !"
                server.sendmail(email_address, email_receiver, message)
