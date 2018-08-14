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
\____________   |  _   _________ 
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
    
    open_save_file=open("save.txt","r")#Opens save file in read+write mode
    stats_assignment_holder=open_save_file.read() #Holds all stats in a string
    stats_assignment_holder=stats_assignment_holder.split(":")#Splits each stat (name, atk etc.) into an array
    p_name=stats_assignment_holder[0]#Name is pulled from save file
    p_atk=stats_assignment_holder[1]#Attack is pulled from save file
    p_def=stats_assignment_holder[2]#Defense is pulled from save file
    p_hp=stats_assignment_holder[3]#HP is pulled from save file
    open_save_file.close()#Closes file for later use and to save RAM

    return p_name, p_hp, p_atk, p_def 

#END OF pull_stats_from_save()

def save_the_game():#Defines the function save_the_game, this can be input into a dictionary so saving can happen on demand.
    open_save_file=open("save.txt","w")#Opens save file in read+write mode
    open_save_file.write(str(p_name)+":"+str(p_atk)+":"+str(p_def)+":"+str(p_hp))#Writes the current stats to the save file.
    open_save_file.close()#Closes save file to save RAM as this is typically the last use during code execution
    print("Game has been saved")#Gives confirmation that saving has happened. 
    
#END OF save_the_game()



def hub(p_name, p_hp, p_atk, p_def ): #Defines the function hub, this is where the game hub is.

    global fight_difficulty

    keep_playing=True
    
    fight_difficulty=int(1)#Sets default difficulty, in case difficulty isn't changed by user.
    
    while keep_playing==True:#As long as this condition is satisfied, the game will keep looping about until the user wants to finish the session
    
        mode_selection=input("Would you like to...\n[Fight] An Enemy\n[Save] Your Game\nChange the Enemy [Difficulty]\n[Finish] Game Session\n") #Input to decide game mode, and directs to a function.

        if mode_selection.lower()==("fight"): #When input is made all lowercase, if it is "fight", do the following

            e_name, e_atk, e_def, e_hp=create_an_enemy(fight_difficulty)
            p_hp, p_atk, p_def=initiate_fight_mode(fight_difficulty, p_name, p_hp, p_atk, p_def, e_name, e_atk, e_def, e_hp)

        elif mode_selection.lower()==("save"): #When input is made all lowercase, if it is "save", do the following
            save_the_game()#Runs the save_the_game() function

        elif mode_selection.lower()==("difficulty"): #When input is made all lowercase, if it is "difficulty", do the following
            fight_difficulty=change_difficulty(fight_difficulty)#Runs the change_difficulty() function, sending fight_difficulty into it to show current difficulty

        elif mode_selection.lower()==("finish"): #When input is made all lowercase, if it is "finish", do the following
            keep_playing=False #Ends the loop, allowing the game to quit
            
        else:
            print("Command not recognised. Please enter a valid input. Valid commands are in [] brackets.") #Tells user the command isn't recognised, and helps tell user what are valid commands.

#END OF hub()


def initiate_fight_mode(fight_difficulty, p_name, p_hp, p_atk, p_def, e_name, e_atk, e_def, e_hp):#Defines function
    print("\n\n\n\n\nEnemy Stats\nName: "+str(e_name)+" / Difficulty: "+str(fight_difficulty)+"\nHP: "+str(e_hp)+"\nAttack: "+str(e_atk)+"\nDefence: "+str(e_def))
    import random

    p_maxhp=p_hp
    e_maxhp=e_hp

    battle_finished=False
    while battle_finished==False:
        print("\n\n\n\n\nEnemy Stats\nName: "+str(e_name)+" / Difficulty: "+str(fight_difficulty)+"\nHP: "+str(e_hp)+"/"+str(e_maxhp)+"\nAttack: "+str(e_atk)+"\nDefence: "+str(e_def))
        
        print("\n\n\n\n\nPlayer Stats\nName: "+str(p_name)+"\nHP: "+str(p_hp)+"/"+str(p_maxhp)+"\nAttack: "+str(p_atk)+"\nDefence: "+str(p_def))



        fight_command=input("""Would you like to...
    Attack? (Type [1])
    Escape? (Type [2])
    """)  #User input to decide action in battle
        if fight_command==("1"):
      
            player_damage_dealt =p_atk - e_def #Determines damage dealt by the player
            if player_damage_dealt < 0: #If it is negative damage...
                player_damage_dealt=0 #...Set to 0, to prevent negative damage

            enemy_damage_dealt =e_atk - p_def #Determines damage dealt by the enemy
            if enemy_damage_dealt < 0:#If it is negative damage...
                enemy_damage_dealt=0 #...Set to 0, to prevent negative damage

            p_hp=p_hp-enemy_damage_dealt
            
            e_hp=e_hp-player_damage_dealt

            if p_hp<=0:
                battle_finished=("Failed")

            if e_hp<=0:
                battle_finished=True
            
             
        elif fight_command==("2"):
            battle_finished=("Escaped")

        else:
            print("Invalid Command. Please type a number associated to a command above, without brackets")



    if battle_finished==True:
        p_hp=p_maxhp #Resets HP to max
 
        p_hp=stat_roulette(p_hp,fight_difficulty)
        p_atk=stat_roulette(p_atk,fight_difficulty)
        p_def=stat_roulette(p_def,fight_difficulty)

        print("HP is currently "+str(p_hp))
        print("Attack is currently "+str(p_atk))
        print("Defense is currently "+str(p_def))

    elif battle_finished==("Escaped"):
        print("You successfully escaped!")
        p_hp=p_maxhp #Resets HP to max

    elif battle_finished==("Failed"):
        print("You died!")
        p_hp=p_maxhp #Resets HP to max

    return p_hp, p_atk, p_def

        
#END OF initiate_fight_mode()


def change_difficulty(fight_difficulty):

    difficulty_set_successfully=False
    while difficulty_set_successfully==False:
        try:
            difficulty_input=int(input("Enemy difficulty is currently set to "+str(fight_difficulty)+"\nWhat would you like to set it to?\n"))
            if (difficulty_input!=0) and (str(difficulty_input).strip("-")==str(difficulty_input)):
                print("Difficulty change is successful. Enemy difficulty is now "+str(difficulty_input))
                difficulty_set_successfully=True
                return difficulty_input
            else:
                print("Error, difficulty is negative or zero. Please input a positive, whole number")
        except ZeroDivisionError:
            ("Difficulty change is unsuccessful. Please input a positive, whole, non-zero number")

#END OF change_difficulty()

def create_an_enemy(fight_difficulty):
    
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

def stat_roulette(stat,fight_difficulty):
    fight_difficulty=fight_difficulty*random.randint(1,50)
    stat_bonus=fight_difficulty//100
    stats_roulette_result=random.randint(0,99)
    if fight_difficulty%100>stats_roulette_result:
        stat_bonus+=1
    stat=stat+stat_bonus 
    return stat

#END OF stat_roulette()





def tutorial():
    print("""_____Tutorial is a WIP____________
The harder the enemy, the more likely you are to gain stats after battle,
but its random whether you do so keep grinding until you get stronger.
You can fight, you can save but please don't hurt each other.

And if you already have an old save file and are seeing this,
copy your old save.txt from the old game folder!

Have fun playing this WIP mess!


""")#Indicates a new game is made, requiring a tutorial [TODO]


#END OF tutorial()



#_________________END OF FUNCTION DECLARING____________________________________________________________________________________________________________________

#_________________BEGINNING OF "CODE"____________________________________________________________________________________________________________________

import random
    

title_screen()#Shows the title screen

save_manager_on_load()#Runs save_manager_on_load

p_name, p_hp, p_atk, p_def =pull_stats_from_save()#Runs pull_stats_from_save

p_hp=int(p_hp)
p_atk=int(p_atk)
p_def=int(p_def)


if new_game == True: #This is true when a save file didn't exist at startup, so a new game is started and we make a tutorial or beginning
    tutorial()
    hub(p_name, p_hp, p_atk, p_def )
elif new_game == False: #This is true when a save file does exist at startup, so game is started and save is loaded.
    hub(p_name, p_hp, p_atk, p_def )

else:
    print("Error has occured: new_game is not True or False")#new_game's value is clearly not a Boolean, so this is an error saying its gone wrong


print("Now exiting")


























