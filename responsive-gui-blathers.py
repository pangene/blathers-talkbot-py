import tkinter as tk
import blathers

DEFAULT_FONT = 'Chalkboard 23'
LISTBOX_FONT = 'Chalkboard 18'
BLURB_COLOR = '#FEFAE6'
TEXT_COLOR = '#8A846E'
HEADING_COLOR = 'pink'
HEADING_TEXT_COLOR = 'white'
BACKGROUND_COLOR = 'blue'

VERSIONS = blathers.Blathers.versions
CREATURES = blathers.Blathers.creatures[:3]


# Utility functions
def beautify_text(string):
    '''Returns beautified form of Python/personal naming-convention string.'''
    return string.replace('_', ' ').replace('-', ' ').title()

# Command functions for buttons



# Creating root window
root = tk.Tk()
root.title('Blathers Talkbot Responsive GUI')
root.minsize(500, 600)
root.geometry('500x600')
root.option_add('*Font', DEFAULT_FONT)
root.configure(background=BACKGROUND_COLOR)


# Creating and positioning all the frames
selection_frm = tk.Frame(master=root, bg=BACKGROUND_COLOR)
selection_frm.pack(fill=tk.X, padx=10, pady=10)

version_type_frm = tk.Frame(master=selection_frm)
version_type_frm.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

creature_select_frm = tk.Frame(master=selection_frm, bg=BACKGROUND_COLOR)
creature_select_frm.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

dialogue_frm = tk.Frame(master=root, bg=HEADING_COLOR)
dialogue_frm.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=20, pady=10)


# Version selection
version_frm = tk.Frame(master=version_type_frm, bg=BACKGROUND_COLOR)
version_frm.pack(expand=True, fill=tk.BOTH)

version_heading_lbl = tk.Label(master=version_frm,
    text='Version',
    bg=HEADING_COLOR,
    fg=HEADING_TEXT_COLOR
    )
version_heading_lbl.pack(fill=tk.X)

for version in VERSIONS:
    version_button = tk.Button(master=version_frm,
        text=beautify_text(version),
        fg=TEXT_COLOR,
        )
    version_button.pack(fill=tk.X)


# Creature type selection
type_frm = tk.Frame(master=version_type_frm, bg=BACKGROUND_COLOR)
type_frm.pack(expand=True, fill=tk.BOTH)

type_heading_lbl = tk.Label(master=type_frm,
    text='Creature type',
    bg=HEADING_COLOR,
    fg=HEADING_TEXT_COLOR
    )
type_heading_lbl.pack(fill=tk.X)

for creature in CREATURES:
    type_button = tk.Button(master=type_frm,
        text=beautify_text(creature),
        fg=TEXT_COLOR,
        )
    type_button.pack(fill=tk.X)

# Creature listbox
creature_listbox_lbl = tk.Label(master=creature_select_frm,
    text='Creatures',
    bg=HEADING_COLOR,
    fg=HEADING_TEXT_COLOR
    )
creature_listbox_lbl.pack(fill=tk.X)
creature_scrollbar = tk.Scrollbar(creature_select_frm, orient=tk.VERTICAL)
creature_listbox = tk.Listbox(master=creature_select_frm,
    bd=0,
    bg=BLURB_COLOR,
    fg=TEXT_COLOR,
    font=LISTBOX_FONT,
    yscrollcommand=creature_scrollbar.set
)
creature_scrollbar.config(command=creature_listbox.yview)
creature_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
for i in range(20):
    creature_listbox.insert(tk.END, i)
creature_listbox.pack(expand=True, fill=tk.BOTH)

# Dialogue textbox
dialogue_lbl = tk.Label(master=dialogue_frm,
    text='Blathers',
    bg=HEADING_COLOR,
    fg=HEADING_TEXT_COLOR
    )
dialogue_lbl.pack(fill=tk.X)
dialogue_text = tk.Text(master=dialogue_frm,
    state=tk.DISABLED,
    bg=BLURB_COLOR,
    fg=TEXT_COLOR,
    wrap=tk.WORD
)
dialogue_text.pack(fill=tk.X)

root.mainloop()