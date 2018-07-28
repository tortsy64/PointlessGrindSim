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


def save_manager_on_load() :#Defines a function called save_manager_on_load

    global new_game #Makes new_game usable outside of function

    try: #If save doesn't exist, make it in the 'try', if it already exists, then load it in the 'except'

        open_save_file=open("save.txt","x") #Create 'open_save_file which opens save.txt and will only check if it doesn't exist.
        open_save_file.close()#Closes save.txt , to save RAM and to allow it to be opened later on


        new_game=True #This means a new game tutorial function or whatever should be made and run when this is True

        #Run NewGame function [TODO]

    except FileExistsError: #When save creation fails, this happens, as this will seperate new saves from loading one by preventing overwrites
        
        print("Welcome back") #This is where the save should be read/loaded and stats + progress shoukd be got from here.

        new_game=False #This means a continue game function should be made and ran or whatever when this is False

        #Run LoadGame functiom[TODO]


save_manager_on_load()#Runs save_manager_on_load

title_screen()

if new_game == False: #This is false when a save file exists, and is first because load save is more likely than new game save.
    print("This is where we load the game, but not right now. It's a WIP") #Loads the game [TODO]

elif new_game == True: #This is true when a save file didn't exist at startup, so a new game is started and we make a tutorial or beginning
    print("This is where we do the tutorial, but not right now. It's a WIP")#Begins the game [TODO]
