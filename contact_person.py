class Contact_person:
    def __init__(self, id, name, phone):
        self.name = name
        self.phone = phone
        self.id = id
    
    def display(self):
        print(f"Id is: {self.id} Name is: {self.name} Phone is: {self.phone}")

