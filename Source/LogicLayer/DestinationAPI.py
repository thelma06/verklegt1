from DataLayer.DataAPI import DataAPI

class DestinationAPI:
    def __init__(self):
        self.__destination_repo = DataAPI()

    def add_destination(self, destination):
        if self.is_valid_destination(destination):
            self.__destination_repo.add_destination(destination)
    
    def is_valid_destination(self, destination):
        #here should be some code to 
        #validate the video
        return True

    def get_destinations(self):
        return self.__destination_repo.get_destinations()

    def get_destinations_by_country(self, country):
        pass