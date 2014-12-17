# Natalie Calkins
# Final Project Game

import random
# needed for working directory
import os

#Global Variables:

localPath = ""
endUser = ""
endGame = 0


# global sound bites

chimeSound = ()
blahSound = ()
para4Sound = ()
para5Sound = ()
para6Sound = ()

# global images

monterey = ()
sunset = ()
para3 = ()
para4 = ()
para5 = ()
inUniverse = ()
universeImage = ()

def makeNegative(monterey):
  pixels = getPixels(monterey)
  for pix in pixels:
    redP = getRed(pix)
    setRed(pix, 255 - redP)
    greenP = getGreen(pix)
    setGreen(pix, 255 - greenP)
    blueP = getBlue(pix)
    setBlue(pix, 255 - blueP)
  return(monterey)


# choose sounds

def findSound(localPath):
  global chimeSound
  global blahSound
  global para4Sound
  global para5Sound
  global para6Sound
  
  chimeSound = os.path.abspath(localPath + "\FinalProject\chimes.wav")
  chimeSound = makeSound(chimeSound)
  
  para4Sound = os.path.abspath(localPath + "\FinalProject\para4Sound.wav")
  para4Sound = makeSound(para4Sound)
  
  para5Sound = os.path.abspath(localPath + "\FinalProject\para5Sound.wav")
  para5Sound = makeSound(para5Sound)
  
  para6Sound = os.path.abspath(localPath + "\FinalProject\para6Sound.wav")
  para6Sound = makeSound(para6Sound)
  
  #blahSound = os.path.abspath(localPath + "\FinalProject\blahblah.wav")
  #blahSound = makeSound(blahSound)
  
# choose pictures

def findImages(localPath):

  global jellyFish
  global monterey
  global sunset
  global inUniverse
  global universeImage
  global para3
  global para4
  global para5

  jellyFish = os.path.abspath(localPath + "\FinalProject\Jellyfish.jpg")
  jellyFish = makePicture(jellyFish)
  
  monterey = os.path.abspath(localPath + "\FinalProject\Monterey.jpg")
  monterey = makePicture(monterey)
  
  sunset = os.path.abspath(localPath + "\FinalProject\Koala.jpg")
  sunset = makePicture(sunset)
  
  para3 = os.path.abspath(localPath + "\FinalProject\para3.jpg")
  para3 = makePicture(para3)
  
  para4 = os.path.abspath(localPath + "\FinalProject\para4.jpg")
  para4 = makePicture(para4)
  
  para5 = os.path.abspath(localPath + "\FinalProject\para5.jpg")
  para5 = makePicture(para5)
  
  universeImage =  os.path.abspath(localPath + "\FinalProject\Jellyfish.jpg")
  universeImage = makePicture(universeImage)
  
  inUniverse =  os.path.abspath(localPath + "\FinalProject\Jellyfish.jpg")
  inUniverse = makePicture(inUniverse)
  

############################################################################

def welcome():
  global localPath
  global endUser
  showInformation("""Welcome to a 4th dimensional parallel universe\n,__,\n""")
  
  if localPath == "":
    showInformation("Please select the \"working\" folder as your directory.")
    localPath = setMediaFolder()
 
  if endUser == "":
    userName = requestString("What is your name?")
    while userName == "":
      userName = requestString("Looks like you haven't entered your name. Please enter a valid name")
  
    showInformation("Welcome, " + userName + ".")
    
#set sound and pictures
  findSound(localPath)
  findImages(localPath)  

  showInformation("In each universe you will be told where to go to proceed through the dimensions.")
  showInformation("You can go up, down, left or right by typing the word of that direction.")
  showInformation("It can take some time to move through time and space.")  
  showInformation("Enter \"help\" to open the help menu.")
  showInformation("Enter \"exit\" to end your journey.")

def helpMenu():
  showInformation("You can go up, down, left or right by typing the word of that direction." +
                  "(It can take some time to travel through the portals, so please be patient.) " +
                  "Enter \"help\" to open the help menu. " +
                  "Enter \"exit\" to end your your journey.")  
  
  
def map():
  global inUniverse
  if inUniverse == 'water':
    show(jellyFish)
  elif inUniverse == 'ice':
    show(monterey)
  elif inUniverse == 'weightless':
    show(jellyFish)
  elif inUniverse == 'ether':
    show(sunset)
  
  else:
    show(sunset)  
  

  ########################
# universe 1
# weightless

def para1():
  global jellyFish
  global monterey
  global inUniverse
  global universeImage
  
  
  
  inUniverse = 'weightless'
  
  
  
  universeImage = makeNegative(jellyFish)
  repaint(jellyFish)
  
  where = 0
  
  # print description
  showInformation("Here you are in the weightless dimension")
  # print directions
  showInformation("Enter 'down' to leave this universe or enter 'exit' to end the journey")
  userInput = requestString("Type the word 'down'")
  # while user input
  while where == 0:
    if userInput == "exit":
      where = 1
      global endGame
      endGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to go 'down' or 'exit'?")
    elif userInput == "down":
     where = 1
     para2()
    
    else:
        showInformation("There is nothing here.")
        userInput = requestString("Would you like to: \n"  +
                                "go \"down\"")
   
  
##############################################################################  
# parallel universe 2
# ice

def para2():
  global chimeSound
  global sunset
  global inUniverse
  global universeImage
  global blahSound
  
  inUniverse = 'ice'
  
  play(chimeSound)
  
  universeImage = makeNegative(monterey)
  repaint(monterey)
   
  where = 0
  
  # print description
  showInformation("You are in the dimension of coldness")
  # print directions
  showInformation("You can go left or right")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
  # while user input
  while where == 0:
    if userInput == "exit":
      global endGame
      where = 1
      endGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
   
    elif userInput == "back":
      play(chimeSound)
      where = 1
      para1()
    elif userInput == "left":
      where = 1
      para6()
    elif userInput == "right":
      where = 1
      para7()
    
    else:
      userInput = requestString("Where would you like to go\n" +
                                "Would you like to: \n" +
                                "go \"right\"\n" +
                                "go \"left\"\n" +
                                "go \"back\"")  
  
  
 


##############################################################################  
# parallel universe 3
# contemplation

def para6():
  global chimeSound
  global sunset
  global inUniverse
  global universeImage
  global blahSound
  global para4Sound
  global para4
  
  inUniverse = 'ether'
  
  play(para4Sound)
  
  universeImage = makeNegative(para4)
  repaint(para4)
   
  where = 0
  
  # print description
  showInformation("You are in the dimension of ether")
  # print directions
  showInformation("You can go left or right")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
  # while user input
  while where == 0:
    if userInput == "exit":
      global endGame
      where = 1
      endGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
   
    elif userInput == "back":
      play(chimeSound)
      where = 1
      para1()
    elif userInput == "left":
      where = 1
      para7()
    elif userInput == "right":
      where = 1
      para8()
    
    else:
      userInput = requestString("Where would you like to go\n" +
                                "Would you like to: \n" +
                                "go \"right\"\n" +
                                "go \"left\"\n" +
                                "go \"back\"")  
  
  
###################################################################### 

def para7():
  global chimeSound
  global sunset
  global inUniverse
  global universeImage
  global blahSound
  global para5Sound
  global para5
  
  inUniverse = 'water'
  
  play(para5Sound)
  
  universeImage = makeNegative(para5)
  repaint(para5)
   
  where = 0
  
  # print description
  showInformation("You are in the dimension of wetness")
  # print directions
  showInformation("You can go left or right")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
  # while user input
  while where == 0:
    if userInput == "exit":
      global endGame
      where = 1
      endGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
   
    elif userInput == "back":
      play(chimeSound)
      where = 1
      para1()
    elif userInput == "left":
      where = 1
      para3()
    elif userInput == "right":
      where = 1
      para4()
    
    else:
      userInput = requestString("Where would you like to go\n" +
                                "Would you like to: \n" +
                                "go \"right\"\n" +
                                "go \"left\"\n" +
                                "go \"back\"")  
  
##############################################################
  
def para8():
  global chimeSound
  global sunset
  global inUniverse
  global universeImage
  global blahSound
  global para6Sound
  global para5
  
  inUniverse = 'thinking'
  
  play(para5Sound)
  
  universeImage = makeNegative(para5)
  repaint(para5)
   
  where = 0
  
  # print description
  showInformation("You are in the dimension of contemplation")
  # print directions
  showInformation("You can go left or right")
  # get user input
  userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
  # while user input
  while where == 0:
    if userInput == "exit":
      global endGame
      where = 1
      endGame = 1
    elif userInput == "help":
      helpMenu()
      userInput = requestString("Would you like to: \n" +
                            "go \"left\"\n" +
                            "go \"right\"\n" +
                            "go \"back\"")
   
    elif userInput == "back":
      play(chimeSound)
      where = 1
      para1()
    elif userInput == "left":
      where = 1
      para3()
    elif userInput == "right":
      where = 1
      para4()
    
    else:
      userInput = requestString("Where would you like to go\n" +
                                "Would you like to: \n" +
                                "go \"right\"\n" +
                                "go \"left\"\n" +
                                "go \"back\"")  
  
  



 
  
  
  
########################
# program

def game():
  
  welcome()
  global endGame
  quitGame = 0
  while endGame == 0:
    showInformation("You can visit many dimensions")
    para1()

  # goodbye message
  showInformation("Hope you enjoyed your journey, " + endUser)
  quit
  
game()

