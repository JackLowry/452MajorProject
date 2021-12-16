import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
#Going to chrome and opening up a new tab on my Mac
pyautogui.moveTo(876, 876)
pyautogui.click()
pyautogui.moveTo(142, 12)
pyautogui.click()
pyautogui.moveTo(155, 35)
pyautogui.click()
pyautogui.moveTo(164, 59)
pyautogui.click()
pyautogui.typewrite('http://127.0.0.1:5000/', interval=0.1) #Goes to website
gui.press('return')
pyautogui.moveTo(725, 540) #if user has to be created, register them
pyautogui.click()
pyautogui.moveTo(732, 105)
pyautogui.doubleClick()
pyautogui.typewrite('Xin', interval=0.1)  #User name to be created
pyautogui.moveTo(720, 140)
pyautogui.doubleClick()
pyautogui.typewrite('x123', interval=0.1)  #User password to enter
pyautogui.moveTo(732, 175)
pyautogui.doubleClick()
pyautogui.typewrite('20', interval=0.1)  #User age to enter
pyautogui.moveTo(791, 198)
pyautogui.click()
pyautogui.click()  #Select home campus
pyautogui.moveTo(706, 253)
pyautogui.doubleClick()
pyautogui.typewrite('Silvers', interval=0.1)  #Specify residence hall
pyautogui.moveTo(738, 273)
pyautogui.click()
pyautogui.click()  #Select Gender
pyautogui.moveTo(736, 310)
pyautogui.click()
pyautogui.click()  #Select Year
pyautogui.moveTo(792, 347)
pyautogui.click()
pyautogui.click()  #Specify sexual orientation
pyautogui.moveTo(757, 400)
pyautogui.doubleClick()
pyautogui.typewrite('Computer Engineering', interval=0.1)  #Major
pyautogui.moveTo(725, 427)
pyautogui.click()
pyautogui.click()  #Specify school of study
pyautogui.moveTo(706, 475)
pyautogui.doubleClick()
pyautogui.typewrite('I am an engineer', interval=0.1)  #Bio of user
pyautogui.moveTo(660, 518)
pyautogui.click()
pyautogui.moveTo(578, 302)
pyautogui.doubleClick()  #Select picture
pyautogui.moveTo(724, 554)
pyautogui.click()
pyautogui.moveTo(736, 480) #if user already created, proceed to login
pyautogui.click()
pyautogui.moveTo(707, 444)
pyautogui.doubleClick()
pyautogui.typewrite('Xin', interval=0.1)  #Loggin in, specify user name
pyautogui.moveTo(703, 463)
pyautogui.doubleClick()
pyautogui.typewrite('x123', interval=0.1)  #password
pyautogui.moveTo(729, 481)
pyautogui.click()   #logging in
pyautogui.moveTo(730, 474)
pyautogui.click() #mingle
pyautogui.moveTo(765, 444)
pyautogui.click() 
pyautogui.click() #Home Campus Select - Busch
pyautogui.moveTo(763, 486)
pyautogui.click() 
pyautogui.click() #Gender Select - Male
pyautogui.moveTo(765, 519)
pyautogui.click() 
pyautogui.click() #Year select
pyautogui.moveTo(765, 555)
pyautogui.click() 
pyautogui.click() #Sexual Orientation Select
pyautogui.moveTo(765, 595)
pyautogui.click() 
pyautogui.click() #School select 
pyautogui.moveTo(906, 594)
pyautogui.click() #Submit - you are now in the Mingle page, seeing the pictures of possible matches
pyautogui.moveTo(766, 740)
pyautogui.click() #Mingle with them!
gui.keyDown('command')
gui.press('left') 
gui.keyUp('command') #Now you are back on the Mingle filters page
pyautogui.moveTo(750, 632)
pyautogui.click() #Go back to previous page
pyautogui.moveTo(750, 530)
pyautogui.click() #Chat With Matches!