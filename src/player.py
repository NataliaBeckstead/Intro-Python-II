class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = 'outside'
        self.items = []
    def __str__(self):
        return 'Name: {self.name}, current room: {self.current_room}, items: {self.items}'.format(self=self)