

class Main_menu:

    #def __init__(self):

    def main_menu(self):
        action = ""
        while(action != "q"):
            print("*********************************************")
            print("*                                           *")
            print("*            WELCOME TO NaN-AIR!            *")
            print("*                                           *")
            print("*********************************************")
            print("")
            print("1: Create")
            print("2: Get")
            print("3: Update")
            print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()