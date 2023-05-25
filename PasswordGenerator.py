import string
import random

class PasswordGenerator:
    def __init__(self, size, password):
        self.size = size
        self.password = password
    
    def password_generator(self):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        self.password = random.choices(password, k=self.size)
        return ''.join(self.password)
    
    def check_password_security(self):
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
            return True
        
        else:
            return False
    
    def final_password(self):
        if self.check_password_security():
            return ''.join(self.password)
        else:
            self.password = self.password_generator()
            return self.final_password() 

    