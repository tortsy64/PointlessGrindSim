#_________________BEGINNING OF FUNCTION DECLARING____________________________________________________________________________________________________________________

def title_screen() :#Defines a function called title_screen
    print("""
Welcome to...
 _______________ 
|		|                                _ 
|     __________| 				| | 
|    |               				| | 
|    |   _______             _                  | | 
|    |	|	|  ________ |_|  _______    ____| | 
|    |	| ____  | |   _____| _  /  ___  \  |  __  | 
|    |       |	| |  |      | | | |   | |  | |  | | 
|    |_______|	| |  |      | | | |   | |  | |  | | 
|		| |  |      | | | |   | |  | |__| | 
\_______________/ \__/      \_/ \_/   \_/  |______| 
 _______________ 
/	        \ 
|     __________|  
|    | 
|    |__________   _  
|    		| |_| 
\____________   |  _.  _________ 
 ____        |	| | | /  _   _  \ 
|    |_______|	| | | | | | | | | 
|		| | | | | | | | | 
\_______________/ \_/ \_/ \_/ \_/ 
""")


#END OF title_screen()


def save_manager_on_load() :#Defines a function called save_manager_on_load

    global new_game #Makes new_game usable outside of function
    global name #Makes name usable outside of function

    try: #If save doesn't exist, make it in the 'try', if it already exists, then load it in the 'except'
        open_save_file=open("save.txt","x") #Create 'open_save_file which opens save.txt and will only work if save.txt doesn't exist. If save.txt does exist, it will Error and go to the except

        name=input("Whats your name?")#Asks user for name

        open_save_file.write(str(name)+":1:1:10")#Thus writes the name, attack, defense and hp of the new character to the newly made save file


        open_save_file.close()#Closes save.txt , to save RAM and to allow it to be opened later on


        new_game=True #This means a new game tutorial function or whatever should be made and be run when this is True

    except FileExistsError: #When save creation fails, this happens, as this will seperate new saves from loading one by preventing overwrites
           
        print("Welcome back") #This is where the save should be read/loaded and stats + progress shoukd be got from here.

        new_game=False #This means a continue game function should be made and ran or whatever when this is False


#END OF save_manager_on_load()

def pull_stats_from_save():

    global name #Makes name usable outside of function
    global p_atk #Makes p_atk usable outside of function
    global p_def #Makes p_def usable outside of function
    global p_hp #Makes p_hp usable outside of function
    
    open_save_file=open("save.txt","r+")#Opens save file in read+write mode
    stats_assignment_holder=(open_save_file.read()) #Holds all stats in a string
    stats_assignment_holder=stats_assignment_holder.split(":")#Splits each stat (name, atk etc.) into an array
    name=stats_assignment_holder[0]#Name is pulled from save file
    p_atk=stats_assignment_holder[1]#Attack is pulled from save file
    p_def=stats_assignment_holder[2]#Defense is pulled from save file
    p_hp=stats_assignment_holder[3]#HP is pulled from save file
    open_save_file.close()#Closes file for later use and to save RAM

#END OF pull_stats_from_save()

def save_the_game():#Defines the function save_the_game, this can be input into a dictionary so saving can happen on demand.
    open_save_file=open("save.txt","w")#Opens save file in read+write mode
    open_save_file.write(str(name)+":"+str(p_atk)+":"+str(p_def)+":"+str(p_hp))
    open_save_file.close()
    print("Game has been saved")
    



def game(): #Defines the function game, this is where the game is.
    print("Error 404: Game not found") #Placeholder to indicate function game has been activated [TODO]


def tutorial():
    print("Tutorial is a WIP")#Indicates a new game is made, requiring a tutorial [TODO]



#_________________END OF FUNCTION DECLARING____________________________________________________________________________________________________________________

#_________________BEGINNING OF "CODE"____________________________________________________________________________________________________________________

title_screen()

save_manager_on_load()#Runs save_manager_on_load
pull_stats_from_save()#Runs pull_stats_from_save



if new_game == True: #This is true when a save file didn't exist at startup, so a new game is started and we make a tutorial or beginning
    tutorial()
    game()
elif new_game == False: #This is true when a save file does exist at startup, so game is started and save is loaded.
    game()

else:
    print("Error has occured: new_game is not True or False")

save_the_game()






























