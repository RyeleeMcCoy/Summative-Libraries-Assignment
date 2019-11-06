#-----------------------------------------------------------------------
#Libraries Summative
#Ryelee McCoy
#November 5 2019
#
#----------------------Imports/Functions/Lists--------------------------
from modules import createuser
from modules import characterscraper
from modules import changevalues
from modules import savecharacter
#--------------------------Actual Code----------------------------------
def main():#Calls all the functions to make the program work.
    createuser.create_user()
    filename = characterscraper.character_scraper()
    input("> ")
    changevalues.change_values()
    input("> ")
    savecharacter.save_character(filename)

    
main()