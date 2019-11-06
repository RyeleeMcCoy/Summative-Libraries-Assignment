#-----------------------------------------------------------------------
#Libraries Summative
#Ryelee McCoy
#November 5 2019
#
#--------------------------Functions/Lists------------------------------
from modules import characterscraper

#--------------------------Actual Code----------------------------------

def change_values():
    print("You are at level", characterscraper.user_details["Level"]) #Brings up what level they are from the previously created dictionary.
    print("You fought a creature and won! You leveled up but lost 25 Health")
    print("Your health is now at 75")
    print("--------------------------")
    print("LEVEL UP")
    print("--------------------------")
    print("You are now level 2!")
    characterscraper.user_details["Health"] = "75"#Changes the stats in the dictionary to save what they did.
    characterscraper.user_details["Level"] = "2"