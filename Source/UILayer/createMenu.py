from UILayer.mainMenu import Main_menu

class Create_Menu:

    def create_menu(self):
        action = ""
        while(action != "q"):
            print("*********************************************")
            print("*                                           *")
            print("*                  CREATE                   *")
            print("*                                           *")
            print("*********************************************")
            print("")
            print("1: Create employee")
            print("2: Create destination")
            print("3: Create flight")
            print("4: Create voyage")
            print("b: Back")
            print("q: Quit")

            action = input("Choose an option: ").lower()

            if action == "b":
                ui = Main_menu()
                ui.main_menu()