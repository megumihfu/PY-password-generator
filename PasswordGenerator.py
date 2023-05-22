import string
import random

class PasswordGenerator:
    def __init__(self, size):
        self.size = size

    def password_size(self):
        self.size = int(input("Enter the size needed for your new password (highter than 8): "))
        if self.size < 8:
            self.size = int(input("Please retry with a size highter than 8"))
        return self.size
    
    def password_generator(self):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        password = random.choices(password, k=self.size)
        return ''.join(password)
    
    def check_password_security(self):
        password = self.password_generator()
        print(password)
        has_digit = False
        has_upper = False
        has_lower = False

        for x in password:
            if x.isdigit():
                has_digit = True
            elif x.islower():
                has_lower = True
            elif x.isupper():
                has_upper = True
            
        if has_digit & has_lower & has_upper:
            print("It's strong enough")
            return True
        else:
            print("It's not strong enough")
            return False
    
    def final_password(self):
        if self.check_password_security() is True:
            pass
        else:
            print("The password generated isn't strong enough for you")
            self.password_generator()
            self.check_password_security()
            self.final_password()

    