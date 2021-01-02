# Introduction

The Blathers talkbot is a way to hear the descriptions Blathers gives about all the various creatures found in Animal Crossing that you normally only hear when donating said creature. It functions for all the various versions of Animal Crossing and most of the creatures.

The database used to contain all the creatures and all the versions is from a webscraping script I made [here](https://github.com/pangene/acwiki-scraper). It seems to be missing a small amount (~1-3 creatures) per table. The exact reasons why can be seen in the readme for the acwiki-scraper project. I may manually add those creatures and descriptions later for this project.

This talkbot only works on the command-line. There is a gui implementation, but right now it is very broken. If you for some reason want to play with this project, just access it through the command line for now.

# How it works

The command-line implementation is very simple. It asks you for what version of Blathers you want to talk to, and then you enter a dialogue-loop.

The dialogue-loop functions a bit like this: root-dialogue --(user-select)--> creature-dialogue --(user-select)--> creature-description --> root-dialogue. This is how dialogue functions in a lot of games, and Animal Crossing is no different.

The functions for root-dialogue and creature-dialogue are the same. However, depending on which version and type of creature you selected, different dialogue will be taken from the SQL table and printed in the command line. 

The way this program is written, it is very simple to add or remove options when the user is requested to choose. The main trouble would be getting the dialogue for the options.

# Improvements

* I'm still currently working on the gui form of this talkbot, which will use Tkinter.

* Adding the remaining creatures to the database, which is really more about either improving my webscraper or manually adding them, which I have so far been too lazy to do.