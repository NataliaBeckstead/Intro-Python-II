class Room:
    def __init__(self, name, description, is_light, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return 'Name: {self.name}, description: {self.description}, items: {self.items}, light: {self.is_light}'.format(self=self)

