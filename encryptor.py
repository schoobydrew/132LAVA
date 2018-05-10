from Tkinter import *

import serial

from random import randint, choice

#create character list

characterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \

't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', \

'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

#ser = serial.Serial('/dev/ttyACM0', 9600) for USB communication

#file path for USB

def getSliderValue():

    x = scale.get()

    print x

    return x

def genPass():

    x = getSliderValue()

    #create empty string to add too

    nitpick = ""

    for i in range(x):

        #grab the seed from arduino

        #generate random number for wordlist

        kabocha = randint(0, len(characterlist)-1)

        #adds a character

        pick = characterlist[kabocha]

        nitpick += pick

    return nitpick

def createString():

    s = genPass()

    generatedpass.config(text=s)

def encryptPhrase():

    #reginalds stuff this allows you to get from the textbox and display on the screen

    x = textbox.get()

    generatedpass.config(text=x)

    textbox.delete(0, END)

def longWord():

    w = open('WordList.txt', 'r')
    words = w.read()
    word = words[0:]

    split = word.split()
    # you have to use choice instead of random.choice :/
    myWord1 = choice(split)
    myWord2 = choice(split)
    myWord3 = choice(split)

    combinedWords = ''.join([myWord1, myWord2, myWord3])
    generatedpass.config(text=combinedWords)


# $ MAIN WINDOW $ #

root = Tk()

#sizing, weight the columns to not move

root.geometry("600x520")

root.resizable(0,0)

root.columnconfigure(0, weight=0)

root.columnconfigure(1, weight=1)

root.columnconfigure(2, weight=0)

#label that we work with on the app

generatedpass = Label(root, text="Your string will appear here!")

generatedpass.grid(row=0, column=1)

#create buttons

dictionary = Button(root, text="WORDS!", command=longWord).grid(row=1, column=0)

generate = Button(root, text="RANDOM!", command=createString).grid(row=1, column=1)

regString = Button(root, text="INPUT!", command=encryptPhrase).grid(row=1, column=2)

#adds the scale

scale = Scale(root, from_=6, to=40, orient="horizontal")

scale.grid(row=2, column=1)

#adds the textbox and sets it to always allow input with the focus command

textbox = Entry(root)

textbox.grid(row=3, column=1)

textbox.focus()

root.mainloop()
