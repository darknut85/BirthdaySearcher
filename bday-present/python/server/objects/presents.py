class Presents(dict):
    def __init__(self,Id, Name, Owner):
        dict.__init__(self, Id = Id, Name = Name, Owner = Owner)

class Present:
    def __init__(self, Id, Name, Owner):
        self.Id = Id
        self.Name = Name
        self.Owner = Owner