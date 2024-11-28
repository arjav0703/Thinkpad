# IMPORT LIBRARIES
from tkinter import *
from tkinter import filedialog

toor=Tk() # assign it to the tkinter() library

toor.geometry('600x600') # set window dimentions
toor.resizable(False,False)
toor.title('Thinkpad')


# configure Background
toor.config(background='lightblue')

def savefile():
    openfile = filedialog.asksaveasfile(mode= 'w', defaultextension='.txt')
    if openfile is None:
        return
    to_be_written=str(string.get(1.0,END))
    openfile.write(to_be_written)
    openfile.close    
    

def openfile():
    file_to_open = filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])

    if file_to_open is None:
        stuff = file_to_open.read()
    string.insert(INSERT,stuff)

    

#set buttons
save_button = Button(toor,width='5',height='1',bg='#fff',text='Save',command=savefile).place(x=5,y=5)
open_button = Button(toor,width='5',height='1',bg = '#fff', text='Open' ,command=openfile).place(x=80,y=5)

string = Text(toor,height='31',width='63', wrap = WORD,font='arial')
string.place(x=13,y=50)
toor.mainloop()