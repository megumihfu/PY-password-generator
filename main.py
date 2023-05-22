import sys
from PasswordGenerator import PasswordGenerator

if __name__ == "__main__":
    size = int(input("Enter the size needed for your new password : "))
    if size < 8:
        size = int(input("Please retry with a size highter than 8"))
    
    password = ""
    generator = PasswordGenerator(size, password) #creation de l'instance
    
    generator.password_generator()
    final_password = generator.final_password()
    print("Password generated : ", final_password)