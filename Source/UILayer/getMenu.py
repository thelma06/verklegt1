from UILayer.mainMenu import Main_menu

class Get_Menu:

    def get_menu(self):
        action = ""
        while(action != "q"):
            print("*********************************************")
            print("*                                           *")
            print("*                   GET                     *")
            print("*                                           *")
            print("*********************************************")
            print("")
            print("1: Get employee")
            print("2: Get destination")
            print("3: Get flight information")
            print("4: Get flight schedule")
            print("4: Get employee schedule")
            print("b: Back")
            print("q: Quit")

            action = input("Choose an option: ").lower()

            if action == "b":
                ui = Main_menu()
                ui.main_menu()