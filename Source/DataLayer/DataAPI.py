from models.Destination import Destination
import csv

class DataAPI:
    
    def __init__(self):
        self.__destinations = []

    def add_destination(self, destination):
        country = destination.get_country()
        airport = destination.get_airport()
        duration = destination.get_duration()
        distance = destination.get_distance()
        contact_name = destination.get_contact_name()
        contact_phone = destination.get_contact_phone()
        with open("./data/destinations.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['country', 'airport', 'duration', 'distance', 'contact_name', 'contact_phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'country': country, 'airport': airport, 'duration': duration, 'distance': distance, 'contact_name': contact_name, 'contact_phone': contact_phone})
        csv_file.close()

    def get_destinations(self):
        if self.__destinations == []:
            destinations_str = ""
            with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['country'] + ', ' + row['airport'] + ', ' + row['duration'] + ', ' + row['distance'] + ', ' + row['contact_name'] + ', ' + row['contact_phone'])