import tkinter as tk
from PIL import ImageTk, Image
import blathers

# Chalkboard, Nadeem, Gill Sans are all similar to AC font
FONT = 'Chalkboard'
BACKGROUND_IMAGE = 'images/background.png'
# RGB for textbox background: 254, 250, 230
TEXTBOX_COLOR = '#FEFAE6'
# RGB for font color: 138, 132, 110
FONT_COLOR = '#8A846E'
BLATHERS_IMAGE = 'images/Blathers_NH.png'

VERSIONS = blathers.Blathers.versions

def create_window():
    '''Sets up the gui window with sizing, background, textboxes, etc.'''
    global text_label, version, version_label

    window = tk.Tk()
    window.geometry('1280x720')
    window.resizable(0, 0)
    window.option_add('*Font', FONT + ' 26')

    background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_IMAGE))
    background_label = tk.Label(window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    version_frame = tk.Frame(master=window, width=350, height=115, bg=TEXTBOX_COLOR)
    version_frame.place(x=130, y=105)
    version_frame.columnconfigure([0, 1, 2], minsize=105)
    version_frame.rowconfigure([0, 1], minsize=50)
    row, column = 0, 0
    for version in VERSIONS:
        if column == 3:
            column = 0
            row += 1
        version = beautify_text(version)
        version_button = tk.Button(master=version_frame,
                text=version,
                font=FONT + ' 23',
                bg=TEXTBOX_COLOR,
                fg=FONT_COLOR,
                command=(lambda version: lambda: change_version(version))(version)
            )
        version_button.grid(row=row, column=column)
        column += 1

    version_label = tk.Label(master=window,
            text='Current: ' + beautify_text(version),
            bg=TEXTBOX_COLOR,
            fg=FONT_COLOR,
            font=FONT + ' 22'
        )
    print(version_label)
    version_label.place(x=220, y=65)

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

def main():
    create_window()

if __name__ == '__main__':
    main()
