import tkinter as tk
import blathers

MIN_WIDTH = 525
MIN_HEIGHT = 650

DEFAULT_FONT = 'Chalkboard 20'
LISTBOX_FONT = 'Chalkboard 18'
BLURB_COLOR = '#FEFAE6'
TEXT_COLOR = '#8A846E'
HEADING_COLOR = '#F3A5BC'
HEADING_TEXT_COLOR = 'white'
BACKGROUND_COLOR = '#D6F8E0'

VERSIONS = blathers.Blathers.versions
CREATURES = blathers.Blathers.creatures[:3]
GREETING = '''Welcome to the Blathers talkbot responsive GUI!
After making your selection, press enter to read the description!'''

VERSIONS_NO_SEA_CREATURES = VERSIONS[:3]


# Many utility and command functions are copied from gui_blathers.py, but I
# chose not to import it. This is because I named many things differently and
# importing those functions likely wouldn't work anyways given how they rely on
# global variables and bad practices.


def build_app():  # Probably better if this was a class.
    '''Builds the GUI.'''

    # Utility functions

    def beautify_text(string):
        '''Returns beautified form of Python/personal naming-convention string.'''
        return string.replace('_', ' ').replace('-', ' ').title()

    # Command functions for buttons / Functions that alter GUI

    def print_dialogue(string):
        '''Displays text in the dialogue textbox.'''
        dialogue_text.config(state=tk.NORMAL)
        dialogue_text.delete(1.0, tk.END)
        dialogue_text.insert(tk.END, string)
        dialogue_text.config(state=tk.DISABLED)

    def change_version(new_version):
        '''Changes the current version.'''
        nonlocal curr_version
        curr_version = new_version
        curr_version_lbl.config(text='Current: ' + beautify_text(new_version))
        update_type_buttons(curr_version)
        update_creature_list()

    def change_type(new_type):
        '''Changes the current creature type.'''
        nonlocal curr_creature_type
        curr_creature_type = new_type
        curr_type_lbl.config(text='Current: ' + beautify_text(new_type))
        update_creature_list()

    def update_type_buttons(version):
        '''Changes which buttons are present based on game version.'''
        if version in VERSIONS_NO_SEA_CREATURES:
            type_buttons['deep-sea_creature'].config(state=tk.DISABLED)
            if curr_creature_type == 'deep-sea_creature':
                change_type('fish')
        else:
            type_buttons['deep-sea_creature'].config(state=tk.NORMAL)

    def update_creature_list():
        '''Updates the creatures in the creature listbox.'''
        dialogues = blathers.get_version_creature_SQL_table(curr_version,
            curr_creature_type, connection)
        creature_listbox.delete(0, tk.END)
        for creature in dialogues:
            creature_listbox.insert(tk.END, creature)

    def get_creature_description():
        '''Gets creature description from SQL table.'''
        dialogues = blathers.get_version_creature_SQL_table(curr_version,
            curr_creature_type, connection)
        choice = creature_listbox.get(tk.ANCHOR)
        return dialogues[choice]

    def display_description():
        '''Displays the description in the textbox.'''
        description = get_creature_description()
        print_dialogue(description)

    # SQL stuff
    connection = blathers.connect_to_database('dialogue.db')

    # Creating root window
    root = tk.Tk()
    root.title('Blathers Talkbot Responsive GUI')
    root.minsize(MIN_WIDTH, MIN_HEIGHT)
    root.geometry(f'{MIN_WIDTH}x{MIN_HEIGHT}')
    root.option_add('*Font', DEFAULT_FONT)
    root.configure(background=BACKGROUND_COLOR)
    root.bind('<Return>', lambda x: display_description())


    # Creating and positioning all the frames
    selection_frm = tk.Frame(master=root, bg=BACKGROUND_COLOR)
    selection_frm.pack(fill=tk.X, padx=10, pady=10)

    version_type_frm = tk.Frame(master=selection_frm, bg=BACKGROUND_COLOR)
    version_type_frm.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

    version_frm = tk.Frame(master=version_type_frm,
        bg=BLURB_COLOR,
        highlightbackground=TEXT_COLOR,
        highlightthickness=1
    )
    version_frm.pack(expand=True, fill=tk.BOTH, pady=(0, 10))

    type_frm = tk.Frame(master=version_type_frm,
        bg=BLURB_COLOR,
        highlightbackground=TEXT_COLOR,
        highlightthickness=1
    )
    type_frm.pack(expand=True, fill=tk.BOTH)

    creature_select_frm = tk.Frame(master=selection_frm,
        bg=BLURB_COLOR,
        highlightbackground=TEXT_COLOR,
        highlightthickness=1
    )
    creature_select_frm.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    dialogue_frm = tk.Frame(master=root,
        bg=BLURB_COLOR,
        highlightbackground=TEXT_COLOR,
        highlightthickness=1
    )
    dialogue_frm.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=20, pady=10)


    # Version selection
    version_heading_lbl = tk.Label(master=version_frm,
        text='Version',
        bg=HEADING_COLOR,
        fg=HEADING_TEXT_COLOR
        )
    version_heading_lbl.pack(fill=tk.X, ipadx=100)

    curr_version_lbl = tk.Label(master=version_frm,
        text='Current: n/a',
        bg=BLURB_COLOR,
        fg=TEXT_COLOR
        )
    curr_version_lbl.pack(fill=tk.X)

    for version in VERSIONS:
        version_button = tk.Button(master=version_frm,
            text=beautify_text(version),
            fg=TEXT_COLOR,
            command = (lambda x: lambda: change_version(x))(version)
            )
        version_button.pack(fill=tk.X, padx=10, pady=(0, 3))


    # Creature type selection
    type_heading_lbl = tk.Label(master=type_frm,
        text='Creature type',
        bg=HEADING_COLOR,
        fg=HEADING_TEXT_COLOR
        )
    type_heading_lbl.pack(fill=tk.X)

    curr_type_lbl = tk.Label(master=type_frm,
        text='Current: n/a',
        bg=BLURB_COLOR,
        fg=TEXT_COLOR
        )
    curr_type_lbl.pack(fill=tk.X)

    type_buttons = {}
    for creature in CREATURES:
        type_button = tk.Button(master=type_frm,
            text=beautify_text(creature),
            fg=TEXT_COLOR,
            command = (lambda x: lambda: change_type(x))(creature)
            )
        type_buttons[creature] = type_button
        type_button.pack(fill=tk.X, padx=10, pady=(0, 3))

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
    creature_listbox.pack(expand=True, fill=tk.BOTH, padx=(5, 0))

    # Dialogue textbox
    dialogue_lbl = tk.Label(master=dialogue_frm,
        text='Blathers',
        bg=HEADING_COLOR,
        fg=HEADING_TEXT_COLOR
        )
    dialogue_lbl.pack(fill=tk.X)

    dialogue_scrollbar = tk.Scrollbar(dialogue_frm, orient=tk.VERTICAL)
    dialogue_text = tk.Text(master=dialogue_frm,
        state=tk.DISABLED,
        bg=BLURB_COLOR,
        fg=TEXT_COLOR,
        wrap=tk.WORD,
        highlightthickness=0,
        yscrollcommand=dialogue_scrollbar.set
    )
    dialogue_scrollbar.config(command=dialogue_text.yview)
    dialogue_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    dialogue_text.pack(fill=tk.X, padx=(10, 0))


    # Prepare content
    curr_version = VERSIONS[0]
    curr_creature_type = CREATURES[0]
    change_version(curr_version)
    change_type(curr_creature_type)
    update_creature_list()
    print_dialogue(GREETING)

    root.mainloop()

if __name__ == '__main__':
    build_app()
