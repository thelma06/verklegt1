#Just a test file

from ModuleClasses import Destination


class IOAPI():

    def __init__(self):
        self.__destination = []


    def add_destination(self,destination):
        # first add to file then to private list
        with open("Destination.csv", "a+") as destination_file:
            ids = destination.get_id()
            place = destination.get_destination()
            destination_file.write("{},{}\n".format(ids, place))
            print(ids,place)


   # update destination
    def update_destination(self):
        if self.__destination == []:
            with open("Destination.csv", "r") as destination_file:
                for line in destination_file.readlines():
                    ids, place = line.split(",")
                    new_destination = Destination(ids,place)
                    self.__destination.append(new_destination)  
                    print(new_destination)
        
        return self.__destination