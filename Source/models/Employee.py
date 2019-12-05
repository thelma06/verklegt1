class Employee:

    def __init__(self, name = "", so = "", address = "", home_phone = "", cell_phone = "", email = ""):
        self.name = name
        self.so = so
        self.address = address
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.email = email

    def get_name(self):
        return str(self.name)

    def get_so(self):
        return str(self.so)
        
    def get_address(self):
        return str(self.address)

    def get_home_phone(self):
        return str(self.home_phone)

    def get_cell_phone(self):
        return str(self.cell_phone)

    def get_email(self):
        return str(self.email)