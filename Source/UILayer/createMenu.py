# from UILayer.mainMenu import Main_menu
from LogicLayer.DestinationAPI import DestinationAPI
from models.Destination import Destination

class Create_Menu:

    def __init__(self):
        self.__destination_service = DestinationAPI()
        # self.create_employee_lst = []
        # self.create_destination_lst = []
        # self.create_flight_lst = []
        # self.create_voyage_lst = []

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
                self.__create_employee()
            elif action == "2":
                self.__create_destination()

    def __success_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*                  SUCCESS                  *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __create_employee_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*              CREATE EMPLOYEE              *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __create_destination_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*            CREATE DESTINATION             *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __create_flight_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*               CREATE FLIGHT               *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __create_voyage_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*               CREATE VOYAGE               *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __create_employee(self):
        # action2 = ""
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
        self.__create_employee_header()
        print("**  Please fill in the information below   **")
        print("")
        name_str = input("Name: ")
        DOB_str = input("Date of birth (dd/mm/yyyy): ")
        address_str = input("Address: ")
        home_phone_str = input("Home phone: ")
        mobile_phone_str = input("Mobile phone: ")
        email_str = input("E-mail: ")
        occupation_str = input("Occupation: ")
        airplane_license_str = inptu("Airplane license: ")
        print("")
        correct = input("Is this information correct? (Y/N)").lower()

        if correct == "y":
            self.__success_header()
            ''' Hér þarf að kalla í API niður í logic layer þar sem inputið
                er sett í rétt format áður en það fer í data layer til 
                skráningar.'''
            print("**   Press enter to return to main menu    **")
        if correct == "n":
            self.__create_employee()
    
    def __create_destination(self):
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
        self.__create_destination_header()
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
            self.__success_header()
            new_destination = Destination(country_str, airport_str, duration_str, distance_str, contact_name_str, contact_phone_nr_str)
            self.__destination_service.add_destination(new_destination)
            ''' Hér þarf að kalla í API niður í logic layer þar sem inputið
                er sett í rétt format áður en það fer í data layer til 
                skráningar.'''
            print("**   Press enter to return to main menu    **")
        if correct == "n":
            self.__create_destination()

    def __create_flight(self):
        self.__create_flight_header()
        pass

    def __create_voyage(self):
        self.__create_voyage_header()
        pass