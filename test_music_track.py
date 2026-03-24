'''
This is the unit testing file.
Author: Thuan Nguyen
'''

import pytest

from artist import Artist
# from album import Album
# from vehicle import Vehicle
# from sedan import Sedan
# from truck import Truck
# from garage import Garage



#  Unit Testing for artist.py
class TestArtist:
    def test_constructor(self):
        m = Artist("BTS", "K-pop")
        assert m.name == "BTS"
        assert m.genre == "K-pop"

    def test_str(self):
        m = Artist("Hoa Minzy", "V-pop")
        assert str(m) == "Hoa Minzy, V-pop"

    def test_constructor_2(self):
        m = Artist("Mrs.GREEN APPLE", "J-pop")
        assert m.name == "Mrs.GREEN APPLE"
        assert m.genre == "J-pop"
        assert str(m) == "Mrs.GREEN APPLE, J-pop"



        