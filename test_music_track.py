'''
This is the unit testing file.
Author: Thuan Nguyen
'''

import pytest

from artist import Artist
from album import Album
from music_track import MusicTrack
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


#  Unit Testing for album.py
class TestAlbum:
    def test_constructor(self):
        am = Album("Peace and Relaxation", True, [2020, 2021, 2022])
        assert am.name == "Peace and Relaxation"
        assert am.active == True
        assert am.years == [2020, 2021, 2022]

    def test_first_year(self):
        am = Album("Chill with Da Lab", False, [2023, 2024, 2025])
        assert am.debut_year == 2023

    def test_str(self):
        am = Album("Rocking Hurricane", False, [1987, 1988])
        result = str(am)
        assert "Rocking Hurricane" in result
        assert "False" in result
        assert "1987" in result

    def test_empty_years_raises(self):
        with pytest.raises(ValueError):
            Album("Forgotten song", False, [])

    def test_years_defensive_copy(self):
        """Changing the original must not affect the model"""
        original_list = [2025, 2026]
        am = Album("Anime Shockwave", True, original_list)
        original_list.clear()
        assert am.years == [2025, 2026]

    def test_years_getter_returns_copy(self):
        """Changing the original must not affect the model"""
        am = Album("The world of Genshin", False, [2020, 2021, 2022, 2023, 2024, 2025])
        returned = am.years
        returned.append(2026)
        assert len(am.years) == 6


#  Unit testing for music_track.py and abstract contract
class TestMusicTrackAbstract:
    def test_music_track_cannot_be_directly_initialized(self):
        """Music Track is abstract and should not be directly initialized"""
        with pytest.raises(TypeError):
            MusicTrack(
                Artist("Thuan Nguyen", "Internation"),
                Album("Harmonize Earth", True, [2040]),
                300
            )

    def test_subclass_must_implement_total_play_time(self):
        """A subclass that does not have total_play_time should not work"""
        # This incomplete version should raise TypeError
        with pytest.raises(TypeError):
            class Incompletion(MusicTrack):
                pass
            Incompletion(
                Artist("Nguyen Huu", "Beyondy"),
                Album("Beyond The Earth's End", True, [4080]),
                290
            )