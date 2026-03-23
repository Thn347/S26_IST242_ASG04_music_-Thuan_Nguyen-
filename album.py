"""
Represents an Album
"""

class Album:
    def __init__(
            self, 
            title: str, 
            active: bool, 
            years: list[int]
            ):
        if not years:
            raise ValueError("The years list must not be empty.")
        
        self._name = title
        self._active = active
        self._years = list(years) # defensive copy

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def active(self) -> bool:
        return self._active
    
    @property
    def years(self) -> list[int]:
        return list(self._years) # return a copy
    
    @property
    def first_year(self) -> int:
        """
        Returns the first (earliest) debut years
        """
        return self._years[0]
    
    # F150 in production = True, release year: 2020
    def __str__(self) -> str:
        return f"{self._name}. active = {self._active}, debut year: {self._years[0]}"
        