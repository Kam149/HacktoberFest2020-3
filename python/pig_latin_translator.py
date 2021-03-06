###############################################################################################################################
#A Pig Latin is an encrypted word in English, which is generated by doing following alterations:
#The first vowel occurring in the input word is placed at the start of the new word along with the remaining alphabets of it.
#The alphabets present before the first vowel are shifted at the end of the new word followed by “ay”.
#The objective is to conceal the words from others not familiar with the rules.
###############################################################################################################################


#IMPORTING LIBRARIES#
from tkinter import *
 
#Translator Function#
def pig_latin():
    consonant = (' B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y')
    vowel = ('A','E','I','O','U')

    pig_latin_string =''
    user_sentence = var.get()
    user_sentence = str(user_sentence)
    words = user_sentence.split()
    
    for user_word in words:
    # getting first letter and making sure its a string and setting it to uppercase
        first_letter = user_word[0]
        first_letter = str(first_letter)
        first_letter = first_letter.upper()
  
        if first_letter in consonant:
            length_of_word = len(user_word)
            remove_first_letter = user_word[1 : length_of_word]
            pig_latin = remove_first_letter + first_letter + 'ay'
            pig_latin_string = pig_latin_string + ' ' + pig_latin
        
        elif first_letter in vowel:
            pig_latin = user_word + 'way'
            pig_latin_string = pig_latin_string + ' ' + pig_latin
        
        else:
            pig_latin_string = 'INVALID INPUT!'
    var1.set(pig_latin_string)
    

#Tkinter root with window title#
root = Tk()
root.title("Pig Latin Translator")
root.resizable(0, 0) #Stops window from being resized


#Creating a Frame and Grid to hold the Content#
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)


 
#Text Box to take user input#
Label(mainframe, text = "Enter text").grid(row = 2, column = 0)
var = StringVar()
textbox = Entry(mainframe, textvariable = var).grid(row = 2, column = 1)
 
Label(mainframe, text = "Output").grid(row = 2, column = 2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable = var1).grid(row = 2, column = 3)

 
#Creating a button to call pig_latin function#
b = Button(mainframe, text = 'Translate', command = pig_latin).grid(row = 3, column = 1, columnspan = 3)
root.mainloop()
