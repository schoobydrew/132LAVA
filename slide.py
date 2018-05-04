#from Tkinter import *
import Tkinter as tk
import serial
from random import randint, seed
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
def createPhrase():
    s = genPass()
    generatedpass.config(text="{}".format(s))
def encryptPhrase():
    print "Test"
def longWord():
    print "BOY"
#main
window = tk.Tk()
window.title("LAVA")
backg = tk.Frame(master=window, width=500)
backg.pack()
#create slider
scale = Scale(window, from_=6, to=40, orient=HORIZONTAL)
scale.pack(side=BOTTOM)
#create button for generating a random phrase
generate = Button(window, text='Generate!', command=createPhrase)
generate.pack(side=BOTTOM)
#create button for dictionary thing that reginald does
#create label
generatedpass = Label(window, text="")
generatedpass.pack(side=TOP)
#create button for word phrase
dictionary = Button(window, text='WORDS!', command=longWord)
dictionary.pack(side=BOTTOM)
###
window.mainloop()
