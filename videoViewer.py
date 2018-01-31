# Program Name  : VideoViewer
# Created by    : Francois Mindiel
# Created date  : 10/05/16
# Version       : 1.0
# Description   : Used to pass parameters to video.py and create objects for TV shows or movies.
#                 Also displays info of objects and opens a web page to browse categories.
#

# Update History:

import video                        # to call functions and class from video.py
import webpagecreator               # to use functions from webpagecreator.py - courtesy of Simon :)


### Creating Movie shows ###
Avengers = video.Movie("The Avengers",
                       "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                       143,
                       "Joss Whedon",
                       2012,
                       "PG-13",
                       "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

DarkKnight = video.Movie("The Dark Knight",
                       "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                       152,
                       "Christopher Nolan",
                       2008,
                       "PG-13",
                       "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                       "https://www.youtube.com/watch?v=EXeTwQWrcwY")

Deadpool = video.Movie("Deadpool",
                       "A former Special Forces operative turned mercenary is subjected to a rogue experiment that leaves him with accelerated healing powers, adopting the alter ego Deadpool.",
                       108,
                       "Tim Miller",
                       2016,
                       "R",
                       "http://i.newsarama.com/images/i/000/162/257/i02/deadpool-ver9-11e99.jpg?1452784920",
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")

GuardiansOfTheGalaxy = video.Movie("Guardians of the Galaxy",
                       "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                       121,
                       "James Gunn",
                       2014,
                       "PG-13",
                       "http://cdn.collider.com/wp-content/uploads/guardians-of-the-galaxy-movie-poster1.jpg",
                       "https://www.youtube.com/watch?v=B16Bo47KS2g")



### Creating TV shows ###
Arrow = video.TVSeries("Arrow",
                       "young vampire hunter",
                       42,
                       "Greg Berlanti",
                       2012,
                       4,
                       10,
                       "http://ia.media-imdb.com/images/M/MV5BMTg3OTc0NzkyOV5BMl5BanBnXkFtZTgwMDMwMTM3MjE@._V1_UY1200_CR80,0,630,1200_AL_.jpg",
                       "https://www.youtube.com/watch?v=2q3l4fMVCO8")

Buffy = video.TVSeries("Buffy the Vampire Slayer",
                       "A young girl, destined to slay vampires, demons and other infernal creatures, deals with her life fighting evil, with the help of her friends.",
                       44,
                       "Joss Whedon",
                       1997,
                       1,
                       12,
                       "http://fontmeme.com/images/Buffy-the-Vampire-Slayer-TV-Series.jpg",
                       "https://www.youtube.com/watch?v=-1v_q6TWAL4")


Flash = video.TVSeries("The Flash",
                       "Barry Allen wakes up 9 months after he was struck by lightning and discovers that the bolt gave him the power of super speed. With his new team and powers, Barry becomes 'The Flash' and fights crime in Central City.",
                       43,
                       "Greg Berlanti",
                       2014,
                       2,
                       9,
                       "http://ia.media-imdb.com/images/M/MV5BNjAwNzkxNzAwNF5BMl5BanBnXkFtZTgwODg2NTc2NjE@._V1_UY1200_CR164,0,630,1200_AL_.jpg",
                       "https://www.youtube.com/watch?v=UMRBs0-OXCA")

ModernFamily = video.TVSeries("Modern Family",
                       "Three different, but related families face trials and tribulations in their own uniquely comedic ways.",
                       22,
                       "Steven Levitan",
                       2009,
                       5,
                       12,
                       "http://ecx.images-amazon.com/images/I/51S2zWtsh1L._AC_UL320_SR232,320_.jpg",
                       "https://www.youtube.com/watch?v=aogZUDx51vQ")


    ### Calling function to show info of the different objects created. ###
Avengers.showInfo()
DarkKnight.showInfo()
Deadpool.showInfo()
GuardiansOfTheGalaxy.showInfo()

Arrow.showInfo()
Buffy.showInfo()
Flash.showInfo()
ModernFamily.showInfo()



### creating categories ###         Used in webpagecreator.py for display in webpage
categories = ["action", "comedy", "drama", "fantasy"]

action = [Avengers, Deadpool, GuardiansOfTheGalaxy, Arrow,Buffy, Flash]
comedy = [Deadpool, ModernFamily]
drama = [DarkKnight, Buffy, Arrow, Flash]
fantasy = [Avengers, Deadpool, GuardiansOfTheGalaxy, Buffy]


webpagecreator.create_genre_pages(categories, [action, comedy, drama, fantasy]) # invokes external file to display webpage






# This is the end of the program
# Francois Mindiel ID 2804582
# This work is protected by copyright laws!