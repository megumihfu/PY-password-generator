import string
import random

class PasswordGenerator:
    #size = int(input("Enter password's size you need : "))
    
    def __init__(self, size):
        self.size = size
    
    def password_generator(size):
        password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))
        return password
    