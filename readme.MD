# Usage

If for some reason you want to play with these programs:

1. Download or clone this repository onto your machine

2. Open your shell (terminal, bash, etc.)

3. Move to the directory you downloaded

4. Run ```python3 filename.py``` where filename.py is the implementation you want to run. The command-line implementation is blathers.py, the pretty GUI is gui_blathers.py, and the responsive GUI is responsive_gui_blathers.py

# Introduction

The Blathers talkbot is a way to hear the descriptions Blathers gives about all the various creatures found in Animal Crossing that you normally only hear when donating said creature. It functions for all the various versions of Animal Crossing and most of the creatures.

The database used to contain all the creatures and all the versions is from a webscraping script I made [here](https://github.com/pangene/acwiki-scraper). It seems to be missing a small amount (around 1-3) of creatures per table. Some of the descriptions may also be partially incorrect. The exact reasons why can be seen in the readme for the acwiki-scraper project. I may manually add/fix those creatures and descriptions later for this project.

This talkbot has a command-line implementation and two GUI implementations, a pretty version I made first and then a responsive version, both made in Tkinter.

# The command-line implementation

The command-line implementation is very simple. It asks you for what version of Blathers you want to talk to, and then you enter a dialogue-loop.

The dialogue-loop functions a bit like this: root-dialogue --(user-select)--> creature-dialogue --(user-select)--> creature-description --> root-dialogue. This is how dialogue functions in a lot of games, and Animal Crossing is no different.

The functions for root-dialogue and creature-dialogue are the same. However, depending on which version and type of creature you selected, different dialogue will be taken from the SQL table and printed in the command line. 

The way this program is written, it is very simple to add or remove options when the user is requested to choose. The main trouble would be getting the dialogue for the options.

# The GUI implementations

Both versions of the graphical user interface are pretty straightforward to use. You pick what version of Blathers and what type of creature. The list of creatures updates as you make your selection. Then, pick your creature from the list, and press enter to read the description.

The GUI implementations were made with Python's standard GUI library Tkinter. They are functionally the same. Each GUI creates a window, organizes each of the components in their specified areas, then enters an event loop.

During the event loop, if a button is pressed, or the <Return> key is pressed, it performs the corresponding command. For the buttons, that means updating the respective variable to the new version and updating the creature list. For the version buttons specifically, it might also disable the "Deep Sea Creatures" button as not all versions of Animal Crossing have sea creatures. For the <Return> key, the program gets the appropriate SQL table and gets the description of the selected creature.

## The Pretty GUI

![GUI picture](https://github.com/pangene/blathers-talkbot-py/blob/main/readme_images/blathers_gui_img.png "The Blathers Talkbot GUI")

This Pretty GUI is not responsive. The size of the window is set at 1280x720 (the screen size of the Nintendo Switch) and cannot be changed. During the organization of the components of the GUI, tkinter's place method is used in numerous areas, which is bad practice for responsive GUIs.

I made this pretty version first before I had a good understanding of Tkinter's limits. I had some images I premade for this project and I wanted to use them. 

Tkinter is absolutely not well-suited for any sort of visually-appealing UI (It doesn't even have native support for PNGs!). Transparent backgrounds on PNGs do not function unless using a Canvas widget, which has its own limitations for responsiveness. In the end, I just decided to make a non-responsive GUI.

## The Responsive GUI

![Responsive GUI picture](https://github.com/pangene/blathers-talkbot-py/blob/main/readme_images/blathers_responsive_gui_img.png "The Blathers Talkbot Responsive GUI")

If you can't tell by the name, this version of the GUI is responsive. It has a minimum size of 525x650 to fit all the components neatly, but it can be expanded much larger.

After making the pretty GUI and violating many good practice standards of Tkinter, I decided to make this responsive version. While not perfect, it follows guidelines much better and was made with a much better understanding of Tkinter's tools and limitations.

# Improvements

* Make image appear in the GUI implementation. Again, images in tkinter are hard. Also, I would have to webscrape all those images.

* Adding the remaining creatures to the database/fixing the messed up descriptions, which is really more about either improving my webscraper or manually adding them, which I have so far been too lazy to do.

* Making the GUI into an executable. I tried to use PyInstaller for this, but I kept running into errors. I may try again later.