'''
A tester class to run the neccessary classes
Author: Thuan Nguyen
'''

# from <file> import <class>
from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist

"""
#Track	 #Artist	        #Genre	      #Album Title              #Active	 #Years	      #Extra
Song	 Kendrick Lamar	    Hip-Hop	      DAMN.	                    True	 2017-2018	  220 sec
Song	 Alanis Morissette  Alternative	  Jagged Little Pill	    False	 1995-1996	  245 sec
Podcast	 Joe Rogan	        Comedy	      The Joe Rogan Experience	True	 2009-2010	  9000 sec, explicit
Podcast	 Sarah Koenig	    Journalism	  Serial	                False	 2014-2015	  5400 sec, not explicit (default)
"""

def main():

    # podcast
    Joe = Podcast(Artist("Joe Rogan", "Comedy"),
                  Album("The Joe Rogan Experience", True, list(range(2009, 2010))), 
                  9000,
                  is_explicit=True)
    
    Sarah = Podcast(Artist("Sarah Koenig", "Journalism"),
                    Album("Serial", False, list(range(2014, 2015))), 
                    5400, 
                    is_explicit=False)
    
    # song
    Lamar = Song(Artist("Kendrick Lamar", "Hip-hop"),
                 Album("DAMN", True, list(range(2017, 2018))), 
                 220)
    
    Alanis = Song(Artist("Alanis Morissette", "Alternative"),
                  Album("Jagged Little Pill", False, list(range(1995, 1996))), 
                  245)
    
    g = Playlist()
    g.add_track(Joe)
    g.add_track(Sarah)
    g.add_track(Lamar)
    g.add_track(Alanis)

    print("Before sorting:")
    print(g)
   
    g.sort_by_release_year()

    print("\nAfter sorting:")
    print(g)

if __name__ == "__main__":
    main()