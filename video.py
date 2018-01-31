# Program Name  : video.py
# Created by    : Francois Mindiel
# Created date  : 10/05/16
# Version       : 1.0
# Description   : Used to create objects when parameters are passed on. Contains a parent class and 2 child classes.
#
#

# Update History:

import webbrowser       # used to open a url in the web browser

class Video():          # class used to create objects, with initialisation

    """
    A generic display of information for a video.
    """

    def __init__(self, title = "", desc = "", duration = 0, image_url = "", youtube_url = ""):      # initialisation
        self.title = title
        self.desc = desc
        self.duration = duration
        self.image_url = image_url
        self.youtube_url = youtube_url

    def showInfo(self):                                             # displays info for Video class
        print("\n********************************************\n")
        print("\t\t\t", self.__doc__)
        print("\n********************************************\n")
        print("Title:\t\t\t", self.title)
        print("Description:\t", self.desc)
        print("Duration:\t\t", self.duration, "minutes")
        print("Image url:\t\t", self.image_url)
        print("Youtube url:\t", self.youtube_url)

    def open_image_url(self):
        webbrowser.open(self.image_url)

    def open_youtube_url(self):
        webbrowser.open(self.youtube_url)


class Movie(Video):
    """
    Lists information for a movie.
    """
    def __init__(self, title, desc, duration, director, yearRelease, rating, image_url, youtube_url):

        Video.__init__(self, title, desc, duration, image_url, youtube_url) # initialisation for child class

        self.director = director
        self.yearRelease = yearRelease
        self.rating = rating

    def showInfo(self):                                     # overrides showInfo from Video class
        Video.showInfo(self)

        print("Director:\t\t", self.director)               # prints additional details for Movie class
        print("Year of release:", self.yearRelease)
        print("Rating:\t\t\t", self.rating)
        print(input())


class TVSeries(Video):
    """
    Lists information for a TV show.
    """
    def __init__(self, title, desc, duration, director, yearAired, seasonNo, episodeNo, image_url, youtube_url):
        Video.__init__(self, title, desc, duration, image_url, youtube_url) # initialisation for child class

        self.director = director                            # initialisation of additional parameters for tvShow class
        self.yearAired = yearAired
        self.seasonNo = seasonNo
        self.episodeNo = episodeNo


    def showInfo(self):                                     # overrides showInfo from Video class
        Video.showInfo(self)

        print("Director:\t\t", self.director)               # prints additional details for tvShow class
        print("Year aired:\t\t", self.yearAired)
        print("Season No:\t\t", self.seasonNo)
        print("Episode No:\t\t", self.episodeNo)
        print(input())






# This is the end of the program
# Francois Mindiel ID 2804582
# This work is protected by copyright laws!