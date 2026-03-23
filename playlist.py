from music_track import MusicTrack

class Playlist:
    '''
    A playlist is a place that stores a collection of songs
    '''

    # Constructor
    def __init__(self):
        """Initialize an empty list"""
        self._tracks: list[MusicTrack] = []

    # Getter
    @property
    def tracks(self) -> list[MusicTrack]:
        """Return a copy of the internal list (to protect encapsulation)"""
        return list(self._tracks)

    def add_track(self, musictrack: MusicTrack) -> None:
        """Add a track to the list"""
        self._tracks.append(musictrack)

    def clear_playlist(self):
        """Empties the playlist of all the track"""
        self._tracks.clear()

    def sort_by_release_year(self):
        self._tracks.sort()

    def __str__(self) -> str:
        return "\n".join(str(v) for v in self._tracks) # str1.join(str2)