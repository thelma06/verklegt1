
class Plane:

    def __init__(self, name = "", model = "", producer = "", number_of_seats = ""):
        #self.plane_ID = plane_ID
        self.name = name
        self.model = model
        self.producer = producer
        self.number_of_seats = number_of_seats
        #self.pilot_ID = pilot_it

    def get_name(self):
        return str(self.name)

    def get_model(self):
        return str(self.model)

    def get_producer(self):
        return str(self.producer)

    def get_number_of_seats(self):
        return str(self.number_of_seats)

        