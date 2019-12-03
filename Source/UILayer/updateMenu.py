# from UILayer.mainMenu import Main_menu

class Update_Menu:

    def update_menu(self):
        action = ""
        while(action != "b"):
            print("")
            print("*********************************************")
            print("*                                           *")
            print("*                 UPDATE                    *")
            print("*                                           *")
            print("*********************************************")
            print("")
            print("1: Update employee")
            print("2: Update destination")
            print("3: Update flight")
            print("b: Back")
            # print("q: Quit")

            action = input("Choose an option: ").lower()

            # if action == "b":
            #     ui = Main_menu()
            #     ui.main_menu()
            
            # else:
            #     action = "q"