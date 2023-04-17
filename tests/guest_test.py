import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Brian", "Dancing Queen", 50)

    def test_guest_has_name(self):
        self.assertEqual("Brian", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Dancing Queen", self.guest.favourite_song)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_rent_room(self):
        self.guest.rent_room(25)
        self.assertEqual(25, self.guest.wallet)


