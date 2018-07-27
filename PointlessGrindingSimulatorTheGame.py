print("Placeholder") #Title Screen


def save_manager_on_load() :#Defines a function called save_manager_on_load

    try: #If save doesn't exist, make it in the 'try', if it already exists, then load it in the 'except'
        open_save_file=open("save.txt","x") #Create 'open_save_file which opens save.txt and will only
        open_save_file.close()#Closes save.txt , to save RAM and to allow it to be opened later on

    except FileExistsError: #When save creation fails, this happens, as this will seperate new saves from loading one by preventing overwrites
        
        print("Welcome back")#


save_manager_on_load()#Runs save_manager_on_load
