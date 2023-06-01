import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# Create a GUI app
from Model import Model_main

app = tk.Tk()

# Specify the title and dimensions to app
app.title('Tkinter Dialog')
app.geometry('1000x500')
app['background']='#0A2B35'

# Create a textfield for putting the
# text extracted from file
text=tk.Text(app,width = 60, height=4, font=("Helvetica", 32))
# Specify the location of textfield
text.grid(column=50, row=50, sticky='nsew')

HPath = []
VPath = []
# Create a function to open the file dialog


def open_text_file1():
    # Specify the file types
    filetypes = (('text files', '*.txt'),
                 ('All files', '.'))

    # Show the open file dialog by specifying path
    f = fd.askopenfile(filetypes=filetypes,
                       initialdir="C:/Users/abdal/PycharmProjects/HCI_project/Test")

    # Insert the text extracted from file in a textfield
    HPath.append(str(os.path.abspath(f.name)))

def open_text_file2():
    # Specify the file types
    filetypes = (('text files', '*.txt'),
                 ('All files', '.'))

    # Show the open file dialog by specifying path
    f = fd.askopenfile(filetypes=filetypes,
                       initialdir="C:/Users/abdal/PycharmProjects/HCI_project/Test")

    # Insert the text extracted from file in a textfield
    VPath.append(str(os.path.abspath(f.name)))


def GetResult():
    text.delete('1.0' , 'end')
    move = Model_main(HPath[len(HPath)-1],VPath[len(VPath)-1])
    if move == 'Up':
        move = '\n \t \t    Eat'
    elif move == 'Down':
        move = '\n \t \t    Drink'
    elif move == 'Right':
        move = '\n \t \t    Sleep'
    elif move == 'Left':
        move = '\n \t \t    Bathroom'
    elif move == 'Blink':
        move = '\n \t \t    Blink'

    text.insert('1.0', str(move))



# Create an open file button
open_button = ttk.Button(app, text='Open File',
                         command=open_text_file1).place(x=400,y=300)

label1 = ttk.Label(app, text='Enter horizontal signal : ').place(x=150,y=300)

open_button2 = ttk.Button(app, text='Open File',
                         command=open_text_file2).place(x=400,y=400)

label2 = ttk.Label(app, text='Enter vertical signal : ').place(x=150,y=400)


open_button3 = ttk.Button(app, text='Get result',
                         command=GetResult).place(x=750,y=300)

# Specify the button position on the app

# Make infinite loop for displaying app on the screen
app.mainloop()