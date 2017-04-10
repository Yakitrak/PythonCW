#UP781587#
#Programming Python Assignment - Interactive Patch#

from graphics import *
import math
patchList = [] 

#Program Starts Here#
def main(): 
    print("Hello there! Welcome to KJainwal's interactive patchwork program.")
    print("Please follow the instructions to make your personalised patchwork. Have fun!")
    
    patchSize, userColourList = getInputs()
    win = drawPatches(patchSize, userColourList)
    swapPatch(patchSize, win)
 
#Takes and Validates Inputs#    
def getInputs():
    patchSize = 0
    userColourList  = []
    validSizes = ["5", "7", "9"]                                         
    validColours = ["red", "blue", "green", "orange", "magenta", "cyan"]
    validColoursForChecking = ["red", "blue", "green", "orange", "magenta", "cyan"]
    NumOfCol = 0 
    
    #Number Validation:
    while patchSize not in validSizes:   
        patchSize = input("Please enter a valid size of patches (5, 7 or 9): ")
     
    #Colour Validation:
    while NumOfCol < 3:                   
        col = input("Enter a colour from the list: " + str(', '.join(validColours)) + ": ").lower()
        
        #Checks If Valid Colour:
        if col in validColoursForChecking:  
        
            #Checks If Already Used:
            if col not in userColourList: 
                NumOfCol += 1
                userColourList.append(col)
                validColours.remove(col)
                print(col, "accepted")
            else:
                print("Sorry, you have already used that colour. Please enter a different one.")
        else:
            print("Sorry, that is not valid. Please enter a valid colour!") 
    patchSize = eval(patchSize)   
    return patchSize, userColourList 
    
#Draws Both Patches Correctly#      
def drawPatches(patchSize, userColourList): 
    win = GraphWin("KJainwal Coursework", (patchSize*100), (patchSize*100))
    win.setBackground("white")
    x = 0
    y = 0
    #Used To Cycle Through Colours:
    col = 0           
    #Diagonal Is Always In This Part:          
    diagonal = patchSize - 1    
    
    for i in range(patchSize):
        for j in range(patchSize):
            border = Rectangle(Point(x, y), Point(x + 100, y + 100))
            border.draw(win)
            
            #Checks If Its Diagonal:
            if i+j == diagonal: 
                patchList.append(drawPatch1(win, x, y, userColourList[col]))
            else:
                patchList.append(drawPatch2(win, x, y, userColourList[col])) 
            col += 1
            if col >= 3:
                 col = 0
            x += 100
        x = 0
        y += 100
    return win
        
#Draw First Patch#
def drawPatch1(win, x, y, colour): 
    rect = []
    topx = x
    topy = y
    botx = topx + 100
    boty = topy + 100
    for i in range(10):
        rect.append(Rectangle(Point(topx, topy), Point(botx,boty)))
        if i%2 != 0:
            rect[i].setFill(colour)
            rect[i].setOutline(colour)
        else:
            rect[i].setFill("white")
            rect[i].setOutline("white")
        botx -= 10 
        topy += 10
        rect[i].draw(win)
    return rect
        
#Draw Second Patch#       
def drawPatch2(win, x, y, colour): 
    rect = []
    topy = y
    boty = topy + 10
    
    #Loops 2 Lines 5 Times To Make 10 Lines:
    for i in range(5):  
        topx = x 
        botx = topx + 15
        
        #Makes First Line:
        for i in range(4): 
            if i == 0:
                rect.append(drawRectangle(Point(topx, topy), Point(botx, boty), colour, win))
                topx += 35
                botx += 35
                
            elif i == 3:
                botx -= 10
                topx -= 10
                rect.append(drawRectangle(Point(topx, topy), Point(botx, boty), colour, win))
            else:
                topx -= 10
                botx -= 5
                rect.append(drawRectangle(Point(topx, topy), Point(botx, boty), colour, win))
                topx += 40
                botx += 35
        topx = x + 10
        botx = x + 30
        topy += 10
        boty += 10
        
        #Makes Second Line:
        for i in range(3): 
            rect.append(drawRectangle(Point(topx, topy), Point(botx, boty), colour, win))
            topx = topx + 30
            botx = botx + 30
        topy += 10
        boty += 10
    return rect

#Draws Rectangles For Patch2#      
def drawRectangle(p1, p2, colour, win): 
    rect = Rectangle(p1, p2)
    rect.setFill(colour)
    rect.draw(win)
    return rect 

#Allows The User To Swap Patches Through Clicks# 
def swapPatch(patchSize, win):
    print("Click on two patches to swap their design!")
    #Infinite Loop - User May Play Long As He Wants:
    while True:
        click = win.getMouse() #Gets First Click
        #Rounded Click to Nearest Integer Point On Screen:
        patchPosition1 = int(math.floor(click.getX()/100)+(patchSize*math.floor(click.getY()/100))) 
        #Finds Value Of Coordinates In List:
        select = patchList[patchPosition1]
        selectX = (math.floor(click.getX()/100)*100) 
        selectY = (math.floor(click.getY()/100)*100) 
        
        click = win.getMouse() #Gets Second Click
        #Rounded Click to Nearest Integer Point On Screen:
        patchPosition2 = int(math.floor(click.getX()/100)+(patchSize*math.floor(click.getY()/100))) 
        #Finds Value Of Coordinates In List:
        select2 = patchList[patchPosition2]
        
        #Updates Position For Both Patterns In List:
        patchList[patchPosition2] = patchList[patchPosition1]  
        patchList[patchPosition1] = select2                   
        
        #Moves First Clicked Patch:       
        for i in range(len(select)): 
            select[i].move(-(selectX - (math.floor(click.getX()/100)*100)), -(selectY - (math.floor(click.getY()/100)*100)))
        
        #Moves Second Clicked Patch:
        for i in range(len(select2)): 
            select2[i].move(selectX - (math.floor(click.getX()/100)*100), selectY - (math.floor(click.getY()/100)*100))
                
main()
            