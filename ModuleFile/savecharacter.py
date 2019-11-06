#-----------------------------------------------------------------------
#Libraries Summative
#Ryelee McCoy
#November 5 2019
#
#--------------------------Functions/Lists------------------------------
from modules import characterscraper

#--------------------------Actual Code----------------------------------
def save_character(file):     #Function: Takes all the information that was changed and what not and saves it back into the file to be used for a later date.
    with open (file, 'w') as f: 
        for akey in characterscraper.user_details.keys(): 
            f.write(akey + ",")
            f.write((characterscraper.user_details[akey]))
            if akey != "Level":
                f.write(",") 