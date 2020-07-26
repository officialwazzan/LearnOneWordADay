# LearnOneWordADay
Teach me one word a day - Automate your learning with no Effort


Brief:

You got an old laptop that you haven't used for a while. Well let's use it to enrich you with vocabularies :)
I made this for my family to help us take advantage of being at home during  the lockdown

Step by Step:
The python script will automatically have a new word shown to you everyday:
1- Turn on your laptop
2- Place your laptop somewhere where you'll walk by multiple times a day, this could be next to your door, bathroom etc
3- Download python https://www.python.org/downloads/ and make sure to tick the box where it says add to windows Path
4- Restart, "typical 😅" 
5- Run CMD as an administrator 
6- Run "install pip pyautogui"
7- Run "import pyautogui"
8- Open dictionary.com or any other dictionary that you want
9- Run the below and make sure you copy the empty line to enable you to hover the mouse to the place of the text box where the word need to be entered, the below will give you 5seconds to execute, so no need to run :) 
"time.sleep(5)
pyautogui.position()

"
9- copy the above x and y values and replace accordingly in in lines 27 and 29 from the main.py file
10- repeat step number 8 whilst hover the mouse of the URL text box
11- Replace the x and y values accordingly in lines of 35 and 37
12-  Find the listOfWords
13- Replace the words you want to learn in the CSV file
14- open dictionary.com or your selected website
14- Run main.py, you got 5 second to minimise the script console window
15- you got it working ;) 

Upon request I could add:
- instructions for Mac users
- automate it more to get ride of 10 steps
- to dim the light of screen during the night and increase it in the mornings 
