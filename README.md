# Tyler Toro
## Justice Through Code - Spring 2021


                   .... ............... ..........................
                   .. ......................... .......... .......
                   ...... ..... ......... ........................
                   ..........  Escaping Toro Sanctum...... .......
                   ........ ............... ............... ......
                   :::::::::::::::::::::::::::::::::::::::::::::::
                   :::::::::::::::::::::::::::::::::::::::::::::::


Welcome to my first project, **Escaping Toro Sanctum**. This is a text based adventure game with user interactivity. Toro Sanctum is a 
fictional bioengineering facility where the user is placed. The objective of the game is to follow the storyline and choose the correct path that will lead to locating an exit and finding the lost group, Team Bravo. The user is the team leader of Alpha Team, and the story is updated based on the user input. 

*The code is sectioned off with the hash "#" character and labeled*

There are several questions posed to the user in the "user info" section of the script. The user provides:
    - Name
    - weight
    - favorite color
    - Special item
    - Someone they admire
    - A city they plan to travel to
    - Country leasT likely to travel to

**///Name** - The name provided is stored in the variable, user_name, and is plugged throughout the dialogue and storyline. This adds
to the interactive experience.

**///weight** - The user weight, which is checked with the defined "input_weight" function. This function will determine if the input
is an integer, and will continue to ask until an integer is provided. The only instance user weight comes into play is during the 
Elevator path, after Mission Objective. When the user attempts to rappel down an elevator shaft, the maximum weight is calculated
at [user_weight - 20], which results in game over.

**///Favorite Color** - the user inputs their favorite color, and the input is plugged into the scenery. For example, when traveling 
down the main stairs in the Basement path (the correct path), the "user_color" is used to describe the lights. It is a cue showing
they are at an important part of the story. In the lab, the user_color is described as scattered, a cue that something is wrong. 
The Lab path leads to game over & a retry.

**///Special Item** - The user is asked to pick an item out of three options (a coin, locket, or compass). This item only comes into
play during the Lab path, where the item falls out of the pocket of the user and rolls out of the lab, a cue to LEAVE. The user
input is converted from "1, 2, or 3" and stored as the correct string "A Coin..A locket etc" . If the user does not enter a correct
response in the "user info" section, nothing is stored as their item, and the print statement skips to "pass"

**///Idol** - The user is asked to provide someone they look up to; this input is stored as a string and used to create Bravo Team leaders name at the end of the game. 

**///City** - The user is asked to name a city they would like to visit. This input is stored as a string, and used to generate the name of the fictional island where the Toro Sanctum research facility is located

**///Country** - The user is asked to provide the name of a country they would least likely travel to. This input is stored as a string, and used to generate the location from which both teams originate. This is a bit of humor, forcing the user to have traveled where they least expected to.

# The basic decision tree of the game



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
    (Dry Storage)   |             |           loss + retry
      Unit A        |             |                 
       Win          |             |                      
                    |             |                        
               (Freezer)          |                         
                 Unit B           |                          
            loss + retry          |                        
                                  /\                      
                                /    \                   
                              /        \                   
                           /              \              
               (Emergency Exit)        (Return to Basement)
                       |                       |
                  loss + retry            (Basement)


The only win is choosing the Basement, then Dry Storage Unit A. However, when faced with an end game situation, the user is asked if
they want to try again. If their input is y, for yes, the defined "escaping_sanctum()" function is executed, which asks the question:

   Will you search for Bravo Team and Escape Toro Sanctum?


## ///Defined Functions///:

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


## /// How many questions posed to user??
Over the course of the game, the user is asked 11 questions if they choose just the correct paths from start to finish. Several more questions will be asked of the user if they face a game over screen. Many of the defined functions are paths, with several chances to return to a previous "fork in the road". If the user chooses not to play at any point, a game over screen will print followed by a "sys.exit()" function to stop the program. 


## ///Imported default Python Libraries:
sys, time, os

sys - Used for system specific functions, ie sys.stdout.write() writes on the terminal
time - Used to manipulate and access time functions, ie time.sleep used for delay
os - Used for misc. operating system interfaces. I originally wanted to use os.exit to close terminal/powershell but could not figure it out

## ///Time Variables

slow = 2.5 seconds, for slow delay
dia = 0.1 seconds, for dialogue
quick = 0.01 seconds, for very fast text display
step = 1 second, for small delay


## ///References:
I would like to thank Tim Statler from CompSciCentral (compscicentral.com) and their youtube tutorial
"Simple Python Project | Text-Based Adventure Game: Time Unraveled" for assisting me in learning the basics of a text-based game.
<https://www.youtube.com/watch?v=ypNFNr72Xe8>

The simple pause() function was helpful in learning, there are many ways to make a user press a key before continuing. This webpage 
was a great source.
https://stackoverflow.com/questions/11552320/correct-way-to-pause-a-python-program

The input_weight() function was a long experiment, with thanks to a contributor on stackoverflow.com. I needed my function to make sure the user inputs an integer for weight, because their weight it used in the story. Upon customizing the example on that webpage a bit, I was able to make it work.
https://stackoverflow.com/questions/20095244/how-do-i-check-if-input-is-a-number-in-python



                   .... ............... ..........................
                   .. ......................... .......... .......
                   ...... ..... ......... ........................
                   ..........  Escaping Toro Sanctum...... .......
                   ........ ............... ............... ......
                   :::::::::::::::::::::::::::::::::::::::::::::::
                   :::::::::::::::::::::::::::::::::::::::::::::::

Esacping Toro Sanctum ® is a work of fiction. Characters, names, businesses, locations, events, and incidents are products of the authors and co-authors(you, the user) imagination. Any resemblance to actual persons, both living or dead, or actual events is purely coincidental"

