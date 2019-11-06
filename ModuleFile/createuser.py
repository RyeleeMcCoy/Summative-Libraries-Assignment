#-----------------------------------------------------------------------
#Libraries Summative
#Ryelee McCoy
#November 5 2019
#
#--------------------------Functions/Lists------------------------------
#
#
#--------------------------Actual Code----------------------------------
def create_user():
    name = input("What is your username? ")
    race = input("What is your Race? ")
    weapon = input("What is your choice of weapon? ")
    file = name + "inventory" '.txt' #This creates a name that can be used with a file while using user input.
    save = open(file, 'w')#create the file with the user input, most likely will be their username.
    save.write("Race,")#All of the save.writes are saving the information into the newly created file.
    save.write(race + ",")
    save.write("Weapon,")
    save.write(weapon + ",")
    save.write("Health,")
    save.write("100,")
    save.write("Level,")
    save.write("1")