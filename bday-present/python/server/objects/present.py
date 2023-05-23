class Present(dict):
    def __init__(self,Id, Name, Owner):
        dict.__init__(self, Id = Id, Name = Name, Owner = Owner)