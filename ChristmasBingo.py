#! python3
# ChristmasBingo.py

import random
from tkinter import *

words = ['Mary', 'Joseph', 'Jesus', 'Frosty', 'Manger', 'Presents', 'Snow', 'Chimney', 'Fireplace', 'Star', 'Garland', 'Ornaments',
         'Tinsel', 'Mistletoe', 'Church', 'Carols', 'Santa', 'Candy Cane', 'Sledding', 'Elf', 'North Pole', 'Rudolph', 'Hot Cocoa',
         'Wise Men', 'Nativity', 'Bethlehem', 'Stockings', 'Gingerbread', 'Egg Nog', 'Lights', 'Donkey', 'Wreath', 'Nice List',
         'Sprinkles', 'Cookies', 'Noel', 'Angel', 'Mittens', 'Silver Bells', 'Holly', 'Gift Wrap', 'Grinch', 'Drummer Boy', 'Icicles',
         'Marshmallows', 'Nutcracker', 'Frankincense', 'Silent Night', 'Chestnuts']

def CreateCard():
    global text
    card = random.sample(words, 24)
    text.insert(END, '\n\n')
    text.insert(END, card[0] + ' | ' + card[1] + ' | ' + card[2] + ' | ' + card[3] + ' | ' + card[4] + '\n')
    text.insert(END, '--------------------------------------------------------------\n')
    text.insert(END, card[5] + ' | ' + card[6] + ' | ' + card[7] + ' | ' + card[8] + ' | ' + card[9] + '\n')
    text.insert(END, '--------------------------------------------------------------\n')
    text.insert(END, card[10] + ' | ' + card[11] + ' | FREE SPACE | ' + card[12] + ' | ' + card[13] + '\n')
    text.insert(END, '--------------------------------------------------------------\n')
    text.insert(END, card[14] + ' | ' + card[15] + ' | ' + card[16] + ' | ' + card[17] + ' | ' + card[18] + '\n')
    text.insert(END, '--------------------------------------------------------------\n')
    text.insert(END, card[19] + ' | ' + card[20] + ' | ' + card[21] + ' | ' + card[22] + ' | ' + card[23] + '\n\n')
    text.yview(END)


def draw():
    global text
    if len(words) == 0:
        text.insert(END, 'All Words have been drawn!\n')
        text.yview(END)
    else:
        drawn = random.choice(words)
        words.remove(drawn)
        text.insert(END, drawn + '\n')
        text.yview(END)


def reset():
    global words
    global text
    words = ['Mary', 'Joseph', 'Jesus', 'Frosty', 'Manger', 'Presents', 'Snow', 'Chimney', 'Fireplace', 'Star', 'Garland', 'Ornaments',
             'Tinsel', 'Mistletoe', 'Church', 'Carols', 'Santa', 'Candy Cane', 'Sledding', 'Elf', 'North Pole', 'Rudolph', 'Hot Cocoa',
             'Wise Men', 'Nativity', 'Bethlehem', 'Stockings', 'Gingerbread', 'Egg Nog', 'Lights', 'Donkey', 'Wreath', 'Nice List',
             'Sprinkles', 'Cookies', 'Noel', 'Angel', 'Mittens', 'Silver Bells', 'Holly', 'Gift Wrap', 'Grinch', 'Drummer Boy', 'Icicles',
             'Marshmallows', 'Nutcracker', 'Frankincense', 'Silent Night', 'Chestnuts']
    random.shuffle(words)
    text.insert(END, 'New Round: Clear your Boards!\n')
    text.insert(END, '---------------------------------------\n')
    text.yview(END)


root = Tk()
root.title('Christmas Bingo')
root.geometry('650x500')

#TextBox
text = Text(root, background='#101010', foreground='#D6D6D6', borderwidth=18, relief='sunken', width=20, height=15, wrap=WORD, font=('Purisa', 15))
text.insert(END, "Welcome to Christmas Bingo!\n\n")
text.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky=N+S+E+W)

#TextBox Tags
text.tag_add("alignment", "1.0", "end")
text.tag_configure("alignment", justify=CENTER)

text.tag_add("title", "1.0", "1.27")
text.tag_configure("title", foreground="red", underline=1)

#Stretch to fit
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

#Buttons
Button(root, text = 'Draw', fg = 'green', command = draw).grid(row = 3, column = 0, sticky=N+S+E+W)
Button(root, text = 'Reset', fg = 'orange', command = reset).grid(row = 3, column = 1, sticky= N+S+E+W)
Button(root, text = 'Create Card', fg = 'Blue', command = CreateCard).grid(row = 3, column = 2, sticky= N+S+E+W)
Button(root, text = 'Quit', fg = 'red', command = quit).grid(row = 3, column = 3, sticky= N+S+E+W)

root.mainloop()

