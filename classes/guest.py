class Guest:
    
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def rent_room(self, amount):
        self.wallet -= amount

