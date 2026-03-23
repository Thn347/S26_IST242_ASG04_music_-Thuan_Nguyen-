'''
This represented music artist
'''

class Artist:
    """
    Docstring for Artist
    """
    # constructor
    def __init__(self, name: str, genre: str):
        self._name = name
        self._genre = genre
        pass

    # getters methods
    @property
    def name(self) -> str:
        return self._name
    
    # properties
    @property
    def genre(self) -> str:
        return self._genre
    
    # printing out the artist objects
    def __str__(self) -> str:
        return f"{self._name}, {self._genre}"
        
    # setter methods
