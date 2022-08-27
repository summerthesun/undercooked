#UNDERCOOKED

#Name: Summer Sun
#student id: sdsun

from cmu_112_graphics import *
import random, time, math

# #ALL images were drawn by Summer Sun on pixilart.com

def appStarted(app):
    app.paused = True
    app.game = True
    app.inStart = True

    app.player = Player(app)

    app.maze = Map(app)

    #floor image
    app.floor = app.loadImage('floor.png')
    app.floor = app.scaleImage(app.floor, 1/3)

    #countertop image
    app.countertop = app.loadImage('countertop.png')
    app.countertop = app.scaleImage(app.countertop, 1/3)

    #stovetop image
    app.stovetop = app.loadImage('stovetop.png')
    app.stovetop = app.scaleImage(app.stovetop, 1/3)

    #countertop image
    app.cuttingBoard = app.loadImage('cuttingboard.png')
    app.cuttingBoard = app.scaleImage(app.cuttingBoard, 1/3)

    #countertop image
    app.timerbutton = app.loadImage('timerbutton.png')
    app.timerbutton = app.scaleImage(app.timerbutton, 1/2)

    #countertop image
    app.dogBin = app.loadImage('dogbin.png')
    app.dogBin = app.scaleImage(app.dogBin, 1/3)

    #countertop image
    app.bunBin = app.loadImage('bunbin.png')
    app.bunBin = app.scaleImage(app.bunBin, 1/3)

    #wiener image
    app.dog = app.loadImage('dog.png')
    app.dog = app.scaleImage(app.dog, 1/3)

    #cooked wiener image
    app.donedog = app.loadImage('donedog.png')
    app.donedog = app.scaleImage(app.donedog, 1/3)

    #bun image
    app.bun = app.loadImage('unslicedbun.png')
    app.bun = app.scaleImage(app.bun, 1/3)

    #bun image
    app.slicedbun = app.loadImage('slicedbun.png')
    app.slicedbun = app.scaleImage(app.slicedbun, 1/3)

    #hotdog image
    app.hotdog = app.loadImage('baredog.png')
    app.hotdog = app.scaleImage(app.hotdog, 1/3)

    #hotdog ketchup image
    app.ketchup = app.loadImage('withketchup.png')
    app.ketchup = app.scaleImage(app.ketchup, 1/3)

    #mustard image
    app.mustard = app.loadImage('withmustard.png')
    app.mustard = app.scaleImage(app.mustard, 1/3)

    #relish image
    app.relish = app.loadImage('withrelish.png') 
    app.relish = app.scaleImage(app.relish, 1/3)

    #ketchup bottle image
    app.ketchupBin = app.loadImage('ketchup.png')
    app.ketchupBin = app.scaleImage(app.ketchupBin, 1/3)

    #mustard bottle image
    app.mustardBin = app.loadImage('mustard.png')
    app.mustardBin = app.scaleImage(app.mustardBin, 1/3)

    #mustard bottle image
    app.relishBin = app.loadImage('relish.png')
    app.relishBin = app.scaleImage(app.relishBin, 1/3)

    #order image
    app.bareOrder = app.loadImage('orderbaredog.png')
    app.bareOrder = app.scaleImage(app.bareOrder, 2/3)

    #order image
    app.ketchupOrder = app.loadImage('orderketchup.png')
    app.ketchupOrder = app.scaleImage(app.ketchupOrder, 2/3)

    #order image
    app.mustardOrder = app.loadImage('ordermustard.png')
    app.mustardOrder = app.scaleImage(app.mustardOrder, 2/3)

    #order image
    app.relishOrder = app.loadImage('orderrelish.png')
    app.relishOrder = app.scaleImage(app.relishOrder, 2/3)

    #order image
    app.emptyOrder = app.loadImage('emptyorder.png')
    app.emptyOrder = app.scaleImage(app.emptyOrder, 2/3)

    #plate image
    app.plate = app.loadImage('plate.png')
    app.plate = app.scaleImage(app.plate, 1/3)

    #gameOverPage
    app.gameOver = app.loadImage('gameover.png')

    #start page
    app.start = app.loadImage('startpage.png')
    

    app.timerCounter = 0
    app.timerDelay = 1000

    app.counters = []

    app.order = Order(app)
    print(f"{app.order, app.order.type} 1")

    app.totalScore = 0
    app.objectiveOrders = 5
    app.completedOrders = 0

    app.displayScoreCount = 0
    app.displaying = False

    for i in range(len(app.maze.board)):
        for j in range(len(app.maze.board[0])):
            if(app.maze.board[i][j] != 0):
                app.counters.append((i,j))


def keyPressed(app, event):
    if(not app.paused and app.game):
        if (event.key == 'Left'):
            if app.player.ableToWalk(app):
                app.player.cx -= 15
            app.player.dir = 3
            app.player.spriteCounter = (1 + app.player.spriteCounter) % len(app.player.spriteF)
        elif (event.key == 'Right'):
            if app.player.ableToWalk(app):
                app.player.cx += 15
            app.player.dir = 2
            app.player.spriteCounter = (1 + app.player.spriteCounter) % len(app.player.spriteF)
        elif (event.key == 'Up'):
            if app.player.ableToWalk(app):
                app.player.cy -= 10
            app.player.dir = 1
            app.player.spriteCounter = (1 + app.player.spriteCounter) % len(app.player.spriteF)
        elif (event.key == 'Down'):
            if app.player.ableToWalk(app):
                app.player.cy += 10
            app.player.dir = 0
            app.player.spriteCounter = (1 + app.player.spriteCounter) % len(app.player.spriteF)


        elif (event.key == 's'):
            app.game = True
            resetTimer(app)


        elif (event.key == 'c'):
            if(app.player.dir == 3):
                app.player.dir = 4
            elif(app.player.dir == 2): 
                app.player.dir = 5
            if(len(app.maze.allFood) > 0 and app.player.closestItem(app).onCuttingBoard):
                    app.player.closestItem(app).cuts +=1
                    if(app.player.closestItem(app).cuts >= 10):
                        app.player.closestItem(app).sliceBun()
            app.player.spriteCounter = (1 + app.player.spriteCounter) % len(app.player.spriteCL)


        elif (event.key == 'g'):
            newFood = Wiener(random.randrange(100,700), random.randrange(100,700))
            app.allfood.append(newFood)
            app.wieners.append(newFood)
        elif (event.key == 'f'):
            newFood = Bun(random.randrange(100,700), random.randrange(100,700))
            app.allfood.append(newFood)
            app.buns.append(newFood)

        elif (event.key == 'Space'):
            if app.player.isHolding == None:
                wx, wy = app.maze.wienerBinIndex
                bx, by = app.maze.bunBinIndex
                if(wx - 80 < app.player.cx < wx + 80 and 
                     wy - 80 < app.player.cy < wy + 80):
                        takeBinWiener(app)
                elif(bx - 80 < app.player.cx < bx + 80 and 
                     by - 80 < app.player.cy < by + 80):
                        takeBinBun(app)
                else:
                    app.player.pickUp(app)
            elif type(app.player.isHolding) == Wiener:
                app.player.place(app)
                if(app.player.closestItem(app).onStove):
                    app.maze.cookingWieners.add(app.player.closestItem(app))
            elif type(app.player.isHolding) == Bun:
                app.player.place(app)
            elif type(app.player.isHolding) == HotDog:
                app.player.place(app)

    if (event.key == 'p'):
        print('hi')
        app.inStart = False
        app.paused = not app.paused

def takeBinWiener(app):
    wx, wy = app.maze.wienerBinIndex
    newWiener = Wiener(app, wx, wy)
    app.maze.wieners.append(newWiener)
    app.maze.allFood.append(newWiener)

def takeBinBun(app):
    wx, wy = app.maze.bunBinIndex
    newBun = Bun(app, wx, wy)
    app.maze.buns.append(newBun)
    app.maze.allFood.append(newBun)
    

#resets the timer
def resetTimer(app):
    app.timerCounter = 0

def timerFired(app):
    if(not app.paused and app.game):
        app.timerCounter += 1
    if(app.timerCounter == 240):
        app.game = False

    for elem in app.maze.cookingWieners:
        elem.cookTime += 1
        if(elem.cookTime >= 10):
            elem.cooked = True

    
    if(app.displaying == True):
        if(app.displayScoreCount < 3):
            app.displayScoreCount += 1
        else:
            app.displayScoreCount = 0
            app.displaying = False
        print(app.displayScoreCount)



#redraws everything on the screen
def redrawAll(app, canvas):
    makeFloor(app, canvas)
    if(app.player.isHolding != None):
        app.player.isHolding.setLocation(app, app.player.cx, app.player.cy)

    placeCounters(app, canvas)

    doTime(app, canvas)

    sprite = app.player.sprites[app.player.dir][app.player.spriteCounter]
    canvas.create_image(app.player.cx, app.player.cy, image=ImageTk.PhotoImage(sprite))
    
    canvas.create_rectangle(0,0,app.width, 15, fill = 'darkGreen', 
                            outline = 'darkGreen')
    canvas.create_text(15,5, fill = 'tan', text = 'Press [P] to pause', 
                        font = 'Courier 8 bold', anchor = 'nw')

    #draw wieners, buns, and hot dogs
    drawHotDog(app, canvas)

    drawWiener(app, canvas)

    drawBun(app, canvas)

    if(app.displaying):
        drawSubmit(app, canvas)
    else:
        drawOrder(app, canvas)


    if(app.paused):
        canvas.create_text(app.width/2, app.height/2 + 10, fill = 'black', 
                         text = 'PAUSE', 
                        font = 'Courier 20 bold')
        if(app.inStart):
            drawStart(app, canvas)
            
    if(not app.game):
        drawGameOver(app, canvas)

def drawGameOver(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.gameOver))

    if(app.completedOrders >= app.objectiveOrders):
        message = f'''Congrats! You completed at least {app.objectiveOrders} orders!'''
    else:
        message = f'You completed {app.completedOrders} out of {app.objectiveOrders} orders. Try again!'

    canvas.create_text(app.width/2, app.height/2 - 10, fill = 'black', 
                        text = message, 
                        font = 'Courier 20 bold')
    canvas.create_text(app.width/2, app.height/2 + 50, fill = 'black', 
                        text = f'Final Score: {app.totalScore}', 
                        font = 'Courier 40 bold')
    canvas.create_text(app.width/2, app.height/2 + 100, fill = 'black', 
                        text = f'Thanks for playing!', 
                        font = 'Courier 30 bold')
    canvas.create_text(app.width/2, app.height/2 + 150, fill = 'black', 
                        text = f'Created by Summer Sun for CMU 15-112', 
                        font = 'Courier 24')

def drawStart(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.start))
   
    canvas.create_text(app.width/2, app.height/2 + 20, fill = 'black', 
                        text = '''CONTROLS:
        
        Arrow keys to move chef around the screen

        [C] to chop

        [SPACE] to pick up and place''', 
                        font = 'Courier 20 bold')

    canvas.create_text(app.width/2, app.height/2 + 150, fill = 'black', 
        text = f"You have 4 minutes to complete {app.objectiveOrders} orders!", 
                        font = 'Courier 24 bold')

    canvas.create_text(app.width/2, app.height/2 + 190, fill = 'black', 
                        text = 'Press [P] to Start!', 
                        font = 'Courier 24')

#these methods draw the food items
def drawWiener(app, canvas):
    for wiener in app.maze.wieners:
        x, y = wiener.getLocation()
        if(wiener.cooked):
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.donedog))
        else:
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.dog))

#draws the bun
def drawBun(app, canvas):
    for bun in app.maze.buns:
        x, y = bun.getLocation()
        if(bun.sliced):
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.slicedbun))
        else:
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.bun))

#draws the hot dog based on its type
def drawHotDog(app, canvas):
    for hotdog in app.maze.hotdogs:
        x, y = hotdog.getLocation()
        if(hotdog.condiment == 'ketchup'):
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.ketchup))
        elif(hotdog.condiment == 'mustard'):
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.mustard))
        elif(hotdog.condiment == 'relish'):
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.relish))
        else:
            canvas.create_image(x, y, image=ImageTk.PhotoImage(app.hotdog))

#draws the order sheet in the top right corner
def drawOrder(app, canvas):
    if(app.order.type == 'ketchup'):
        canvas.create_image(700, 80, image=ImageTk.PhotoImage(app.ketchupOrder))
    elif(app.order.type == 'mustard'):
        canvas.create_image(700, 80, image=ImageTk.PhotoImage(app.mustardOrder))
    elif(app.order.type == 'relish'):
        canvas.create_image(700, 80, image=ImageTk.PhotoImage(app.relishOrder))
    else:
        canvas.create_image(700, 80, image=ImageTk.PhotoImage(app.bareOrder))

#draws the score earned by the 
def drawSubmit(app, canvas):
    score = app.maze.prevScore if app.maze.prevScore != None else 0
    canvas.create_image(700, 80, image=ImageTk.PhotoImage(app.emptyOrder))
    if(score > 5):
        canvas.create_text(700, 40,
                        text = f"+{score}", fill = 'darkGreen', 
                        font = 'Calibri 40 bold', anchor = 'n')
    else:
        canvas.create_text(700, 40,
                        text = f"+{score}", fill = 'red', 
                        font = 'Calibri 40 bold', anchor = 'n')
    

    
#draws the timer in the bottom right corner
def doTime(app, canvas): 

    canvas.create_image(780, 680, 
                        image=ImageTk.PhotoImage(app.timerbutton), 
                        anchor = 'ne')

    minute = f'{app.timerCounter//60}'
    second = f'{app.timerCounter%60}'

    if(minute == '0'):
        minute = '00'
    elif(int(minute) < 10):
        minute = '0' + minute
    
    if(second == '0'):
        second = '00'
    elif(int(second) < 10):
        second = '0' + second
    
    canvas.create_text(720, 720,
                        text = minute + ':' + second, 
                        fill = 'black', font = 'Calibri 30 bold', anchor = 'n')

#GAME: iteratively tiles the floor image to cover the whole background
def makeFloor(app, canvas):
    for i in range(len(app.maze.board)):
        for j in range(len(app.maze.board[0])):
            thisX = 80*i
            thisY = 80*j
            canvas.create_image(thisX, thisY, 
                                image=ImageTk.PhotoImage(app.floor))

#GAME: places the image of a countertop at every position
def placeCounters(app, canvas):
    for i in range(len(app.maze.board[0])):
        for j in range(len(app.maze.board)):
            if(app.maze.board[i][j] == 1):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.countertop))
            elif(app.maze.board[i][j] == 2):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.stovetop))
            elif(app.maze.board[i][j] == 3):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.cuttingBoard))
            elif(app.maze.board[i][j] == 4):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.dogBin))
            elif(app.maze.board[i][j] == 5):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.bunBin))
            elif(app.maze.board[i][j] == 6):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.ketchupBin))
            elif(app.maze.board[i][j] == 7):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.mustardBin))
            elif(app.maze.board[i][j] == 8):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.relishBin))
            elif(app.maze.board[i][j] == 9):
                canvas.create_image(i*80, j*80, 
                                    image=ImageTk.PhotoImage(app.plate))


#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#printing
#######################################

def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def print2dList(L):
    print(repr2dList(L))

#######################################

class Map:
    def __init__(self, app):
        self.board = []
        for i in range(app.width//80 + 1):
            row = []
            for j in range(app.height//80 + 1):
                row.append(0)
            self.board.append(row)

        self.mazeCounter(1, 1, len(self.board[0]) - 2, len(self.board) - 2, 0)   
        self.placeOthers()

        self.cuttingBoardIndex = set()
        self.stoveIndex = set()
        self.wienerBinIndex = None
        self.bunBinIndex = None

        self.ketchupIndex = None
        self.mustardIndex = None
        self.relishIndex = None
        self.plateIndex = None

        self.allFood = []
        self.hotdogs = []
        self.wieners = []
        self.buns = []

        self.cookingWieners = set()

        self.prevScore = None
        
        self.doCounterIndex()
        
    #BOARD: recursive division method for countertop generation
    #idea & pseudocode from https://en.wikipedia.org/wiki/Maze_generation
    # _algorithm
    #instead of dividing into 4 each iteration, I am going to divide into 2
    #https://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division
    # -algorithm
    def mazeCounter(self, x, y, width, height, direction, prevHole = (0,0), 
                    prevDir = 1):
        if(width <= 2 or height <= 2):
            return ('hi')
        else:

            prevHoleX, prevHoleY = (prevHole)

            if(direction == 0):
                horiz = True
            elif(direction == 1):
                horiz = False

            wallStartX = x if horiz else random.randrange(x+1, x+width-1)
            wallStartY = random.randrange(y+1, y+height-1) if horiz else y

            holeX = random.randrange(x, x+width) if horiz else wallStartX
            holeY = wallStartY if horiz else random.randrange(y, y+height)


            #conditional to make sure that no passage is blocked by a wall
            if(prevDir != direction):
                if(prevDir == 0):
                    if(wallStartX == prevHoleX):
                        wallStartX += 1
                elif(prevDir == 1):
                    if(wallStartY == prevHoleY):
                        wallStartY += 1

            #build walls onto app.board
            if horiz:
                for wX in range(x, x + width):
                    if(wX != holeX):
                        self.board[wX][wallStartY] = 1
            else:
                for wY in range(y, y + height):

                    if(wY != holeY):
                        self.board[wallStartX][wY] = 1

            #first section 
            x1 = x
            y1 = y
            width1 = width if horiz else (wallStartX - x)
            height1 = (wallStartY - y) if horiz else height - 1

            self.mazeCounter(x1, y1, width1, height1, 
                        self.coinFlipDirection(width1, height1), 
                        (holeX, holeY), direction)

            #second section
            x2 = x if horiz else (wallStartX + 1)
            y2 = (wallStartY) if horiz else y
            width2 = width if horiz else (width - wallStartX)
            height2 = (height - wallStartY) if horiz else height

            self.mazeCounter(x2, y2, width2, height2, 
                                self.coinFlipDirection(width2, height2), 
                                (holeX, holeY), direction)

    #choose the direction of the new wall to be added
    def coinFlipDirection(self, width, height):
        if(width > height):
            return 1 #vertical line
        elif(height > width):
            return 0 #horizontal line
        else:
            return random.randrange(2)

    #places bins, cutting boards, and stoves
    def placeOthers(self):
        counters = {2:2, 3:2, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
        countPlaced = 0

        while True:
            for r in range(len(self.board)):
                    for c in range(len(self.board[0])):
                        if(self.board[r][c] == 1):
                            pick = random.randrange(2, 10)
                            if(counters[pick] > 0):
                                self.board[r][c] = pick
                                counters[pick] = counters[pick] - 1

            #makes sure everything is placed down
            for key in counters:
                if counters[key] == 0:
                    countPlaced += 1
            
            if(countPlaced >= 10):
                break
            
    #sets up variables that store the indexes of the different types of counters
    def doCounterIndex(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(self.board[i][j] == 3):
                    x = (i * 80)
                    y = (j * 80)
                    self.cuttingBoardIndex.add((x, y))
                elif(self.board[i][j] == 2):
                    x = (i * 80) 
                    y = (j * 80)
                    self.stoveIndex.add((x, y))
                elif(self.board[i][j] == 4):
                    x = (i * 80) 
                    y = (j * 80)
                    self.wienerBinIndex = (x, y)
                elif(self.board[i][j] == 5):
                    x = (i * 80) 
                    y = (j * 80)
                    self.bunBinIndex = (x, y)
                elif(self.board[i][j] == 6):
                    x = (i * 80) 
                    y = (j * 80)
                    self.ketchupIndex = (x, y)
                elif(self.board[i][j] == 7):
                    x = (i * 80) 
                    y = (j * 80)
                    self.mustardIndex = (x, y)
                elif(self.board[i][j] == 8):
                    x = (i * 80) 
                    y = (j * 80)
                    self.relishIndex = (x, y)
                elif(self.board[i][j] == 9):
                    x = (i * 80) 
                    y = (j * 80)
                    self.plateIndex = (x, y)

    #returns True if every value in a dictionary is 0
    def allZero(d):
        for key in d:
            if d[key] != 0:
                return False
        return True

#class that holds information for the chef sprite
class Player:
    def __init__(self, app):
        self.cx = 180
        self.cy = 180
        self.dir = 0
        self.isHolding = None
        #sprite visual
        self.spriteCounter = 0
        self.sprites = []
        self.spriteDir = 0
        self.setupSpriteStrips(app)

    #pushes the sprite in the opposite direction so that it doesnt get stuck
    #there is an issue here where the sprite can be shoved into the counter and 
    #start walking backwards
    def correctiveMovement(self, app, thisDir):
        if(thisDir == 0):
            self.cy -= 10
        elif(thisDir == 1):
            self.cy += 10
        elif(thisDir == 2):
            self.cx -= 10
        elif(thisDir == 3):
            self.cx += 10

    #SPRITE: checks if the sprite is able to walk
    def ableToWalk(self, app):
        if(((self.cx > 70              and self.dir == 3) or
            (self.cx < app.width - 70  and self.dir == 2) or
            (self.cy > 70              and self.dir == 1) or
            (self.cy < app.height - 70 and self.dir == 0)    )and
            (not self.onCounter(app) )):
            return True
        return False

    #SPRITE: checks if the sprite is walking into a Counter
    def onCounter(self, app):
        x = self.cx
        y = self.cy
        
        for elem in app.counters:
            boardX, boardY = elem
            boardX *= 80
            boardY *= 80
            if((x < boardX + 70 and
                x > boardX - 70) and 
                (y < boardY + 70 and
                y > boardY - 70)):
                    self.correctiveMovement(app, self.dir)
                    return True
        return False

    def place(self, app):
        thisFood = self.isHolding
        x = self.cx - (self.cx%80)
        y = self.cy - (self.cy%80)
        if(self.dir == 0):
            y += 80
        
        elif(self.dir == 2):
            x += 80

        thisFood.setLocation(app, x, y)

        #ASSEMBLE ORDERS
        if(type(thisFood) == Wiener):
            for bun in app.maze.buns:
                bX, bY = bun.getLocation()
                if(bun.sliced and thisFood.cooked and bX == x and bY == y):
                    hotDog = HotDog(app, bun, thisFood)
                    #add hotdog
                    app.maze.hotdogs.append(hotDog)
                    app.maze.allFood.append(hotDog)

                    #remove bun
                    app.maze.buns.remove(bun)
                    app.maze.allFood.remove(bun)

                    #remove wiener
                    app.maze.wieners.remove(thisFood)
                    app.maze.allFood.remove(thisFood)

        elif(type(thisFood) == Bun):
            for wiener in app.maze.wieners:
                wX, wY = wiener.getLocation()
                if(wiener.cooked and thisFood.sliced and wX == x and wY == y):
                    hotDog = HotDog(app, thisFood, wiener)

                    #add hotdog
                    app.maze.hotdogs.append(hotDog)
                    app.maze.allFood.append(hotDog)

                    #remove bun
                    app.maze.buns.remove(thisFood)
                    app.maze.allFood.remove(thisFood)

                    #add wiener
                    app.maze.wieners.remove(wiener)
                    app.maze.allFood.remove(wiener )
        
        self.isHolding = None

    def pickUp(self, app):
        thisItem = self.closestItem(app)
        if(thisItem == None):
            return
        
        self.isHolding = thisItem
        if(thisItem in app.maze.allFood):
            self.isHolding.setLocation(app, self.cx, self.cy)


    #finds the closest item that is within 120 pixels from the sprite
    def closestItem(self, app):
        smallestDist = 120
        closestXY = None
        for elem in app.maze.allFood:
            x, y = elem.getLocation()
            dist = self.distanceToFood(x, y)
            if(dist < smallestDist):
                smallestDist = dist
                closestXY = elem
        return closestXY

    #calculates distance from the given point to the sprite
    def distanceToFood(self, x,y):
        return math.sqrt((self.cx - x)**2 + (self.cy - y)**2)


    #Sprite cropping base code from:
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheet
    # sWithCropping
    def setupSpriteStrips(self, app):
        #walking sprite
        #FORWARDS 0 
        spritestripF = app.loadImage('forward.png')
        self.spriteF = [ ]
        for i in range(4):
            sprite = spritestripF.crop((140*i, 0, 130+140*i, 250))
            self.spriteF.append(sprite)
        self.sprites.append(self.spriteF)

        #BACKWARDS 1
        spritestripB = app.loadImage('back.png')
        self.spriteB = [ ]
        for i in range(4):
            sprite = spritestripB.crop((20+110*i, 0, 130+110*i, 250))
            self.spriteB.append(sprite)
        self.sprites.append(self.spriteB)

        #RIGHT 2 
        spritestripR = app.loadImage('right.png')
        self.spriteR = []
        for i in range(4):
            sprite = spritestripR.crop((20+110*i, 0, 130+110*i, 250))
            self.spriteR.append(sprite)
        self.sprites.append(self.spriteR)

        #LEFT 3 
        spritestripL = app.loadImage('left.png')
        self.spriteL = []
        for i in range(4):
            sprite = spritestripL.crop((20+110*i, 0, 120+110*i, 250))
            self.spriteL.append(sprite)
        self.sprites.append(self.spriteL)

        #CHOP LEFT
        spritestripCL = app.loadImage('chop.png')
        self.spriteCL = []
        self.spriteCL.append(spritestripCL.crop((0,0,160, 250)))
        self.spriteCL.append(spritestripCL.crop((170,0,335,250)))
        self.sprites.append(self.spriteCL)

        #CHOP RIGHT
        spritestripCR = app.loadImage('chop1.png')
        self.spriteCR = []
        self.spriteCR.append(spritestripCR.crop((0,0,160, 250)))
        self.spriteCR.append(spritestripCR.crop((170,0,335,250)))
        self.sprites.append(self.spriteCR)

#class for order submission
class Order:
    def __init__(self, app, orderNum = random.randrange(4)):
        self.orderNum = orderNum
        self.startTime = app.timerCounter
        self.submitted = False

        if(self.orderNum == 0):
            self.type = 'ketchup'
        elif(self.orderNum == 1):
            self.type = 'mustard'
        elif(self.orderNum == 2):
            self.type = 'relish'
        elif(self.orderNum == 3):
            self.type = None

    #checks if an order is correct
    def isCorrect(self, hotdog):
        if(hotdog.wiener.cooked and hotdog.bun.sliced and 
            hotdog.condiment == self.type):
            return True
        return False

    #scores order and applys new order
    def submit(self, app, hotdog):
        timeTaken = app.timerCounter - self.startTime
        score = 400//timeTaken if timeTaken > 0 else 0
        score = score if self.isCorrect(hotdog) else 0
        app.maze.prevScore = score 
        app.order = None
        if(app.maze.prevScore < 5):
            app.order = Order(app, 0)
        else:
            app.order = Order(app, random.randrange(0,3))


        self.submitted = True
        app.displaying = True

        app.maze.allFood.remove(hotdog)
        app.maze.hotdogs.remove(hotdog)
        app.totalScore += score
        app.completedOrders += 1
        print(score)
        return score
    
#class for weiner
class Wiener:
    def __init__(self, app, x, y):
        self.x = x
        self.y = y
        self.cooked = False
        self.cookTime = 0
        self.onStove = False
        self.onCuttingBoard = False
        self.onMustard = False
        self.onKetchup = False
        self.onRelish = False
        self.onPlate = False

    #sets location of the wiener
    def setLocation(self, app, x, y):
        self.x = x
        self.y = y
        self.onStove = False
        for elem in app.maze.stoveIndex:
            cx, cy = elem
            if(self.x == cx and self.y == cy):
                self.onStove = True
                app.maze.cookingWieners.add(self)
        
    #return location of the wiener
    def getLocation(self):
        return (self.x, self.y)

    #sets wiener to cooked state
    def cookDog(self):
        self.cooked = True
            

#class for the bun
class Bun:
    def __init__(self, app, x, y):
        self.x = x
        self.y = y
        self.sliced = False
        self.cuts = 0
        self.onCuttingBoard = False
        self.onStove = False
        self.onMustard = False
        self.onKetchup = False
        self.onRelish = False
        self.onPlate = False

    #set bun location
    def setLocation(self, app, x, y):
        self.x = x
        self.y = y
        self.onCuttingBoard = False
        for elem in app.maze.cuttingBoardIndex:
            cx, cy = elem

            if(self.x == cx and self.y == cy):
                self.onCuttingBoard = True
                
    #return bun location
    def getLocation(self):
        return (self.x, self.y)

    #set bun to sliced state
    def sliceBun(self):
        self.sliced = True


#class for hotdog (combined bun and wiener)
class HotDog:
    def __init__(self, app, wiener, bun):

        if(type(wiener) == Wiener):
            self.wiener = wiener
            self.bun = bun
        else:
            self.wiener = bun
            self.bun = wiener

        self.condiment = None
        self.onStove = False
        self.onCuttingBoard = False

        self.onMustard = False
        self.onKetchup = False
        self.onRelish = False
        self.onPlate = False

        self.x, self.y = wiener.getLocation()

    #returns location
    def getLocation(self):
        return (self.x,self.y)

    #set location of the hot dog
    def setLocation(self, app, x, y):
        self.x = x
        self.y = y

        self.onKetchup = False
        self.onMustard = False
        self.onRelish = False
        self.onPlate = False

        kX, kY = app.maze.ketchupIndex
        mX, mY = app.maze.mustardIndex
        rX, rY = app.maze.relishIndex
        pX, pY = app.maze.plateIndex

        if(self.condiment == None):
            
            if(self.x == kX and self.y == kY):
                self.onKetchup = True
                self.condiment = 'ketchup'
            elif(self.x == mX and self.y == mY):
                self.onMustard = True
                self.condiment = 'mustard'
            elif(self.x == rX and self.y == rY):
                self.onRelish = True
                self.condiment = 'relish'

        
        if(self.x == pX and self.y == pY):
            self.onPlate = True
            app.order.submit(app, self)
                


runApp(width=800, height=800)