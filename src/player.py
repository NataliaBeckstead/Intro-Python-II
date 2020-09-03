class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def __str__(self):
        return 'Name: {self.name}, current room: {self.current_room}, items: {self.items}'.format(self=self)