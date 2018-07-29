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
""")#Prints the title screen


#END OF title_screen()


def save_manager_on_load() :#Defines a function called save_manager_on_load

    global new_game #Makes new_game usable outside of function
    global p_name #Makes p_name usable outside of function

    try: #If save doesn't exist, make it in the 'try', if it already exists, then load it in the 'except'
        open_save_file=open("save.txt","x") #Create 'open_save_file which opens save.txt and will only work if save.txt doesn't exist. If save.txt does exist, it will Error and go to the except

        p_name=input("Whats your name?")#Asks user for name

        open_save_file.write(str(p_name)+":1:1:10")#Thus writes the name, attack, defense and hp of the new character to the newly made save file


        open_save_file.close()#Closes save.txt , to save RAM and to allow it to be opened later on


        new_game=True #This means a new game tutorial function or whatever should be made and be run when this is True

    except FileExistsError: #When save creation fails, this happens, as this will seperate new saves from loading one by preventing overwrites
           
        print("Welcome back") #This is where the save should be read/loaded and stats + progress shoukd be got from here.

        new_game=False #This means a continue game function should be made and ran or whatever when this is False


#END OF save_manager_on_load()

def pull_stats_from_save():

    global p_name #Makes p_name usable outside of function
    global p_atk #Makes p_atk usable outside of function
    global p_def #Makes p_def usable outside of function
    global p_hp #Makes p_hp usable outside of function
    
    open_save_file=open("save.txt","r")#Opens save file in read+write mode
    stats_assignment_holder=open_save_file.read() #Holds all stats in a string
    stats_assignment_holder=stats_assignment_holder.split(":")#Splits each stat (name, atk etc.) into an array
    p_name=stats_assignment_holder[0]#Name is pulled from save file
    p_atk=stats_assignment_holder[1]#Attack is pulled from save file
    p_def=stats_assignment_holder[2]#Defense is pulled from save file
    p_hp=stats_assignment_holder[3]#HP is pulled from save file
    open_save_file.close()#Closes file for later use and to save RAM

#END OF pull_stats_from_save()

def save_the_game():#Defines the function save_the_game, this can be input into a dictionary so saving can happen on demand.
    open_save_file=open("save.txt","w")#Opens save file in read+write mode
    open_save_file.write(str(p_name)+":"+str(p_atk)+":"+str(p_def)+":"+str(p_hp))#Writes the current stats to the save file.
    open_save_file.close()#Closes save file to save RAM as this is typically the last use during code execution
    print("Game has been saved")#Gives confirmation that saving has happened. 
    
#END OF save_the_game()



def hub(): #Defines the function hub, this is where the game hub is.

    global fight_difficulty

    keep_playing=True
    
    fight_difficulty=int(1)#Sets default difficulty, in case difficulty isn't changed by user.
    
    while keep_playing==True:#As long as this condition is satisfied, the game will keep looping about until the user wants to finish the session
    
        mode_selection=input("Would you like to...\n[Fight] An Enemy\n[Save] Your Game\nChange the Enemy [Difficulty]\n[Finish] Game Session\n") #Input to decide game mode, and directs to a function.

        if mode_selection.lower()==("fight"): #When input is made all lowercase, if it is "fight", do the following

            e_name, e_atk, e_def, e_hp=create_an_enemy(fight_difficulty)
            initiate_fight_mode(fight_difficulty, e_name, e_atk, e_def, e_hp)

        elif mode_selection.lower()==("save"): #When input is made all lowercase, if it is "save", do the following
            save_the_game()#Runs the save_the_game() function

        elif mode_selection.lower()==("difficulty"): #When input is made all lowercase, if it is "difficulty", do the following
            fight_difficulty=change_difficulty(fight_difficulty)#Runs the save_the_game() function

        elif mode_selection.lower()==("finish"): #When input is made all lowercase, if it is "finish", do the following
            keep_playing=False #Ends the loop, allowing the game to quit
            
        else:
            print("Command not recognised. Please enter a valid input. Valid commands are in [] brackets.") #Tells user the command isn't recognised, and helps tell user what are valid commands.

#END OF hub()


def initiate_fight_mode(fight_difficulty, e_name, e_atk, e_def, e_hp):#Defines function
    print("\n\n\n\n\nEnemy Stats\nName: "+str(e_name)+" / Difficulty: "+str(fight_difficulty)+"\nHP: "+str(e_hp)+"\nAttack: "+str(e_atk)+"\nDefence: "+str(e_def))

#END OF initiate_fight_mode()


def change_difficulty(fight_difficulty):

    difficulty_set_successfully=False
    while difficulty_set_successfully==False:
        try:
            difficulty_input=int(input("Enemy difficulty is currently set to "+str(fight_difficulty)+"\nWhat would you like to set it to?\n"))
            difficulty_set_successfully=True
            print("Difficulty change is successful. Enemy difficulty is now "+str(difficulty_input))
            return difficulty_input
        except:
            ("Difficulty change is unsuccessful. Please input a valid whole number")

#END OF change_difficulty()

def create_an_enemy(fight_difficulty):
    global enemy_name
    global e_atk
    global e_def
    global e_hp

    import random
    
    open_enemy_file=open("enemies.txt","r")#Opens enemy file in read mode
    enemy_list=open_enemy_file.read()#Holds all enemies in a string
    enemy_list=enemy_list.split(";")#Make an array where each element is made by splitting the string by ";" eg a;b -> [a,b]
    enemy_total=len(enemy_list)

    e_name=enemy_list[random.randint(0,(enemy_total-1))]
    
    e_atk=int(fight_difficulty)
    e_def=int(fight_difficulty-1)
    e_hp=int(10*int(fight_difficulty))

    return e_name, e_atk, e_def, e_hp

#END OF create_an_enemy()



def tutorial():
    print("Tutorial is a WIP")#Indicates a new game is made, requiring a tutorial [TODO]


#END OF tutorial()



#_________________END OF FUNCTION DECLARING____________________________________________________________________________________________________________________

#_________________BEGINNING OF "CODE"____________________________________________________________________________________________________________________

title_screen()#Shows the title screen

save_manager_on_load()#Runs save_manager_on_load

pull_stats_from_save()#Runs pull_stats_from_save



if new_game == True: #This is true when a save file didn't exist at startup, so a new game is started and we make a tutorial or beginning
    tutorial()
    hub()
elif new_game == False: #This is true when a save file does exist at startup, so game is started and save is loaded.
    hub()

else:
    print("Error has occured: new_game is not True or False")#new_game's value is clearly not a Boolean, so this is an error saying its gone wrong


print("Now exiting")


























