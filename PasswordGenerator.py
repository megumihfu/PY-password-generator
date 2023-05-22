import string
import random

class PasswordGenerator:
    def __init__(self, size, password):
        self.size = size
        self.password = password

    def password_size(self):
        self.size = int(input("Enter the size needed for your new password (highter than 8): "))
        if self.size < 8:
            self.size = int(input("Please retry with a size highter than 8"))
        return self.size
    
    def password_generator(self):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        self.password = random.choices(password, k=self.size)
        #print("dans password_generator : ", ''.join(self.password))
        return ''.join(self.password)
    
    def check_password_security(self):
        #print("dans check_security : ", ''.join(self.password))
        has_digit = False
        has_upper = False
        has_lower = False

        for x in self.password:
            if x.isdigit():
                has_digit = True
            elif x.islower():
                has_lower = True
            elif x.isupper():
                has_upper = True
            
        if has_digit & has_lower & has_upper:
            #print("The password generated is strong enough")
            return True
        else:
            print("The password generated isn't strong enough")
            return False
    
    def final_password(self):
        password = self.check_password_security()
        if password == True:
            #print("pas besoin de regenérer un nouveau mdp")
            return ''.join(self.password)
        else:
            #print("The password generated isn't strong enough for you")
            self.password_generator()
            self.check_password_security()
            self.final_password()

    