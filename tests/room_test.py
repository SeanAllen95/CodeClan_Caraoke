import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("ABBA Room", 25, 5)
        self.song = Song("Dancing Queen", 3)

        self.guest_1 = Guest("Jim", "Dancing Queen", 60)
        self.guest_2 = Guest("Bob", "Mamma Mia", 40)

    def test_has_name(self):
        self.assertEqual("ABBA Room", self.room.name)

    def test_has_price(self):
        self.assertEqual(25, self.room.price)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def test_guests_enter(self):
        self.room.guests_enter(2)
        self.assertEqual(2, self.room.guests)

    def test_guests_leave(self):
        self.room.guests_enter(2)
        self.room.guests_leave(1)
        self.assertEqual(1, self.room.guests)

    def test_add_song_to_room_list(self):
        self.room.add_song_to_room_list("Dancing Queen")
        self.assertEqual("Dancing Queen", self.room.song_list[-1])

    def test_search_for_song_in_room_list(self):
        self.room.add_song_to_room_list("Mamma Mia")
        self.assertEqual(["Mamma Mia"], self.room.song_list)

    def test_increase_cash(self):
        self.room.increase_cash(25)
        self.assertEqual(25, self.room.till)
   
    def test_guest_rent_room(self):
        self.room.increase_cash(25)
        self.room.add_song_to_room_list("Dancing Queen")
        self.guest_1.rent_room(25)
        self.room.guests_enter(1)
        self.assertEqual(25, self.room.till)
        self.assertEqual("Dancing Queen", self.room.song_list[-1])
        self.assertEqual(35, self.guest_1.wallet)
        self.assertEqual(1, self.room.guests)
    
    def test_room_has_capacity(self):
        self.room.guests_enter(5)
        self.assertEqual(self.room.capacity, self.room.guests)

    def test_room_has_favourite_song(self):
        self.room.add_song_to_room_list(self.guest_1.favourite_song)
        self.room.search_for_song_in_room_list(self.guest_1.favourite_song)
        self.assertEqual([self.guest_1.favourite_song], self.room.song_list)



