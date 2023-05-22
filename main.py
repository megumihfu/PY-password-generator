import sys
from PasswordGenerator import PasswordGenerator

if __name__ == "__main__":
    size = int(input("Enter the size needed for your new password : "))
    if size < 8:
        size = int(input("Please retry with a size highter than 8"))
    generator = PasswordGenerator(size) #creation de l'instance
    
    password = generator.password_generator()
    print(password)
    generator.check_password_security()
    print(password)
    generator.final_password()
    print("Password generated : ", password)