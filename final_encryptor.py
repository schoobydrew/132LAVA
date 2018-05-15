################################################################################
#                               Lava Lamp Encryptor                            #
#       Members: Andrew Schoonmaker, Reginald Thomas, and Landry Baudouin      #
#                                                                              #
#       Description: An Arduino takes values from a photoresistor that is      #
#       constantly watching a lava lamp.  The values are then sent to a        #
#       raspberry pi where they are used to seed either a long word from a     #
#       file, an inputted set of characters, or a random bunch of characters.  #
################################################################################
                    

from Tkinter import *
import serial
from random import randint, seed, choice
import time

# This can work without a raspberry pi, all you have to do is keep ARDUINO
# at False.  Otherwise replace that with true and some of the paths for the pi
# may need to be changed

ARDUINO = False
MIN_VALUE = 65
MAX_VALUE = 122

#create character list
characterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', \
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]


def getSliderValue():
    x = scale.get()
    return x


# this is so the Arduino and Raspberry Pi can communicate values
def getArduinoSeed():
    #ser = serial.Serial('/dev/ttyACM0', 9600) for USB communication
    ser = serial.Serial('/dev/ttyACM0', 9600)
    x = ser.readline()
    x = int(x[:3])
    x *= time.time()
    return


def copyPaste(a):
    #put the string on the clipboard for copy and paste!
    root.clipboard_clear()
    root.clipboard_append(a)

    
def genPass():
    x = getSliderValue()
    #create empty string to add too
    nitpick = ""
    for i in range(x):
        #grab the seed from arduino
        #generate random number for wordlist
        if ARDUINO:
            seed(getArduinoSeed())
        kabocha = randint(0, len(characterlist)-1)
        #adds a character
        pick = characterlist[kabocha]
        nitpick += pick
    return nitpick


def createString():
    s = genPass()
    generatedpass.config(text=s, foreground="red")
    copyPaste(s)

    
def encryptPhrase():
    newPass = ''
    # grabs the user created password from the textbox
    userPass = textbox.get()
    # loops through the characters in the password
    for char in userPass:
        # ASCII value of the character
        newCharValue = ord(char)
        # gives two options 0 and 1
        coinFlip = randint(0, 1)
        # if coin lands on 0, set to minimum and add a random
        # integer to the ASCII of the character
        if (coinFlip == 0):
            newCharValue = MIN_VALUE + randint(0, MAX_VALUE - MIN_VALUE)
        # if coin lands on 1, set to maximum and subtract a random
        # integer to the ASCII of the character
        else:
            newCharValue = MAX_VALUE - randint(0, MAX_VALUE - MIN_VALUE)
        # grabs the character value of the ASCII number
        # stores it
        newChar = chr(newCharValue)
        # adds the new character to the encrypted password
        newPass += newChar
    generatedpass.config(text=newPass, foreground="red")
    textbox.delete(0, END)
    copyPaste(newPass)


def longWord():
    #takes dictionary words to create a new phrase
    w = open('WordList.txt', 'r')
    words = w.read()
    word = words[0:]
    split = word.split()
    # you have to use choice instead of random.choice :/
    myWord1 = choice(split)
    myWord2 = choice(split)
    myWord3 = choice(split)

    combinedWords = ''.join([myWord1, myWord2, myWord3])
    generatedpass.config(text=combinedWords, foreground="red")
    copyPaste(combinedWords)


#main window
root = Tk()
#sizing, weight the columns to not move
root.geometry("400x200")
root.resizable(0,0)
root.configure(background="white")
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)
#label that we work with on the app
generatedpass = Label(root, text="Your string will appear here!", foreground="red")
generatedpass.config(font=("Courier", 8), background="white")
generatedpass.grid(row=0, column=1)
#create buttons
dictionary = Button(root, text="WORDS!", command=longWord, background="white", foreground="blue").grid(row=1, column=0)
generate = Button(root, text="RANDOM!", command=createString, background="white", foreground="blue").grid(row=1, column=1)
regString = Button(root, text="INPUT!", command=encryptPhrase, background="white", foreground="blue").grid(row=1, column=2)
#adds the scale
scale = Scale(root, from_=6, to=40, orient="horizontal")
scale.grid(row=2, column=1)
#adds the textbox and sets it to always allow input with the focus command
textbox = Entry(root)
textbox.grid(row=3, column=1)
textbox.focus()
root.mainloop()
