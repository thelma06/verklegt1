# from UILayer.mainMenu import Main_menu

class Create_Menu:

    def create_menu(self):
        action = ""
        while(action != "b"):
            print("")
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
            # print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()

            if action == "1":
                self.create_employee()
            elif action == "2":
                self.create_destination()

    def create_employee(self):
        # action2 = ""
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*              CREATE EMPLOYEE              *")
        print("*                                           *")
        print("*********************************************")
        print("")
        print("**  Please fill in the information below   **")
        print("")
        name_str = input("Name: ")
        DOB_str = input("Date of birth (dd/mm/yyyy): ")
        address_str = input("Address: ")
        home_phone_str = input("Home phone: ")
        mobile_phone_str = input("Mobile phone: ")
        email_str = input("E-mail: ")
        occupation_str = input("Occupation: ")
        print("")
        correct = input("Is this information correct? (Y/N)").lower()

        if correct == "y":
            print("")
            print("*********************************************")
            print("*                                           *")
            print("*                  SUCCESS                  *")
            print("*                                           *")
            print("*********************************************")
            print("")
            ''' Hér þarf að kalla í API niður í logic layer þar sem inputið
                er sett í rétt format áður en það fer í data layer til 
                skráningar.'''
            print("**   Press enter to return to main menu    **")
        if correct == "n":
            self.create_employee()
    
    def create_destination(self):
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*            CREATE DESTINATION             *")
        print("*                                           *")
        print("*********************************************")
        print("")
        print("**  Please fill in the information below   **")
        print("")
        country_str = input("Country: ")
        airport_str = input("Airport: ")
        duration_str = input("Flight duration (hh:mm): ")
        distance_str = input("Distance from Iceland (km): ")
        contact_name_str = input("Contact name: ")
        contact_phone_nr_str = input("Contact emergency phone number: ")
        print("")
        correct = input("Is this information correct? (Y/N)").lower()

        if correct == "y":
            print("")
            print("*********************************************")
            print("*                                           *")
            print("*                  SUCCESS                  *")
            print("*                                           *")
            print("*********************************************")
            print("")
            ''' Hér þarf að kalla í API niður í logic layer þar sem inputið
                er sett í rétt format áður en það fer í data layer til 
                skráningar.'''
            print("**   Press enter to return to main menu    **")
        if correct == "n":
            self.create_destination()