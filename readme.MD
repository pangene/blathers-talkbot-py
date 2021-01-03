# Introduction

The Blathers talkbot is a way to hear the descriptions Blathers gives about all the various creatures found in Animal Crossing that you normally only hear when donating said creature. It functions for all the various versions of Animal Crossing and most of the creatures.

The database used to contain all the creatures and all the versions is from a webscraping script I made [here](https://github.com/pangene/acwiki-scraper). It seems to be missing a small amount (around 1-3) of creatures per table. Some of the descriptions may also be partially incorrect. The exact reasons why can be seen in the readme for the acwiki-scraper project. I may manually add/fix those creatures and descriptions later for this project.

This talkbot has both a command-line implementation and a GUI implementation made in Tkinter.

# The command-line implementation

The command-line implementation is very simple. It asks you for what version of Blathers you want to talk to, and then you enter a dialogue-loop.

The dialogue-loop functions a bit like this: root-dialogue --(user-select)--> creature-dialogue --(user-select)--> creature-description --> root-dialogue. This is how dialogue functions in a lot of games, and Animal Crossing is no different.

The functions for root-dialogue and creature-dialogue are the same. However, depending on which version and type of creature you selected, different dialogue will be taken from the SQL table and printed in the command line. 

The way this program is written, it is very simple to add or remove options when the user is requested to choose. The main trouble would be getting the dialogue for the options.

# The GUI implementation

![GUI picture](https://github.com/pangene/blathers-talkbot-py/blob/main/readme_images/blathers_gui_img.png "The Blathers Talkbot GUI")

The graphical user interface is pretty straightforward. You pick what version of Blathers and what type of creature. The list of creatures updates as you make your selection. Then, pick your creature from the list, and press enter to read the description.

This GUI implementation was made with Python's standard GUI library Tkinter. It creates a window, places each of the components in their specified areas, then enters an event loop.

During the event loop, if a button is pressed, or the <Return> key is pressed, it performs the corresponding command. For the buttons, that means updating the respective variable to the new version and updating the creature list. For the version buttons specifically, it might also disable the "Deep Sea Creatures" button as not all versions of Animal Crossing have sea creatures. For the <Return> key, the program gets the appropriate SQL table and gets the description of the selected creature.

This GUI is currently not responsive. The size of the window is set at 1280x720. In the future, I may revisit and make it responsive. However, tkinter does not seem to be well-suited for any sort of visually-appealing UI, so a responsive version would look considerably uglier.

# Improvements

* The current GUI is nonresponsive. It uses tkinter's place method in many areas, which is famously not responsive. If I were to redo this GUI, I could make it responsive but I would have to make it uglier. The problem is that Tkinter has a lot of trouble dealing with transparent images. (It doesn't even have native support for PNGs!)

* Make image appear in the GUI implementation. Again, images in tkinter are hard. Also, I would have to webscrape all those images.

* Adding the remaining creatures to the database/fixing the messed up descriptions, which is really more about either improving my webscraper or manually adding them, which I have so far been too lazy to do.