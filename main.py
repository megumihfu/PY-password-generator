import os
from PasswordGenerator import PasswordGenerator
from UserInterface import UserInterface

if __name__ == "__main__":
    #size = int(input("Enter the size needed for your new password : "))
    #if size < 8:
    #    while size < 8:
    #        size = int(input("Please retry with a size highter than 8 : "))
    
    #password = ""
    #generator = PasswordGenerator(size, password) #creation de l'instance
    
    #generator.password_generator() #tester de mettre final_password = ici plutot
    #password = generator.final_password()
    #print("Password generated : ", password)

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
