import sys
from PasswordGenerator import PasswordGenerator

if __name__ == "__main__":
    print("Hello word !")
    size = int(input("Enter the size needed for your new password : "))
    password = PasswordGenerator.password_generator(size)
    print("Password generated : ", password)