from UILayer.createMenu import Create_Menu
from UILayer.getMenu import Get_Menu


class Main_menu:

    #def __init__(self):

    def main_menu(self):
        action = ""
        while(action != "q"):
            print("")
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

            if action == "1":
                ui = Create_Menu()
                ui.create_menu()
            elif action == "2":
                ui = Get_Menu()
                ui.get_menu()
            elif action == "3":
                ui = 