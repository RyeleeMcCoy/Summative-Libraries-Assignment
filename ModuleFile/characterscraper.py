#-----------------------------------------------------------------------
#Libraries Summative
#Ryelee McCoy
#November 5 2019
#
#--------------------------Functions/Lists------------------------------
user_details = {}

#--------------------------Actual Code----------------------------------
def character_scraper():   
    user_name = input("What user would you like to open? ") #Asks the user for their username to open their file.
    file = user_name + "inventory" '.txt' #This creates a name that can be used with a file while using user input.
    details = open(file, 'r')#Creates the file with the user input, most likely will be their username.
    user_profile = details.read().split(',') #This goes into the file and splits the information between commas to make it into a dictionary.
    print(user_profile) #Prints the newly made dictionary from the file.
    item = 0
    while item < (len(user_profile)): #Whole while statement helps create the information into a useable dictionary.
        user_details[user_profile[item]] = user_profile[item + 1]
        item = item + 2
    details.close() #Closes the file.
    return file #Returns the list needed for later.