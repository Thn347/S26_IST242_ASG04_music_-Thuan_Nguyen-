'''
This is the unit testing file.
Author: Thuan Nguyen
'''

import pytest

from artist import Artist
from album import Album
from music_track import MusicTrack
from song import Song
from podcast import Podcast
from playlist import Playlist



#  Unit testing for artist.py
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


#  Unit testing for album.py
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


# Unit testing for song.py
class TestSong:
    @pytest.fixture
    def song(self):
        return Song(
            Artist("Da Lab", "V-pop"),
            Album("Chilling Breeze", False, [2015, 2016, 2017, 2018]),
            220,
        )
    
    def test_play_time_formatted(self, song):
        assert song.play_time_formatted() == "03:40"

    def test_debut_year(self, song):
        assert song.release_year == 2015

    def test_duration_seconds(self, song):
        assert song.duration_second == 220

    def test_artist(self, song):
        assert song.artist.name == "Da Lab"
        assert song.artist.genre == "V-pop"

    def test_album(self, song):
        assert song.album.name == "Chilling Breeze"

    def test_total_play_time(self, song):
        assert song.total_play_time(2) == 440
        assert song.total_play_time(5) == 1100

    def test_str_contains_required_parts(self, song):
        s = str(song)
        assert "(Da Lab, V-pop)" in s
        assert "Chilling Breeze" in s
        assert "03:40" in s

    def test_str_is_not_explicit(self, song):
        s = str(song)
        assert "explicit" not in s.lower()

    def test_is_instance_of_song(self, song):
        assert isinstance(song, MusicTrack)


# Unit testing for podcast.py
class TestPodcast:
    @pytest.fixture
    def joe(self):
        return Podcast(
            Artist("Joe Rogan", "Comedy"),
            Album("The Joe Rogan Experience", True, [2009, 2010]),
            9000,
            is_explicit=True
        )

    @pytest.fixture
    def sarah(self):
        return Podcast(
            Artist("Sarah Koenig", "Journalism"),
            Album("Serial", False, [2014, 2015]),
            5400,
            is_explicit=False,
        )
    # Explicit
    def test_is_explicit_true(self, joe):
        assert joe.is_explicit is True

    def test_podcast_explicit(self, joe):
        assert joe.play_time_formatted() == "02:30:00"

    def test_release_year_tundra(self, joe):
        assert joe.release_year == 2009

    def test_str_explicit(self, joe):
        s = str(joe)
        assert "(Joe Rogan, Comedy)" in s
        assert "The Joe Rogan Experience" in s
        assert "02:30:00" in s
        assert "True" in s

    
    # Not explicit
    def test_default_not_explicit(self, sarah):
        assert sarah.is_explicit is False

    def test_wheels_non_explicit(self, sarah):
        assert sarah.play_time_formatted() == "01:30:00"

    def test_release_year_serial(self, sarah):
        assert sarah.release_year == 2014

    def test_str_non_explicit(self, sarah):
        s = str(sarah)
        assert "(Sarah Koenig, Journalism)" in s
        assert "Serial" in s
        assert "01:30:00" in s
        assert "False" in s


    def test_how_far_with(self, joe):
        assert joe.total_play_time(2) == 18000

    def test_is_instance_of_music_track(self, joe):
        assert isinstance(joe, MusicTrack)


# Unit testing for comparison and ordering functions
class TestComparison:
    @pytest.fixture
    def song_2020(self):
        return Song(
            Artist("Holunolu", "Hawaii"),
            Album("Hawaii festive", True, [2020, 2021]),
            220,
        )
    
    @pytest.fixture
    def song_1995(self):
        return Song(
            Artist("Volca Halo", "Hawaii"),
            Album("Summer eruption", False, [1995, 1996]),
            245,
        )
    
    @pytest.fixture
    def podcast_2018(self):
        return Podcast(
            Artist("Ngo Kien Huy", "V-pop"),
            Album("Dear, Vietnam", False, [2018, 2019, 2020]),
            9000,
        )

    @pytest.fixture
    def podcast_2020(self):
        return Podcast(
            Artist("YOASOBI", "J-pop"),
            Album("Anime Shockwave", True, [2020, 2021, 2022]),
            4500,
        )

    def test_lt(self, song_2020, song_1995):
        assert song_1995 < song_2020

    def test_not_lt_when_greater(self, song_2020, song_1995):
        assert not (song_2020 < song_1995)

    def test_eq_same_year(self, song_2020, podcast_2020):
        assert song_2020 == podcast_2020

    def test_not_eq_different_year(self, song_1995, song_2020):
        assert song_1995 != song_2020

    def test_gt(self, podcast_2020, podcast_2018):
        assert podcast_2020 > podcast_2018

    def test_sorted_order(self, song_1995, song_2020, podcast_2018):
        vehicles = [song_1995, song_2020, podcast_2018]
        result = sorted(vehicles)
        assert result[0].release_year == 1995
        assert result[1].release_year == 2018
        assert result[2].release_year == 2020
 

# Unit testing for playlist.py
class TestPlaylist:
    @pytest.fixture
    def full_playlist(self):
        g = Playlist()
        g.add_track(
            Podcast(
                Artist("Fordilex Accel", "USA"),
                Album("Metal to the Pedal", True, [2020, 2021, 2022]),
                5400,
                is_explicit=False,
            )
        )
        g.add_track(
            Song(
                Artist("Jun Pham", "V-pop"),
                Album("Cupid Love", False, [1996, 1997, 1998]),
                245,
            )
        )
        g.add_track(
            Song(
                Artist("HOYOVERSE", "Internation"),
                Album("Ripples of Past Reveries", False, [2026]),
                330,
            )
        )
        g.add_track(
            Podcast(
                Artist("miHOYO", "Internation"),
                Album("Honkai Universe", False, [2024, 2025]),
                9000,
                is_explicit=True,
            )
        )
        return g

    def test_add_track(self):
        g = Playlist()
        assert len(g.tracks) == 0
        g.add_track(
            Song(
                Artist("HOYOVERSE", "Internation"),
                Album("Code of Chivalry", True, [2026]),
                330,
            )
        )
        assert len(g.tracks) == 1

    def test_playlists_returns_copy(self):
        """Changing the returned list should not have any affect"""
        g = Playlist()
        g.add_track(
            Song(
                Artist("Comlumbina", "Lullaby"),
                Album("Birth of a Goddess", True, [2027]),
                245,
            )
        )
        external = g.tracks
        external.clear()
        assert len(g.tracks) == 1

    def test_empty_playlist(self):
        g = Playlist()
        g.add_track(
            Song(
                Artist("Skirk", "Beyondy"),
                Album("Solitude and Past", True, [2025]),
                120,
            )
        )
        g.clear_playlist()
        assert len(g.tracks) == 0

    def test_empty_playlist_does_not_set_none(self):
        """After emptying, add_track should still work (list not None)."""
        g = Playlist()
        g.add_track(
            Song(
                Artist("HOYOVERSE", "Internation"),
                Album("Code of Chivalry", True, [2026]),
                330,
            )
        )
        g.clear_playlist()
        # If the internal list were None, this would raise an AttributeError
        g.add_track(
            Song(
                Artist("Comlumbina", "Lullaby"),
                Album("Birth of The Moon Goddess", True, [2027]),
                245,
            )
        )
        assert len(g.tracks) == 1

    def test_sort_by_release_year(self, full_playlist):
        full_playlist.sort_by_release_year()
        tracks = full_playlist.tracks
        years = [v.release_year for v in tracks]
        assert years == sorted(years)

    def test_sort_order_specific(self, full_playlist):
        full_playlist.sort_by_release_year()
        tracks = full_playlist.tracks
        assert tracks[0].release_year == 1996
        assert tracks[1].release_year == 2020
        assert tracks[2].release_year == 2024
        assert tracks[3].release_year == 2026

    def test_str_contains_all_music_track(self, full_playlist):
        s = str(full_playlist)
        assert "Fordilex Accel" in s
        assert "Jun Pham" in s
        assert "HOYOVERSE" in s
        assert "miHOYO" in s

    def test_str_music_track_on_separate_lines(self, full_playlist):
        s = str(full_playlist)
        lines = s.strip().split("\n")
        assert len(lines) == 4


# Unit testing for main.py
class TestMain:

    def test_full_workflow(self):
        """Mirrors the main.py scenario end-to-end."""
        genshin = Artist("HOYOVERSE", "Genshin Impact")
        impact = Podcast(genshin, Album("The World of Teyvat", True, [2020, 2021, 2022]), 9000, is_explicit=True)

        honkai = Artist("miHOYO", "Honkai Star Rail")
        star_rail = Podcast(honkai, Album("Honkai Universe", True, [2023, 2024, 2025]), 9000, is_explicit=True)

        cookie = Artist("Devister", "Cookie Run Kingdom")
        run_kingdom = Song(cookie, Album("Everything you need", False, [2022]), 220)

        frieren = Artist("Mrs. GREEN APPLE", "J-pop")
        himmel = Song(frieren, Album("lulu", False, [2026]), 245)
        
        g = Playlist()
        for v in [impact, star_rail, run_kingdom, himmel]:
            g.add_track(v)

        # Before sorting
        before = g.tracks
        assert before[0].album.name == "The World of Teyvat"
        assert before[1].album.name == "Honkai Universe"
        assert before[2].album.name == "Everything you need"
        assert before[3].album.name == "lulu"

        g.sort_by_release_year()

        # After sorting
        after = g.tracks
        assert after[0].album.name == "The World of Teyvat"
        assert after[1].album.name == "Everything you need"
        assert after[2].album.name == "Honkai Universe"
        assert after[3].album.name == "lulu"

        # Verify types survived polymorphism
        assert isinstance(after[0], Podcast)
        assert isinstance(after[1], Song)
        assert isinstance(after[2], Podcast)
        assert isinstance(after[3], Song)

        # Verify explicit status
        assert after[0].is_explicit is True
        assert after[2].is_explicit is True

        # Verify play_time_formatted
        assert after[0].play_time_formatted() == "02:30:00"   # Genshin Impact
        assert after[1].play_time_formatted() == "03:40"      # Cookie Run Kingdom
        assert after[2].play_time_formatted() == "02:30:00"   # Honkai Star Rail
        assert after[3].play_time_formatted() == "04:05"      # Beyond the Journey's End

        # Verify total_play_time
        assert after[1].total_play_time(2) == 440