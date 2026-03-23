from music_track import MusicTrack
from artist import Artist
from album import Album

class Song(MusicTrack):
    """
    Represents the music 
    """

    # musician
    def __init__(self,
                 artist: Artist,
                 album: Album,
                 duration_seconds: float):
        super().__init__(artist, album, duration_seconds)

    # specifying the abstract method
    def play_time_formatted(self) -> int:
        minutes = self._duration_seconds // 60
        seconds = self._duration_seconds % 60
        return f"{minutes:02d}: {seconds:02d}"
    
    # printing song
    def __str__(self) -> str:
        return (
            f"({self._artist}) {self._album}, duration: {self.play_time_formatted()}"
        )