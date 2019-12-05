from models.Destination import Destination

class DataAPI:
    
    def __init__(self):
        self.__destinations = []
        self.__employee = []

    def add_destination(self, destination):
        # first add to file then to private list
        with open("./data/destinations.txt", "a+") as destinations_file:
            country = destination.get_country()
            airport = destination.get_airport()
            duration = destination.get_duration()
            distance = destination.get_distance()
            contact_name = destination.get_contact_name()
            contact_phone = destination.get_contact_phone()
            destinations_file.write("{}, {}, {}, {}, {}, {}\n".format(country, airport, duration, distance, contact_name, contact_phone))
        destinations_file.close()

    def get_destinations(self):
        if self.__destinations == []:
            destinations_str = ""
            # destinations_str = "{}\t\t {}\t\t {}\t\t {}\t\t {}\t\t {}\n".format("Country", "Airport", "Duration", "Distance", "Contact name", "Contact phone")
            with open("./data/destinations.txt", "r") as destination_file:
                for line in destination_file.readlines():
                    country, airport, duration, distance, contact_name, contact_phone = line.split(",")
                    # title, genre, length = line.split(",")
                    destinations_str += "{}, {}, {}, {}, {}, {}".format(country, airport, duration, distance, contact_name, contact_phone)
                    # videos_str += "{}\t\t {}\t\t {}".format(title, genre, length)
                    # new_video = "{}, {}, {}\n".format(title, genre, length)
                    # self.__videos.append(new_video)
        
        return destinations_str
        # return self.__videos

    def add_employee(self, employee):
        # first add to file then to private list
        with open("./data/employee.txt", "a+") as employee_file:
            name_str = employee.get_name()
            so_str = employee.get_so()
            address_str = employee.get_address()
            home_phone_str = employee.get_home_phone()
            cell_phone_str = employee.get_cell_phone()
            email_str = employee.get_email()
            employee_file.write("{}, {}, {}, {}, {}, {}\n".format(name_str, so_str, address_str, home_phone_str, cell_phone_str, email_str))
        employee_file.close()

    def get_employee(self):
        if self.__employee == []:
            employee_str = ""
            # destinations_str = "{}\t\t {}\t\t {}\t\t {}\t\t {}\t\t {}\n".format("Country", "Airport", "Duration", "Distance", "Contact name", "Contact phone")
            with open("./data/employee.txt", "r") as employee_file:
                for line in employee_file.readlines():
                    name_str, so_str, address_str, home_phone_str, cell_phone_str, email_str = line.split(",")
                    # title, genre, length = line.split(",")
                    employee_str += "{}, {}, {}, {}, {}, {}".format(name_str, so_str, address_str, home_phone_str, cell_phone_str, email_str)
                    # videos_str += "{}\t\t {}\t\t {}".format(title, genre, length)
                    # new_video = "{}, {}, {}\n".format(title, genre, length)
                    # self.__videos.append(new_video)
        
        return employee_str
        # return self.__videos