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
            print("")

            action = input("Choose an option: ").lower()

            if action == "2":
                self.update_destination()
            
            # else:
            #     action = "q"

    def update_employee(self):
        pass

    def update_destination_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*            UPDATE DESTINATION             *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def update_destination(self):
        self.update_destination_header()
        print("   **    Please insert Airport name     **   ")
        print("")
        airport_name_str = input("Airport name: ")
        ''' Hér þarf að gera ráð fyrir kóðanum til að kalla í 
            API sem síðan sækir gögnin niður í data layer og
            skilar þeim aftur.'''
        self.update_destination_header()
        print("     **    Destination information    **     ")
        print("")
        print("Country: " + "Grænland") #Breyturnar eru ekki tilbúnar
        print("Airport: " + "Nuuk") #Breyturnar eru ekki tilbúnar
        print("Flight duration: " + "02:30") #Breyturnar eru ekki tilbúnar
        print("Distance from Iceland: " + "1.000 " + "km.") #Breyturnar eru ekki tilbúnar
        print("Contact name: " + "Chuck Norris") #Breyturnar eru ekki tilbúnar
        print("Contact emergency phone number: " + "+11 444-5555") #Breyturnar eru ekki tilbúnar
        print("")
        correct_str = input("Is this the correct Airport? (Y/N): ").lower()

        if correct_str == "y":
            self.update_destination_header()
            print("*********************************************")
            print("    ** What information would you like to    ")
            print("                 change? **                  ")
            print("")
            print("1: Contact name")
            print("2: Contact emergency phone number")
            print("b: Back")
            print("")
            action = input("Choose an option: ").lower()

    def update_flight(self):
        pass