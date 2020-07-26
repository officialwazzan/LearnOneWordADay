import pyautogui
import csv
import time

time.sleep(5)  # allowing you a plenty of time to minimize and adjust if needed
importedWords = []  # this link will contait a word from each cell in the first column, from the CSV "listOfWords.csv"
reformatImportedwords = []  # reformated version of importedWords, to get ride of "" and []

with open("listOfWords.csv", encoding='utf-8-sig') as csv_file:  # utf-8-sig to avoid § etc
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        importedWords.append(lines)

# the below loop is used to remove ""s and []s frpm the list of importedWords

for tempvalue01 in importedWords:
    tempvalue01 = str(tempvalue01)
    tempvalue01 = (tempvalue01.replace("['", ''))
    tempvalue01 = (tempvalue01.replace("']", ''))
    tempvalue01 = (tempvalue01.replace("'", ''))
    reformatImportedwords.append(tempvalue01)




for tempvalue02 in reformatImportedwords:
    pyautogui.click(x=2224, y=323)  # location of the google dictionary textbox
    pyautogui.hotkey('ctrl', 'a', 'backspace')
    pyautogui.click(x=2224, y=323)  # location of the google dictionary textbox
    print(tempvalue02)
    pyautogui.write(str(tempvalue02))  # the word to be printed
    pyautogui.press('enter')
    time.sleep(86400)

pyautogui.click(x=2411, y=46)  # location of url box
pyautogui.hotkey('ctrl', 'a', 'backspace')
pyautogui.click(x=2411, y=46)  # location of url box
pyautogui.write(
    "https://1.bp.blogspot.com/-CTmwu9vs_do/XZt9oMNvKSI/AAAAAAAAAxw/Qu8X1jv3cnoWyR55M785_X2ApCQm8zoXgCLcBGAsYHQ/s1600/20191007_190112_0000.png")  # url timeout
pyautogui.press('enter')


