class Clients():
    def __init__(self, name, phoneNumber, dob):
        self.name = name
        self.phoneNumber = phoneNumber
        self.dob = dob
        self.id = None
    def __str__(self):
        client_str = "Name: " + self.name + "\n"
        client_str += "Phone Number: " + self.phoneNumber + "\n"
        client_str += "Date of Birth(MMDDYYYY): " + self.dob + "\n"
        return client_str
