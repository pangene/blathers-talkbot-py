import tkinter as tk
from PIL import ImageTk, Image

# Chalkboard, Nadeem, Gill Sans are all similar to AC font
FONT = '', 
BACKGROUND_IMAGE = 'images/background.png'
# RGB for textbox background: 254, 250, 230
TEXTBOX_COLOR = '#FEFAE6'
# RGB for font color: 138, 132, 110
FONT_COLOR = '#8A846E'
BLATHERS_IMAGE = 'images/Blathers_NH.png'

def startup():
    '''Sets up the gui window with sizing, background, textboxes, etc.'''
    global text_label

    window = tk.Tk()
    window.geometry('1280x720')
    window.columnconfigure(0, minsize=1280)
    window.rowconfigure([0, 1, 2], minsize=235)
    window.resizable(0, 0)
    window.option_add('*Font', 'Chalkboard 26')

    background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_IMAGE))
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    textbox_frame = tk.Frame(master=window,
            width=700,
            height=150,
            bg=TEXTBOX_COLOR
        )
    textbox_frame.grid(row=2,column=0)
    textbox_frame.grid_propagate(False)
    text_label = tk.Label(textbox_frame,
            text='',
            anchor='w',
            bg=TEXTBOX_COLOR,
            fg=FONT_COLOR,
            wraplength=680,
            justify='left',
        )

    display_text("Welcome to the Blathers talkbot GUI! Press enter to proceed.")
    text_label.grid(sticky='w')
    window.mainloop()

def display_text(string):
    text_label['text'] = string


def main():
    startup()

if __name__ == '__main__':
    main()
