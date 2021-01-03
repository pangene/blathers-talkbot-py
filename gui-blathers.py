import tkinter as tk
from PIL import ImageTk, Image
import blathers

# Chalkboard, Nadeem, Gill Sans are all similar to AC font
FONT = 'Chalkboard'
BACKGROUND_IMAGE = 'images/background_long-creature.png'
# RGB for textbox background: 254, 250, 230
TEXTBOX_COLOR = '#FEFAE6'
# RGB for font color: 138, 132, 110
FONT_COLOR = '#8A846E'
BLATHERS_IMAGE = 'images/Blathers_NH.png'

VERSIONS = blathers.Blathers.versions
CREATURES = ['bug', 'fish', 'deep-sea_creature']


def display_text(string):
    '''Displays text in the dialogue textbox.'''
    text_label['text'] = string


def beautify_text(string):
    '''Returns beautified form of Python/personal naming-convention string.'''
    return string.replace('_', ' ').replace('-', ' ').title()


def change_version(new_version):
    '''Changes the version of Blathers.'''
    global version
    version = new_version
    version_label['text'] = 'Current: ' + beautify_text(new_version)
    update_creature_list(version, type_creature, connection)

def change_type(new_type):
    '''Changes the type of creature being requested.'''
    global type_creature
    type_creature = new_type
    type_current_label['text'] = 'Current: ' + beautify_text(new_type)
    update_creature_list(version, type_creature, connection)

def update_creature_list(version, type_creature, connection):
    '''Updates the creatures in the creature listbox.'''
    dialogues = blathers.get_version_creature_SQL_table(version,
        type_creature, connection)
    creature_listbox.delete(0, tk.END)
    for creature in dialogues:
        creature_listbox.insert(tk.END, creature)



# SQL stuff
connection = blathers.connect_to_database('dialogue.db')


# Create Window
window = tk.Tk()
window.title('Blathers Talkbot')
window.geometry('1280x720')
window.resizable(0, 0)
window.option_add('*Font', FONT + ' 26')

# Set background image
background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_IMAGE))
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create version selection
version_frame = tk.Frame(master=window, width=350, height=115, bg=TEXTBOX_COLOR)
version_frame.place(x=130, y=105)
version_frame.columnconfigure([0, 1, 2], minsize=105)
version_frame.rowconfigure([0, 1], minsize=50)
row, column = 0, 0
for version in VERSIONS:
    if column == 3:
        column = 0
        row += 1
    version_button = tk.Button(master=version_frame,
            text=beautify_text(version),
            font=FONT + ' 23',
            bg=TEXTBOX_COLOR,
            fg=FONT_COLOR,
            command=(lambda version: lambda: change_version(version))(version)
        )
    version_button.grid(row=row, column=column)
    column += 1
version = VERSIONS[0]
version_label = tk.Label(master=window,
        text='Current: ' + beautify_text(version),
        bg=TEXTBOX_COLOR,
        fg=FONT_COLOR,
        font=FONT + ' 23'
    )
version_label.place(x=220, y=65)


# Create creature type selection
type_creature = CREATURES[0]
type_frame = tk.Frame(master=window, width=350, height=95, bg=TEXTBOX_COLOR)
type_frame.place(x=170, y=310)
type_current_label = tk.Label(master=type_frame,
        text='Current: ' + beautify_text(type_creature),
        bg=TEXTBOX_COLOR,
        fg=FONT_COLOR,
        font=FONT + ' 23'
    )
type_current_label.pack(pady=10)
for creature in CREATURES:
    creature_button = tk.Button(master=type_frame,
            text=beautify_text(creature),
            font=FONT+ ' 23',
            bg=TEXTBOX_COLOR,
            fg=FONT_COLOR,
            command=(lambda type_creature:
                        lambda: change_type(type_creature))(creature)
        )
    creature_button.pack(side=tk.LEFT, padx=10)


# Create creature selection
creature_frame = tk.Frame(master=window, width=155, height=280, bg='blue')
creature_frame.place(x=630, y=110)
creature_scrollbar = tk.Scrollbar(creature_frame, orient=tk.VERTICAL)
creature_listbox = tk.Listbox(master=creature_frame,
        width=12,
        height=12,
        bg=TEXTBOX_COLOR,
        fg=FONT_COLOR,
        font=FONT + ' 18',
        yscrollcommand=creature_scrollbar.set
    )
creature_scrollbar.config(command=creature_listbox.yview)
creature_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
update_creature_list(version, type_creature, connection)
creature_listbox.pack()


textbox_frame = tk.Frame(master=window,
        width=700,
        height=150,
        bg=TEXTBOX_COLOR
    )
textbox_frame.place(x=280, y=510)
text_label = tk.Label(textbox_frame,
        text='',
        anchor='w',
        bg=TEXTBOX_COLOR,
        fg=FONT_COLOR,
        wraplength=675,
        justify='left',
    )

display_text("Welcome to the Blathers talkbot GUI!")
text_label.grid(sticky='w')
window.mainloop()

