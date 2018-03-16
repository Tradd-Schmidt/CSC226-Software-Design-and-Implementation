######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T13: Intro to Classes
#
# Purpose: This module demonstrates creating a simple Song class in Python.

######################################################################
# Acknowledgements:
#
# Originally written by: Dr. Jan Pearce
# Attributes:
#    http://www.songlyrics.com/news/most-well-known-song-lyrics/#LC4BPxac0pvlEuLI.99
#    http://soundbible.com/421-Happy-Birthday-To-You.html
#    http://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

class Song(object):
    """
    A class for describing a song

    Usage:
    jinglebells = Song()        # Uses the default lyrics

    # Add Music attribute
    jinglebells.set_music("jingle.wav") # sets the music appropriately

    # use a method
    jinglebells.print_song()

    # Create another Song object
    beatles = Song(["There's nothing you can know that isn't known.",
                        "Nothing you can see that isn't shown.",
                        "There's nowhere you can be that isn't where you're meant to be.",
                        "It's easy!",
                        "All you need is love.",
                        "All you need is love.",
                        "All you need is love,... love.",
                        "Love is all you need."])

    # Add Music attribute
    beatles.print_song()
    beatles.play_music()
    """

    # the following is a class variable with class scope. It is used for the default lyrics
    # Note that it is INSIDE the class. It is available to all class methods and objects
    bdlyrics = '''Happy birthday to you.\nhappy birthday to you.\nhappy birthday to everyone!\nhappy birthday to you!'''

    def __init__(self, lyrics = [bdlyrics]):
        """
        Creates a new Song object with lyrics that can be added optionally.
        If no lyrics are given, then bdlyrics are used.

        :param lyrics: the lyrics to play with the song
        """
        self.lyrics = lyrics
        self.music = None
        self.duration = 0

    def print_song(self):
        """
        Prints out the lyrics of the Song object

        :return: None
        """
        for line in self.lyrics:
            print (line)
        print('')

    def set_music(self, songfile):
        """
        Allows a songfile (eg. "song.wav") to be associated with Song object

        :param songfile: the filename of the .wav file
        :return: None
        """
        import wave
        import contextlib

        self.music = songfile

        with contextlib.closing(wave.open(songfile,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            self.duration = frames / float(rate)
#            print(duration)        # For testing purposes

    def play_music(self):
        """
        Plays associated music of Song object

        :return: None
        """
        import time     # needed for time.sleep() that waits while music is playing
        if self.music is not None:
            import os
            print("Now playing " + self.music)
            os.system("start " + self.music)
            time.sleep(self.duration)
        else:
            print('Please add music to this object.')
# end class

def main():
    """
    The main() funciton demonstrates the use of the Song class
    Uses constructors to make three new Song objects

    :return: None
    """

    # First example
    bday = Song()               # uses the default lyrics
    bday.set_music("hb.wav")
    bday.print_song()
    bday.play_music()

    # Second example
    jinglelyrics = '''Dashing through the snow
    In a one-horse open sleigh
    O'er the fields we go
    Laughing all the way
    Bells on bobtail ring
    Making spirits bright
    What fun it is to ride and sing
    A sleighing song tonight!
    (chorus)

    Jingle bells, jingle bells,
    Jingle all the way.
    Oh! what fun it is to ride
    In a one-horse open sleigh.
    Jingle bells, jingle bells,
    Jingle all the way;
    Oh! what fun it is to ride
    In a one-horse open sleigh.'''

    jingle = Song([jinglelyrics]) # uses the given lyrics

    # Add Music attribute
    jingle.set_music("jingle.wav")

    # Use of various methods
    jingle.print_song()
    jingle.play_music()


    # Third example
    beatles = Song(["There's nothing you can know that isn't known.",
                        "Nothing you can see that isn't shown.",
                        "There's nowhere you can be that isn't where you're meant to be.",
                        "It's easy!",
                        "All you need is love.",
                        "All you need is love.",
                        "All you need is love,... love.",
                        "Love is all you need."])

    beatles.print_song()
    beatles.play_music()        # We forgot to add the music, so this won't work!!


main()
