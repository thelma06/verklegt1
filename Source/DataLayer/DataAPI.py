from models.Destination import Destination

class DataAPI:
    
    def __init__(self):
        self.__destinations = []

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


    def add_airplane(self, airplane):
        # first add to file then to private list
        with open("./data/Aircraft.csv", "a+") as aircraft_file:
            name = airplane.get_name()
            model = airplane.get_model()
            producer = airplane.get_producer()
            number_of_seats = airplane.get_number_of_seats()
            aircraft_file.write("{}, {}, {}, {}, \n".format(name, model, producer, number_of_seats))
        aircraft_file.close()

    
      def get_airplane(self):
        if self.__airplane == []:
            airplane_str = ""
            # destinations_str = "{}\t\t {}\t\t {}\t\t {}\t\t {}\t\t {}\n".format("Country", "Airport", "Duration", "Distance", "Contact name", "Contact phone")
            with open("./data/Aicraft.csv", "r") as aircraft_file:
                for line in aircraft_file.readlines():
                    name, model, producer, number_of_seats = line.split(",")
                    # title, genre, length = line.split(",")
                    aircraft_str += "{}, {}, {}, {}, {}, {}".format(name, model, producer, number_of_seats)
                    # videos_str += "{}\t\t {}\t\t {}".format(title, genre, length)
                    # new_video = "{}, {}, {}\n".format(title, genre, length)
                    # self.__videos.append(new_video)
        
        return aircraft_str
        # return self.__videos


