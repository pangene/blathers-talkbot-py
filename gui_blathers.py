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
CREATURES = blathers.Blathers.creatures[:3]

def display_text(string):
    '''Displays text in the dialogue textbox.'''
    textbox_text['state'] = tk.NORMAL
    textbox_text.delete(1.0, tk.END)
    textbox_text.insert(tk.END, string)


def beautify_text(string):
    '''Returns beautified form of Python/personal naming-convention string.'''
    return string.replace('_', ' ').replace('-', ' ').title()


def change_version(new_version):
    '''Changes the version of Blathers.'''
    global version
    version = new_version
    version_label['text'] = 'Current: ' + beautify_text(new_version)
    update_type_buttons(version)
    update_creature_list()

def change_type(new_type):
    '''Changes the type of creature being requested.'''
    global type_creature
    type_creature = new_type
    type_current_label['text'] = 'Current: ' + beautify_text(new_type)
    update_creature_list()


def update_type_buttons(version):
    '''Changes which buttons are present based on game version.'''
    if version not in ['new_leaf', 'new_horizons']:
        creature_button_identities['deep-sea_creature']['state'] = tk.DISABLED
        creature_button_identities['fg'] = 'grey'
        if type_creature == 'deep-sea_creature':
            change_type('fish')
    else:
        creature_button_identities['deep-sea_creature']['state'] = tk.NORMAL
        creature_button_identities['fg'] = FONT_COLOR


def update_creature_list():
    '''Updates the creatures in the creature listbox.'''
    dialogues = blathers.get_version_creature_SQL_table(version,
        type_creature, connection)
    creature_listbox.delete(0, tk.END)
    for creature in dialogues:
        creature_listbox.insert(tk.END, creature)


def get_creature_description():
    dialogues = blathers.get_version_creature_SQL_table(version,
        type_creature, connection)
    choice = creature_listbox.get(tk.ANCHOR)
    return dialogues[choice]


def display_description():
    description = get_creature_description()
    display_text(description)


# SQL stuff
connection = blathers.connect_to_database('dialogue.db')


# Create Window
window = tk.Tk()
window.title('Blathers Talkbot')
window.geometry('1280x720')
window.resizable(0, 0)
window.option_add('*Font', FONT + ' 23')
window.bind('<Return>', lambda x: display_description())

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
creature_button_identities = {}
for creature in CREATURES:
    creature_button = tk.Button(master=type_frame,
            text=beautify_text(creature),
            font=FONT+ ' 23',
            bg=TEXTBOX_COLOR,
            fg=FONT_COLOR,
            command=(lambda type_creature:
                        lambda: change_type(type_creature))(creature)
        )
    creature_button_identities[creature] = creature_button
    creature_button.pack(side=tk.LEFT, padx=10)
update_type_buttons(version)

# Create creature selection
creature_frame = tk.Frame(master=window, width=155, height=280, bg='blue')
creature_frame.place(x=630, y=110)
creature_scrollbar = tk.Scrollbar(creature_frame, orient=tk.VERTICAL)
creature_listbox = tk.Listbox(master=creature_frame,
        bd = 0,
        width=20,
        height=12,
        bg=TEXTBOX_COLOR,
        fg=FONT_COLOR,
        font=FONT + ' 18',
        yscrollcommand=creature_scrollbar.set
    )
creature_scrollbar.config(command=creature_listbox.yview)
creature_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
update_creature_list()
creature_listbox.pack()


textbox_frame = tk.Frame(master=window,
        width=700,
        height=150,
        bg=TEXTBOX_COLOR
    )
textbox_frame.place(x=280, y=505)
textbox_scrollbar = tk.Scrollbar(textbox_frame, orient=tk.VERTICAL)
textbox_text = tk.Text(master=textbox_frame,
        state=tk.DISABLED,
        bg=TEXTBOX_COLOR,
        fg=FONT_COLOR,
        width=49,
        height=5,
        wrap=tk.WORD,
        yscrollcommand=textbox_scrollbar.set,
        highlightthickness=0
    )
textbox_scrollbar.config(command=textbox_text.yview)
textbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textbox_text.pack()

display_text("Welcome to the Blathers talkbot GUI! After making your selection, press enter to read the description!")
window.mainloop()
