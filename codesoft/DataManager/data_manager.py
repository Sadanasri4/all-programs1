import json

class DataManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        self.contacts.append(contact.__dict__)
        self.save_contacts()

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        self.save_contacts()

    def search_contact(self, search_term):
        return [c for c in self.contacts if search_term.lower() in c['name'].lower() or search_term in c['phone']]

    def update_contact(self, old_name, new_contact):
        for i, c in enumerate(self.contacts):
            if c['name'] == old_name:
                self.contacts[i] = new_contact.__dict__
                break
        self.save_contacts()
