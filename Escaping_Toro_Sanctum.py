'''
Tyler Toro
Justice Through Code - Spring 2021

Welcome to my first project, Escaping Toro Sanctum. This is a text based adventure game with user interactivity. Toro Sanctum is a 
fictional bioengineering facility where the user is placed. The objective of the game is to follow the storyline and choose the correct 
path that will lead to locating an exit and finding the lost group, Team Bravo. The user is the team leader of Alpha Team, and the story
is updated based on the user input. 

The code is sectioned off with the hash "#" character and labeled

There are several questions posed to the user in the "user info" section of the script. The user provides:
    - Name
    - weight
    - favorite color
    - Special item
    - Someone they admire
    - A city they plan to travel to
    - Country leasT likely to travel to

///Name - The name provided is stored in the variable, user_name, and is plugged throughout the dialogue and storyline. This adds
to the interactive experience.

///weight - The user weight, which is checked with the defined "input_weight" function. This function will determine if the input
is an integer, and will continue to ask until an integer is provided. The only instance user weight comes into play is during the 
Elevator path, after Mission Objective. When the user attempts to rappel down an elevator shaft, the maximum weight is calculated
at [user_weight - 20], which results in game over.

///Favorite Color - the user inputs their favorite color, and the input is plugged into the scenery. For example, when traveling 
down the main stairs in the Basement path (the correct path), the "user_color" is used to describe the lights. It is a cue showing
they are at an important part of the story. In the lab, the user_color is described as scattered, a cue that something is wrong. 
The Lab path leads to game over & a retry.

///Special Item - The user is asked to pick an item out of three options (a coin, locket, or compass). This item only comes into
play during the Lab path, where the item falls out of the pocket of the user and rolls out of the lab, a cue to LEAVE. The user
input is converted from "1, 2, or 3" and stored as the correct string "A Coin..A locket etc" . If the user does not enter a correct
response in the "user info" section, nothing is stored as their item, and the print statement skips to "pass"

///Idol - The user is asked to provide someone they look up to; this input is stored as a string and used to create Bravo Team leaders
name at the end of the game. 

///City - The user is asked to name a city they would like to visit. This input is stored as a string, and used to generate the name of
the fictional island where the Toro Sanctum research facility is located

///Country - The user is asked to provide the name of a country they would least likely travel to. This input is stored as a string, and used 
to generate the location from which both teams originate. This is a bit of humor, forcing the user to have traveled where they least expected to.

The basic decision tree of the game



                      (Escaping Toro Sanctum)
                                 |
                            (User info)
                                 |
                       (Introduction: Start?)
                                 |
                 (Mission Objective: Will you Search..?)
                                /|\
                               / | \
                              /  |  \
                            /    |    \
                          /      |      \
                        /        |        \
             (Basement)        (Lab)      (Elevator) 
                  /|             |             \
               /   |             |              |
              /    |             |              |
   (Dry Storage)   |             |          *loss*+ retry
     <Unit A>      |             |                 
      *Win*        |             |                      
                   |             |                        
              (Freezer)          |                         
               <Unit B>          |                          
          *loss*+ retry          |                        
                                 /\                      
                               /    \                   
                             /        \                   
                          /              \              
                (Emergency Exit)        (Return to Basement)
                        |                       |
                   *loss*+ retry            (Basement)

The only win is choosing the Basement, then Dry Storage Unit A. However, when faced with an end game situation, the user is asked if
they want to try again. If their input is y, for yes, the defined "escaping_sanctum()" function is executed, which asks the question:

   Will you search for Bravo Team and Escape Toro Sanctum?


///Defined Functions///:

header() - this function prints the Escaping Toro Sanctum banner

pause() - this function waits until the user hits <enter> to continue, allowing them to read previous story or before a decision. 

input_weight() - this function checks for correct user input. If an integer is not entered for weight, the question repeats.

starting_question() - this function asks the user if they would like to continue, after providing input

introduction() - this function is the backstory of Escaping Toro Sanctum, soley a print function

escaping_sanctum() - this function asks the user "Will you search for Bravo Team and Escape Toro Sanctum?" and starts the game. This
function also serves as a "Retry" point, so the user can attempt to beat them game in one session.

escaping_sanctum1() - After selecting "y" to play, this function starts the game and leads to the 3 possible paths. The incorrect 
path "Elevator" is at the end of this function, with "Lab" and "Basement" forked out of this function. User is faced with 3 options.

escaping_sanctum2_1() - Basement Path, user is faced with 2 options

escaping_sanctum2_1A() - Freezer path, with game over and retry message

escaping_sanctum2_1B() - Dry Storage path, the correct destination and game win

escaping_sanctum2_2() - Laboratory Path, user is faced with 2 options

escaping_sanctum2_2A() - Emergency exit path, game over with retry. 

escaping_sanctum2_2B() - Path executes the escaping_sanctum2_1() function, returning to basement


/// How many questions posed to user??
Over the course of the game, the user is asked 11 questions if they choose just the correct paths from start to finish. Several more questions will be asked
of the user if they face a game over screen. Many of the defined functions are paths, with several chances to return to a previous "fork in the road". 
If the user chooses not to play at any point, a game over screen will print followed by an "sys.exit()" function to stop the program. 


///Imported default Python Libraries:
sys, time, os

sys - Used for system specific functions, ie sys.stdout.write() writes on the terminal
time - Used to manipulate and access time functions, ie time.sleep used for delay
os - Used for misc. operating system interfaces. I originally wanted to use os.exit to close terminal/powershell but could not figure it out

///Time Variables

slow = 2.5 seconds, for slow delay
dia = 0.1 seconds, for dialogue
quick = 0.01 seconds, for very fast text display
step = 1 second, for small delay


///References:
I would like to thank Tim Statler from CompSciCentral (compscicentral.com) and their youtube tutorial
"Simple Python Project | Text-Based Adventure Game: Time Unraveled" for assisting me in learning the basics of a text-based game.
<https://www.youtube.com/watch?v=ypNFNr72Xe8>

The simple pause() function was helpful in learning, there are many ways to make a user press a key before continuing. This webpage 
was a great source.
https://stackoverflow.com/questions/11552320/correct-way-to-pause-a-python-program

The input_weight() function was a long experiment, with thanks to a contributor on stackoverflow.com. I needed my function to make sure the
user inputs an integer for weight, because their weight it used in the story. Upon customizing the example on that webpage a bit, I was
able to make it work.
https://stackoverflow.com/questions/20095244/how-do-i-check-if-input-is-a-number-in-python



                   .... ............... ..........................
                   .. ......................... .......... .......
                   ...... ..... ......... ........................
                   ..........  Escaping Toro Sanctum...... .......
                   ........ ............... ............... ......
                   :::::::::::::::::::::::::::::::::::::::::::::::
                   :::::::::::::::::::::::::::::::::::::::::::::::

Esacping Toro Sanctum ® is a work of fiction. Characters, names, businesses, locations, events, and incidents are products of the authors 
and co-authors(you, the user) imagination. Any resemblance to actual persons, both living or dead, or actual events is purely coincidental"


'''
import sys
import time
import os

slow = 2.5
dia = 0.1
quick = 0.01
step = 1
#time variables in time.sleep() functions

def header():
    print("  \t\t   .... ............... ..........................")
    time.sleep(dia)
    print("  \t\t   .. ......................... .......... .......")
    time.sleep(dia)
    print("  \t\t   ...... ..... ......... ........................")
    time.sleep(dia)
    print("  \t\t   .........  Escaping Toro Sanctum...... ........")
    time.sleep(dia)
    print("  \t\t   ........ ............... ............... ......")
    time.sleep(dia)
    print("  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::")
    time.sleep(dia)
    print("  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\n\n")
# header

def pause():
    pausing = input("  press <enter> to continue...")


###### CAMPAIGN START - First choices ##############################################
####################################################################################
####################################################################################


def escaping_sanctum1():
    time.sleep(slow)
    print("\n\nAlpha team continues onward, moving past the lobby. The polished linoleum floors reflect each movement.")
    time.sleep(step)
    print("The dim emergency lights flicker, drawing the attention of the team. The rain becomes more faint as they")
    time.sleep(step)
    print("reach the elevator and staircase section at the end of the empty lobby.")
    time.sleep(slow)
    print(f"There is a sudden muffled sound that freezes {user_name} in their tracks\n")
    pause()
    t0 = "\n\n...<<distant radio static>>..\n"
    for letter in t0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*2)
    time.sleep(step)
    t1 = f"\n\t({user_name}): \"Team Alpha! Hold, I hear something..\"\n"
    for letter in t1:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(step)
    t2 = "\n.......\n"
    for letter in t2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*2)
    time.sleep(step)
    t3 = "\n..<<static>>..\n"
    for letter in t3:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*1.5)
    time.sleep(step)    
    t4 = f"\n(???):  ..\"hel-\"..\n"
    for letter in t4:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*1.5)
    time.sleep(step)
    t5 = f"\n\t({user_name}): \"Its coming from the elevator shaft...\"\n"
    for letter in t5:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    print()
    time.sleep(slow)
    escaping_sanctum2 = input("\nWhat will you do next?\n\
    [Select 1, 2, or 3 then press <enter> ]\n\n\
    1) Use the main stairs and search the basement?\n\
    2) Head towards the emergency exit through the lab?\n\
    3) Rappel down the elevator shaft?\n")
    if escaping_sanctum2 == "1":
        time.sleep(slow)
        escaping_sanctum2_1()
    elif escaping_sanctum2 == "2":
        time.sleep(slow)
        escaping_sanctum2_2()
    elif escaping_sanctum2 == "3":
        time.sleep(step)
        print(f"\n{user_name} leads the Team towards the center elevator and peers into the slightly opened doors")
        time.sleep(slow)
        t_3_1 = f"\n\t({user_name}): \"Thats a long way down...hook me up to that safety latch. I'm going down. Cover me\"\n"
        for letter in t_3_1:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(dia)
        time.sleep(slow)
        print(f"\nAfter securing the tactical rope, {user_name} slowly makes their decent..")
        time.sleep(slow)
        print("Once inside the poorly lit elevator shaft, a small sign comes into view..\n")
        pause()
        print("\n\n")
        time.sleep(slow)
        t_3_2= f"WARNING: MAXIMUM WEIGHT FOR LATCH {(int(user_weight)-20)} LBS..."
        for letter in t_3_2:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(dia*1.5)
        time.sleep(step)
        print("       SNAP!")
        time.sleep(step)
        print("\n")
        header()
        retry = input("Game over. Try again? (Y/N):\n")
        if retry == "n" or retry == "N":
            sys.exit()
        else:
            escaping_sanctum()
    else:
        escaping_sanctum1()        


############## Basement choice ###############################################
##############################################################################
##############################################################################


def escaping_sanctum2_1():
    print("\n\n")
    time.sleep(slow)
    print("Alpha Team heads toward the frosted glass doors that lead to the stairs, the basement a dozen flights down.")
    time.sleep(slow)
    print("With a slight push of the doors, radio static can be fainlty heard emanating from below.")
    time.sleep(slow)
    print(f"{user_color.title()} lights illuminate ascending and decending steps, but the team heads towards the noise..\n")
    time.sleep(step)
    pause()
    print()
    t0 = f"\n\t({user_name}): \"We need to recon with Bravo and figure out what happened here. Maybe the storm is interf-\n"
    for letter in t0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    t1 = "\n!!!!ffffffffffffffffffffffffffffssssssssssssssssssssssssssssssssshhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!\n"
    for letter in t1:
        sys.stdout.write(letter.upper())
        sys.stdout.flush()
        time.sleep(quick*2)
    time.sleep(slow)
    print("\nEvery piece of radio equipment on Team Alpha bursts into noise, echoing throughout the landings above.")
    time.sleep(slow)
    t2 = f"\n\t({user_name}): \"What the-- Comms off, turn comms off! ..We're going deaf and blind at this point\""
    for letter in t2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(step)
    print("\n")
    print(f"\nThere are no sounds but footsteps. Team Alpha reaches the basement level, where {user_name} finds a radio on the ground.")
    time.sleep(step)
    print("The lost radio is badly damaged, with deep grooves scratched into the surface. But the battery pack is missing....")
    time.sleep(step)
    print("There is a directory on the wall")
    time.sleep(step)
    print()
    pause()

    ##### Both choices 1&2 fork off in basement #########################################
    #################################################################################

    time.sleep(step)
    print()
    basement_fork = input(f"{user_name}, what direction will you take Team Alpha? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Right: \'Freezer Section: Unit B\'\n\
    2) Straight: \'Dry Storage: Unit A\'\n")
    if basement_fork == "1":
        time.sleep(step)
        escaping_sanctum2_1B()
    elif basement_fork == "2":
        time.sleep(slow)
        escaping_sanctum2_1A()
    else:
        print("\n\t\tinvalid response".upper())
        time.sleep(step)
        print("\n\n")
        escaping_sanctum2_1()    


### Basement - choice 2 (Storage A) #########################################################
#############################################################################################


def escaping_sanctum2_1A():
    print("\n")
    time.sleep(step)
    print("Team Alpha continues slowly down the corridor towards the storage bay. The staircase lights become less and less")
    time.sleep(step)
    print("useful with each step as they head further into darkness. The only thing visible in the distance is a small")
    time.sleep(step)
    print(f"window hovering on the door of Storage Unit A. The dim {user_color} light creeping through is barely visible, but the shadow")
    time.sleep(step)
    print("of a figure flashes past..")
    time.sleep(slow)
    print("\n")
    pause()
    print()
    time.sleep(slow)
    print(f"{user_name} quickens their step and readies Alpha Team to breach the door.")
    time.sleep(slow)
    t0 = f"\n\t ({user_name}): \"On my mark\"..(motions)...3         2          1         "
    for letter in t0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*1.4)
    time.sleep(quick)
    print("            BANG!\n")
    pause()
    time.sleep(slow)
    print("\nBehind the Storage A doors lies Bravo Team. Some are injuried but all are accounted for.")
    time.sleep(slow)
    t1 = f"\n ({bravo_leader}): \"You look spooked, but aren\'t we glad to see you, {user_name}\"\n"
    for letter in t1:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    t2 = f"\n\t({user_name}): \"You don\'t look so hot either. Come on, let\'s get out of this place\"\n"
    for letter in t2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(slow)
    print()
    pause()
    print()
    t3 = "Both teams return to the surface using a freight elevator. The shore where they left their boats is\n\
a ruin of vegetation and sand. The hum of engines roar over the sound of waves crashing against the vehicles. An\n\
injured Bravo squad member peers into the greycast sky, their hand covering a curious wound on their arm......\n\
a deep bite wound. The outline of Toro Sanctum is reflected off their gaze as they look back at the shrinking island."
    for letter in t3:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*1.5)
    time.sleep(slow)
    t4 = "\n\n\t\t\t Thank you for playing"
    for letter in t4:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    print("\n")
    header()

### Basement - Choice 1 (Storage B) ###########################################################
###############################################################################################

def escaping_sanctum2_1B():
    print("\n")
    time.sleep(step)
    print(f"Team Alpha makes a right and heads towards the frozen storage. The flickering {user_color} lights overhead")
    time.sleep(step)
    print("crack and blink as they approach the freezer door. Through the icy window, there is a blinking LED light glowing")
    time.sleep(step)
    print("on the ground in the darkness. The LED light is the same as on everyone\'s radio.")
    time.sleep(slow)
    print("\n")
    pause()
    print()
    print(f"{user_name} grasps the frozen handle and pulls the door open slowly...taking a small step inside.")
    time.sleep(slow)
    print(f"Just as {user_name} grabs the lost radio, a hand lunges out of the darkness, grabbing their wrist")
    time.sleep(slow)
    t0 = f"\n\t({user_name}): ...\"What th--!\""
    for letter in t0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(step)
    print()
    pause()
    print()
    time.sleep(step)
    print("The freezer door slams shut, several locks forced in place.")
    time.sleep(slow)
    print(f"The slowing flash LED light tints the faces engulfing {user_name}...\n")
    time.sleep(slow)
    print("\n")
    header()
    t1 = "\tGame Over\n"
    for letter in t1:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    print()
    time.sleep(step)
    retry = input("Try again? (Y/N)\n")
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum()
    else:
        time.sleep(step)
        print("\t\tInvalid response".upper())
        escaping_sanctum2_1B()



############## Lab Choice ##########################################
####################################################################
####################################################################

def escaping_sanctum2_2():
    print("\n\n")
    time.sleep(slow)
    print("Alpha Team begins to make their way out of the area when a sudden rumble is felt...\n")
    time.sleep(slow)
    t1 = "\n_._.._...............::::::::::::;;;;;;;;;;;;;;;;;;;;######################<CRASH>!!!!!!!!!\n"
    for letter in t1:
        sys.stdout.write(letter.upper())
        sys.stdout.flush()
        time.sleep(quick*2)
    time.sleep(slow)
    time.sleep(slow)    
    print("\nAll at once an elevator car comes screeching past the center shaft, coming to a crash many floors below")
    time.sleep(slow)
    t2 = f"\n\t({user_name}): \"WHAT IS GOING ON HERE?!\"\n"
    for letter in t2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(slow)
    print(f"\n{user_name.title()} peers over the ledge, then regroups the team and heads down a large corridor.")
    time.sleep(step)
    print(f"Onward, Alpha Team can see flashing {user_color.title()} lights through the large glass doors of the lab.\n")
    time.sleep(step)
    pause()
    print()
    time.sleep(step)
    print("\nThe laboratory doors slide against a gritty floor. The lab is field of broken glass and smoke.")
    time.sleep(slow)
    print(f"{user_color.title()} light is scattered in every direction as the team moves toward the emergency exit.")
    time.sleep(step)
    print("The emergency exit doors are blocked by a mountain of large boxes, lab equipment, and garbage\n")
    time.sleep(step)
    pause()
    print()
    if user_item == "A lucky coin" or user_item == "A golden locket" or user_item == "A bronze compass":
        t3 = f"{user_item} falls out of {user_name}\'s pocket and rolls towards the lab entrance, making it to the corridor\n"
        for letter in t3:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(dia)
        time.sleep(slow)
        t4 = f"\n\t({user_name}): \"...strange..\"\n\n"
        for letter in t4:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(dia)
    else:
        pass
    print("\n")

    ##### Both choices fork off in Lab #########################################
    ############################################################################

    lab_fork = input(f"{user_name}, what will you do next? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Onward: \'Dig out emergency exit\'\n\
    2) Go back: \'Return to lobby and take stairs to basement\'\n")
    if lab_fork == "1":
        time.sleep(step)
        escaping_sanctum2_2A()
    elif lab_fork == "2":
        time.sleep(slow)
        escaping_sanctum2_2B()
    else:
        print("\n\t\tinvalid response".upper())
        time.sleep(step)
        print("\n\n")
        escaping_sanctum2_2()    

#### Lab option A - Game over          ##############################
#####################################################################

def escaping_sanctum2_2A():
    print("\n")
    time.sleep(slow)
    print("The Team begins unblocking the emergency exit doors. The massive equipment pieces take")
    time.sleep(slow)
    print("the entire team to move aside. Shards of glass fall off of repositioned boxes. Something")
    time.sleep(slow)
    print(f"catches {user_name}\'s eye.")
    time.sleep(slow)
    print()
    pause()
    time.sleep(slow)
    print("\nAmong the glass are pieces of shredded clothing and hair\n\n")
    time.sleep(slow)
    t1 = ".............................\n"
    for letter in t1:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(slow)
    t2 = f"\n\t({user_name}): \"...WAIT....ALPHA TEAM FALL BAC------"
    for letter in t2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(slow)
    print("\n")
    print("The exit doors plunge open. Alpha team is bombarded, surrounded in seconds")
    print()
    time.sleep(slow)
    print("\n")
    header()
    time.sleep(slow)
    retry = input("Game Over. Try again? (Y/N)\n")
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum()
    else:
        time.sleep(step)
        print("\n\t\tInvalid response".upper())
        escaping_sanctum2_2A()


### Lab option B - Chance to return to lobby ###############################################
############################################################################################

def escaping_sanctum2_2B():
    print("\n")
    print(f"{user_name} guides Alpha Team back to the lobby and to the entrance of the main stairway")
    time.sleep(step)
    escaping_sanctum2_1()

####### Input Weight check ###########################
def input_weight(weight):
    while True:
        try:
            userInput = int(input(weight))
        except:
            print("This is not a whole number, please try again")
            continue
        else:
            return userInput
            break

#### Retry Option ###############################################
#################################################################
def escaping_sanctum():
    escaping_sanctum0 = input("\nWill you search for Bravo Team and Escape Toro Sanctum? (Y/N)\n")
    if escaping_sanctum0 == "n" or escaping_sanctum0 == "N":
        print("Understood\n")
        time.sleep(step)
        loss = "Game Over"
        for letter in loss:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(dia*2)
        sys.exit()
    elif escaping_sanctum0 == "y" or escaping_sanctum0 == "Y":
        escaping_sanctum1()
    else:
        print("This isn\'t a valid response. Try again:\n")
        escaping_sanctum()

########################################################################################################################
########################################################################################################################
## Start of Escaping Toro Sanctum script ###############################################################################
########################################################################################################################
########################################################################################################################


print()
time.sleep(step)
header()
print("\n")
time.sleep(step)
disclaimer = "\n\n\t Esacping Toro Sanctum ® is a work of fiction. Characters, names, businesses, locations,\n\
events, and incidents are products of the authors and co-authors (you, the user) imagination. Any resemblance to actual persons, both\n\
living or dead, or actual events is purely coincidental"
for letter in disclaimer:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(.002)

print("\n\n")
time.sleep(step)

#### Setting global variables and gathering user info #######################################
#############################################################################################

print("Before we begin, we need complete you character profile. Please answer the following questions\n")
pause()
print()
time.sleep(step)
user_name = input("What is your name, Team Leader?:\n")
time.sleep(step)
user_weight = input_weight("\nIn lbs, how much do you weigh?:\n")
time.sleep(step)
user_color = input("\nWhat is your favorite color?:\n")
time.sleep(step)
user_item = input("\n Of the following, which item would you choose to carry with you? \n\
    [Select 1, 2, or 3 then press <enter> ]\n\n\
    1) A lucky coin\n\
    2) A golden locket\n\
    3) A bronze compass\n")
if user_item == "1":
    user_item = "A lucky coin"
elif user_item == "2":
    user_item = "A golden locket"
elif user_item == "3":
    user_item = "A bronze compass"
else:
    user_item = "empty"

print()
time.sleep(step)
bravo_leader = input("Who is someone you look up to or are inspired by?:\n")
def starting_question():
    start_esaping_sanctum = input(f"{user_name}, would you like to Start? (Y/N):\n")
    if start_esaping_sanctum == "n" or start_esaping_sanctum == "N":
        print("Game Over. Please reload program")
        sys.exit()
    elif start_esaping_sanctum == "y" or start_esaping_sanctum == "Y":
        pass
    else:
        print("that was not a valid response.")
        starting_question()
        
print()
time.sleep(step)
user_city = input("Name a city you would like to travel to someday:\n")
time.sleep(step)
user_country = input("\nFinally, what is a country you are least likely to travel to?\n")
time.sleep(slow)
print("\n")
loading = "...saving data...."
for letter in loading:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(dia)
print("\n")
time.sleep(slow)    
starting_question()
print("\n\n")
header()
print("\n\n\n\n\n")
time.sleep(slow)
def introduction():
    print("\n\n")
    print("A single flash of lightning casts dozens of long shadows across the skybridge. The subsequent")
    time.sleep(step)
    print("thunder crashes, deafening the small group. The rain is relentless, making the view in every direction a")
    time.sleep(step)
    print("grey abyss. The only feature made out in the distance, as another flash of lightening blazes across the sky,")
    time.sleep(step)
    print("is the outline of a gigantic building. An entire team has been missing from the rendezvous for the better")
    time.sleep(step)
    print("part of an hour. Someone is shouting over the rain, gripping a radio...\n\n")
    time.sleep(step)
    pause()
    t0 = f"\n\t({user_name}): \"....-repeat, Systems check! Over!\"\n"
    for letter in t0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    t1 = "\n......\n"
    for letter in t1:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*2)
    t2 = f"\n\t({user_name}): \"...Systems check, come in Team Bravo!\"\n"
    for letter in t2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    t3 = "\n...(radio silence)...\n"
    for letter in t3:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*1.5)
    t4 = "\n....<<<static>>>\n"
    for letter in t4:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*2)
    t5 = f"\n\t({user_name}): \"BRAVO, DO YOU READ???!!!\"\n"
    for letter in t5:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    t6 = "\n...(radio silence)...\n"
    for letter in t6:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia*1.5)
    t7 = f"\n\t({user_name}): \"Damn!! Alpha, move out!\"\n\n"
    for letter in t7:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(slow)
    print("\nRain continues to pour in sheets as Alpha team scans the lobby of Toro Sanctum, a newly constructed")
    time.sleep(step)
    print(f"bioengineering facility on {user_city.title()} Island. After the \"Incindent\", the paramilitary contractors of PiThon were")
    time.sleep(step)
    print(f"flown in from {user_country.title()} to inspect Toro Sanctum and the surrounding coast. Team Bravo led the expedition")
    time.sleep(step)
    print("into the facility while Team Alpha scanned the ports of entry and docks. There was nothing. No signs of anyone")
    time.sleep(step)
    print("having visited or worked in the high tech research facility which celebrated its launch two weeks ago. No ships.")
    time.sleep(step)
    print("No vehicles on the newly paved parking lots. Nothing. Team Alpha lost communication with Bravo squad just as the")
    time.sleep(step)
    print("storm starting picking up. With limited visibility, Team Alpha rushes past the deserted security gates and double")
    time.sleep(step)
    print("pane glass doors of Toro Sanctum. The lobby is a massive cavern of steel and glass, abandoned and dimly lit. The rain")
    time.sleep(step)
    print("drums on the glass overhead as Team Alpha steps further into the facility...")
    
    time.sleep(slow)
    print("\n")
    escaping_sanctum()

introduction()