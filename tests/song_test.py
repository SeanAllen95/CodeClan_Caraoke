import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Dancing Queen", 3)
    
    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song.name)

    def test_song_has_duration(self):
        self.assertEqual(3, self.song.duration)

    