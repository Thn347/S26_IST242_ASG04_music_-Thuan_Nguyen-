from music_track import MusicTrack
from artist import Artist
from album import Album

class Podcast(MusicTrack):
    """
    Represent a podcast
    """

    # constructor
    def __init__(self,
                 artist: Artist,
                 album: Album,
                 duration_seconds: int,
                 is_explicit: bool = False # Additional attribution
    ):
        super().__init__(artist, album, duration_seconds)
        self._is_explicit = is_explicit

    @property
    def is_explicit(self) -> bool:
        return self._is_explicit

    # specifying the abstract method with podcast's condition
    def play_time_formatted(self) -> int:
        hours = self._duration_seconds // 3600
        remaining = self._duration_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    # printing podcast
    def __str__(self) -> str:
        return (
            f"({self._artist}) {self._album}, duration: {self.play_time_formatted()} is explicit: {self._is_explicit}"
        )