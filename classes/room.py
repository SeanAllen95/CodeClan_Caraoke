class Room:
    
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.guests = 0
        self.till = 0
        self.song_list = []
        
    def guests_enter(self, number_of_guests):
        self.guests += number_of_guests

    def guests_leave(self, number_of_guests):
        self.guests -= number_of_guests

    def add_song_to_room_list(self, new_song):
        self.song_list.append(new_song)

    def increase_cash(self, cash):
        self.till += cash

    def search_for_song_in_room_list(self, songsearch):
        result = ''
        for song in self.song_list:
            if song == songsearch:
                result = song
        
        return result
            
            
    def room_has_capacity(self):
        while self.guests <= self.capacity:
            continue
        if self.guests > self.capacity:
            return False
        
        
            
