# from UILayer.mainMenu import Main_menu

class Get_Menu:

    def __init__(self):
        self.get_employee_lst = []
        self.get_destination_lst = []
        self.get_flight_info_lst = []
        self.get_flight_schedule_lst = []
        self.get_employee_schedule_lst = []

    def get_menu(self):
        action = ""
        while(action != "b"):
            print("")
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
            print("5: Get employee schedule")
            print("b: Back")
            print("")
            # print("q: Quit")

            action = input("Choose an option: ").lower()

            if action == "2":
                self.__get_destination()
    
    def __get_employee_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*               GET EMPLOYEE                *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __get_destination_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*              GET DESTINATION              *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __get_flight_information_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*          GET FLIGHT INFORMATION           *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __get_flight_schedule_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*            GET FLIGHT SCHEDULE            *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __get_employee_schedule_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*         GET EMPLOYEE INFORMATION          *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __get_employee(self):
        self.__get_employee_header()
        pass

    def __get_destination(self):
        self.__get_destination_header()
        print("   **    Please insert Airport name     **   ")
        print("")
        airport_name_str = input("Airport name: ")
        ''' Hér kæmi þá virknin sem þarf til að kalla í API, sem
            síðan kallar áfram í data layer til að sækja upplýsingar
            um þetta destination.'''
        ''' Hér kæmi virknin sem þarf til að birta gögnin sem logic
            layer API skilar upp.'''
        self.__get_destination_header()
        print("     **    Destination information    **     ")
        print("")
        print("Country: " + "Grænland") #Breyturnar eru ekki tilbúnar
        print("Airport: " + "Nuuk") #Breyturnar eru ekki tilbúnar
        print("Flight duration: " + "02:30") #Breyturnar eru ekki tilbúnar
        print("Distance from Iceland: " + "1.000 " + "km.") #Breyturnar eru ekki tilbúnar
        print("Contact name: " + "Chuck Norris") #Breyturnar eru ekki tilbúnar
        print("Contact emergency phone number: " + "+11 444-5555") #Breyturnar eru ekki tilbúnar
        print("")
        print("**   Press enter to return to main menu    **")


    def __get_flight_information(self):
        self.__get_flight_information_header()
        pass

    def __get_flight_schedule(self):
        self.__get_flight_schedule_header()
        pass

    def __get_employee_schedule(self):
        self.__get_employee_schedule_header()
        pass