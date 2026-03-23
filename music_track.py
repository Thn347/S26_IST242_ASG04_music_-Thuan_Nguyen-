from abc import ABC, abstractmethod
# from functools import total_ordering  # sorting purposes

from artist import Artist
from album import Album

class MusicTrack(ABC):
    """
    Abstract base class (ABC) for all vehicles
    """
    # musician
    def __init__(self,
                 artist: Artist,
                 album: Album,
                 duration_seconds: float):
        self._artist = artist
        self._album = album
        self._duration_seconds = duration_seconds

    @property
    def artist(self) -> Artist:
        return self._artist
    
    @property
    def album(self) -> Album:
        return self._album
    
    @property
    def duration_second(self) -> float:
        return self._duration_seconds
    
    @property
    def release_year(self) -> int:
        return self._album.years[0]
    
    # ----- concrete methods -----
    def total_play_time(self, num_plays: int) -> float:
        return self._duration_seconds * num_plays
    
    # ----- abstract methods -----
    @abstractmethod
    def play_time_formatted(self) -> str:
        pass


    # ---- comparison criteria ----

    def __eq__(self, other) -> bool:
        if not isinstance(other, MusicTrack):
            return NotImplemented
        return self.release_year == other.release_year

    def __lt__(self, other) -> bool:
        if not isinstance(other, MusicTrack):
            return NotImplemented
        return self.release_year < other.release_year
    
    def __hash__(self, other) -> bool:
        return hash(self.release_year)