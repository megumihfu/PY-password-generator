import os
from PasswordGenerator import PasswordGenerator
from UserInterface import UserInterface

if __name__ == "__main__":
    
    generator = UserInterface()
    generator.interface()
    
    while 1:
        retry = input("Do you want to regenerate another password ? [y/n] : ")
        if retry == "y":
            os.system('clear')
            generator.interface()
        else:
            os.system('clear')
            exit(1)
