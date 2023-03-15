from cmu_112_graphics import *
from maze import*
from bfs import*

import random 
import math

def appStarted(app):
    ############################### GRAPHICS ###################################
    #this image is from https://logos.fandom.com/wiki/Animal_Crossing 
    app.logoPrv = app.loadImage("graphics" + os.sep + "logo.png").convert()
    app.logo = ImageTk.PhotoImage(app.logoPrv)
    #this image is from https://pokeinfofan.fandom.com/es/wiki/Ciudad_Azalea 
    app.grassPrv = app.loadImage("graphics" + os.sep + "grass.png").convert()
    app.grass = ImageTk.PhotoImage(app.grassPrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=190748 
    app.grass1Prv = app.loadImage("graphics" + os.sep + "grass1.png").convert()
    app.grass1 = ImageTk.PhotoImage(app.grass1Prv)
    #this image is modified from #this image is from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_corn1Prv = app.loadImage("graphics" + os.sep + "brick_corn1.png").convert()
    app.brick_corn1 = ImageTk.PhotoImage(app.brick_corn1Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_corn3Prv = app.loadImage("graphics" + os.sep + "brick_corn3.png").convert()
    app.brick_corn3 = ImageTk.PhotoImage(app.brick_corn3Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_edge0Prv = app.loadImage("graphics" + os.sep + "brick_edge0.png").convert()
    app.brick_edge0 = ImageTk.PhotoImage(app.brick_edge0Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_edge1Prv = app.loadImage("graphics" + os.sep + "brick_edge1.png").convert()
    app.brick_edge1 = ImageTk.PhotoImage(app.brick_edge1Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_corn0Prv = app.loadImage("graphics" + os.sep + "brick_corn0.png").convert()
    app.brick_corn0 = ImageTk.PhotoImage(app.brick_corn0Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_corn2Prv = app.loadImage("graphics" + os.sep + "brick_corn2.png").convert()
    app.brick_corn2 = ImageTk.PhotoImage(app.brick_corn2Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_edge2Prv = app.loadImage("graphics" + os.sep + "brick_edge2.png").convert()
    app.brick_edge2 = ImageTk.PhotoImage(app.brick_edge2Prv)
    #this image is modified from https://medium.com/@mmmulani/creating-a-game-size-world-map-of-pok%C3%A9mon-fire-red-614da729476a
    app.brick_edge3Prv = app.loadImage("graphics" + os.sep + "brick_edge3.png").convert()
    app.brick_edge3 = ImageTk.PhotoImage(app.brick_edge3Prv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=404671
    app.gorl_frontPrv = app.loadImage("graphics" + os.sep + "gorl_front.png").convert()
    app.gorl_front = ImageTk.PhotoImage(app.gorl_frontPrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=404671
    app.gorl_backPrv = app.loadImage("graphics" + os.sep + "gorl_back.png").convert()
    app.gorl_back = ImageTk.PhotoImage(app.gorl_backPrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=404671
    app.gorl_leftPrv = app.loadImage("graphics" + os.sep + "gorl_left.png").convert()
    app.gorl_left = ImageTk.PhotoImage(app.gorl_leftPrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=404671
    app.gorl_rightPrv = app.loadImage("graphics" + os.sep + "gorl_right.png").convert()
    app.gorl_right = ImageTk.PhotoImage(app.gorl_rightPrv)
    #this image is from https://www.pngegg.com/en/png-yanet 
    app.starpointsPrv = app.loadImage("graphics" + os.sep + "starpoints.png").convert()
    app.starpoints = ImageTk.PhotoImage(app.starpointsPrv)
    #this image is from https://www.pinterest.com/pin/596164069393491976/
    app.isabellePrv = app.loadImage("graphics" + os.sep + "isabelle.png").convert()
    app.isabelle = ImageTk.PhotoImage(app.isabellePrv)
    #this image is from https://nookipedia.com/wiki/Item:Peach_(New_Horizons) 
    app.peachFruitPrv = app.loadImage("graphics" + os.sep + "peach.png").convert()
    app.peachFruit = ImageTk.PhotoImage(app.peachFruitPrv)
    #this image is from https://www.pngitem.com/middle/hJbxboo_cabin-clipart-pixel-art-log-cabin-pixel-art/
    app.housePrv = app.loadImage("graphics" + os.sep + "house.png").convert()
    app.house = ImageTk.PhotoImage(app.housePrv)
    #this image is from https://www.pinterest.com/pin/329466528992877295/ 
    app.woodenPrv = app.loadImage("graphics" + os.sep + "wooden.png").convert()
    app.wooden = ImageTk.PhotoImage(app.woodenPrv)
    #this image is from https://acnh.co/flower-images 
    app.pflowerPrv = app.loadImage("graphics" + os.sep + "pflower.png").convert()
    app.pflower = ImageTk.PhotoImage(app.pflowerPrv)
    #this image is from https://www.models-resource.com/3ds/animalcrossingnewleaf/model/20761/ 
    app.baby_treePrv = app.loadImage("graphics" + os.sep + "baby_tree.png").convert()
    app.baby_tree = ImageTk.PhotoImage(app.baby_treePrv)
    #this image is from https://nookipedia.com/wiki/Item:Peach_Tree_%28New_Horizons%29 
    app.peach_treePrv = app.loadImage("graphics" + os.sep + "peach_tree.png").convert()
    app.peach_tree = ImageTk.PhotoImage(app.peach_treePrv)
    #this image is from https://www.shutterstock.com/image-vector/wooden-fence-pixel-art-set-countryside-2220840343 
    app.fencePrv = app.loadImage("graphics" + os.sep + "fence.png").convert()
    app.fence = ImageTk.PhotoImage(app.fencePrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=190748 
    app.bedPrv = app.loadImage("graphics" + os.sep + "bed.png").convert()
    app.bed = ImageTk.PhotoImage(app.bedPrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=190748 
    app.fridgePrv = app.loadImage("graphics" + os.sep + "fridge.png").convert()
    app.fridge = ImageTk.PhotoImage(app.fridgePrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=190748 
    app.stovePrv = app.loadImage("graphics" + os.sep + "stove.png").convert()
    app.stove = ImageTk.PhotoImage(app.stovePrv)
    #this image is from https://www.pokecommunity.com/showthread.php?t=190748 
    app.tablePrv = app.loadImage("graphics" + os.sep + "table.png").convert()
    app.table = ImageTk.PhotoImage(app.tablePrv)
    #this image is from https://nookipedia.com/wiki/Item:Peach_Jam_%28New_Horizons%29 
    app.jamPrv = app.loadImage("graphics" + os.sep + "jam.png").convert()
    app.jam = ImageTk.PhotoImage(app.jamPrv)
    #this image is from https://nookipedia.com/wiki/Bell
    app.bellPrv = app.loadImage("graphics" + os.sep + "bell.png").convert()
    app.bell = ImageTk.PhotoImage(app.bellPrv)
    #this image is from https://nooksguide.com/catalog/item/91587/Sugar 
    app.sugarPrv = app.loadImage("graphics" + os.sep + "sugar.png").convert()
    app.sugar = ImageTk.PhotoImage(app.sugarPrv) 
    #this image is from https://acnh.co/flower-images
    app.tulipPrv = app.loadImage("graphics" + os.sep + "tulip.png").convert()
    app.tulip = ImageTk.PhotoImage(app.tulipPrv)
    #this image is from https://opengameart.org/content/wooden-house-with-animated-door-pixel-art
    app.isahousePrv = app.loadImage("graphics" + os.sep + "isahouse.png").convert()
    app.isahouse = ImageTk.PhotoImage(app.isahousePrv)
    #this image is from https://nookipedia.com/wiki/Item:Hedge_%28New_Horizons%29 
    app.hedgePrv = app.loadImage("graphics" + os.sep + "hedge.png").convert()
    app.hedge = ImageTk.PhotoImage(app.hedgePrv)
    #this image is from https://nookipedia.com/wiki/Item:Hedge_%28New_Horizons%29 
    app.hedge_sqPrv = app.loadImage("graphics" + os.sep + "hedge_sq.png").convert()
    app.hedge_sq = ImageTk.PhotoImage(app.hedge_sqPrv)
    #this image is from https://animalcrossing.fandom.com/wiki/Island_Designer?file=NH-Island_Designer-Dark_dirt_path.png 
    app.dirtPrv = app.loadImage("graphics" + os.sep + "dirt.png").convert()
    app.dirt = ImageTk.PhotoImage(app.dirtPrv)
    #this image is from https://animalcrossing.fandom.com/wiki/Island_Designer?file=NH-Island_Designer-Dark_dirt_path.png 
    app.sandPrv = app.loadImage("graphics" + os.sep + "sand.png").convert()
    app.sand = ImageTk.PhotoImage(app.sandPrv)
    #this image is from https://nookipedia.com/wiki/Item:White-plumeria_bush_(New_Horizons) 
    app.bushPrv = app.loadImage("graphics" + os.sep + "bush.png").convert()
    app.bush = ImageTk.PhotoImage(app.bushPrv)
    

    ################################ Items #####################################
    app.starx = random.randint(5, 9)
    app.stary = random.randint(4, 5)
    app.star = True
    app.peachx1Left = random.randint(5, 6)
    app.peachy1Left = random.randint(11, 14)
    app.peachx2Left = random.randint(5, 6)
    app.peachy2Left = random.randint(11, 14)
    app.peachx3Right = random.randint(10, 11)
    app.peachy3Right = random.randint(10, 13)
    app.peachx4Right = random.randint(10, 11)
    app.peachy4Right = random.randint(10, 13)
    app.peach1 = True
    app.peach2 = True
    app.peach3 = True
    app.peach4 = True
    app.flower = True

    ########################## Character Dirction ##############################
    app.dir = "front"
    app.cx = 0
    app.cy = 0

    ############################ Inventory Tings ###############################
    app.inventoryBox = True

    ################################ Others ####################################
    app.timer = 0

    ################################ Screens ###################################
    app.loadingScreen = True
    app.mainScreen = False
    app.homeScreen = False
    app.cookingScreen = False
    app.jamMakingScreen = False
    app.makeButton1 = -1
    app.makeButton2 = -1
    app.notEnoughForJam = False
    app.addedToInventory = False
    app.drawIsabelle = True
    app.introDialogue = True
    app.finalDialogue = False
    app.buySellScreen = True
    app.sellScreen = False
    app.isabelleAtHome = False
    app.buyScreen = False
    app.payDebtScreen = False
    app.mazeScreen = False
    ######## maze ##############################################################
    app.visited = True
    app.rows = 10
    app.cols = 10
    app.stack = []
    app.wallSides = {'Top': True, 'Bottom': True, 'Left': True, 'Right': True}
    app.directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    app.maze = [[0] * app.cols for row in range(app.rows)]
    app.makeMaze = False
    app.walk = True
    app.mapChange = False
    app.mazeTimer = 0
    

def timerFired(app):
    app.timer += 1
    if app.timer % 500 == 0 and not app.star:
        app.star = True
        app.starx = random.randint(6, 8)
        app.stary = random.randint(4, 6)
    elif app.timer % 300 == 0 and not app.peach1:
        app.peach1 = True
        app.peachx1Left = random.randint(5, 6)
        app.peachy1Left = random.randint(11, 14)
    elif app.timer % 300 == 0 and not app.peach2:
        app.peach2 = True   
        app.peachx2Left = random.randint(5, 6)
        app.peachy2Left = random.randint(11, 14)
    elif app.timer % 300 == 0 and not app.peach3:
        app.peach3 = True  
        app.peachx3Right = random.randint(10, 11)
        app.peachy3Right = random.randint(10, 13)
    elif app.timer % 300 == 0 and not app.peach4:
        app.peach4 = True 
        app.peachx4Right = random.randint(10, 11)
        app.peachy4Right = random.randint(10, 13)
    if app.mazeScreen:
        app.mazeTimer += 1
    if app.mazeTimer > 50 and app.mazeScreen and centerofthebox(finalmaze.m,app.cx,app.cy):
        app.mapChange = True
    if app.mazeTimer > 80 and app.mazeScreen and centerofthebox(finalmaze.m,app.cx,app.cy):
        finalmaze.m = dfsmaze(10, 10, math.floor((app.cx + 32) / 64), math.floor((app.cy + 32) / 64))
        app.mapChange = False
        app.mazeTimer = 0
    
def centerofthebox(m,x,y):
    if (x % 64 > 20 and y % 64 > 20):
        return False
    return True


def keyPressed(app, event):
    if event.key == "Left":
        if app.mainScreen == True:
            if isLegalMain(app.cx - 8, app.cy):
                app.cx -= 8
        elif app.homeScreen == True:
            if isLegalHome(app.cx - 8, app.cy):
                app.cx -= 8
        elif app.mazeScreen == True and not app.mapChange:
            if isLegalMaze(finalmaze.m, app.cx - 8, app.cy):
                app.cx -= 8
        app.dir = "left"
    elif event.key == "Right":
        if app.mainScreen == True:
            if isLegalMain(app.cx + 8, app.cy):
                app.cx += 8
        elif app.homeScreen == True:
            if isLegalHome(app.cx + 8, app.cy):
                app.cx += 8
        elif app.mazeScreen == True and not app.mapChange:
            if isLegalMaze(finalmaze.m, app.cx + 8, app.cy):
                app.cx += 8
        app.dir = "right"
    elif event.key == "Up":
        if app.mainScreen == True:
            if isLegalMain(app.cx, app.cy - 8):
                app.cy -= 8
        elif app.homeScreen == True:
            if isLegalHome(app.cx, app.cy - 8):
                app.cy -= 8
        elif app.mazeScreen == True and not app.mapChange:
            if isLegalMaze(finalmaze.m, app.cx, app.cy - 8):
                app.cy -= 8
        app.dir = "back"
    elif event.key == "Down":
        if app.mainScreen == True:
            if isLegalMain(app.cx, app.cy + 8):
                app.cy += 8
        elif app.homeScreen == True:
            if isLegalHome(app.cx, app.cy + 8):   
                app.cy += 8
        elif app.mazeScreen == True and not app.mapChange:
            if isLegalMaze(finalmaze.m, app.cx, app.cy + 8):
                app.cy += 8
        app.dir = "front"
    elif event.key == "f":
        if (app.starx * 64 - 32 - app.cx == app.width / 2 and 
            app.stary * 64 - 32 - app.cy == app.height / 2 + 24):
            app.star = False
            storage.addInventory("Star", 1)
        if (app.peachx1Left * 64 - 32 - app.cx == app.width / 2 and 
            app.peachy1Left * 64 - 32 - app.cy == app.height / 2 + 24 and 
            app.peach1 == True):
            storage.addInventory("Peach", 1)
            app.peach1 = False
        elif (app.peachx2Left * 64 - 32 - app.cx == app.width / 2 and 
              app.peachy2Left * 64 - 32 - app.cy == app.height / 2 + 24 and
              app.peach2 == True):
              storage.addInventory("Peach", 1)
              app.peach2 = False
        elif (app.peachx3Right * 64 - 32 - app.cx == app.width / 2 and 
              app.peachy3Right * 64 - 32 - app.cy == app.height / 2 + 24 and
              app.peach3 == True):
              storage.addInventory("Peach", 1)
              app.peach3 = False
        elif (app.peachx4Right * 64 - 32 - app.cx == app.width / 2 and 
              app.peachy4Right * 64 - 32 - app.cy == app.height / 2 + 24 and
              app.peach4):
              storage.addInventory("Peach", 1)
              app.peach4 = False
        if app.mazeScreen == True:
            if app.cx > 560 and app.cx < 584 and app.cy > 536 and app.cy < 580:
                storage.addInventory("Flower", 1)
                app.flower = False
    elif event.key == "Tab":
        if app.inventoryBox == False:
            app.inventoryBox = True
        else:
            if app.inventoryBox == True:
                app.inventoryBox = False
    elif event.key == "Enter":
        app.loadingScreen = False
        app.mainScreen = True
    elif event.key == "e":
        if (app.mainScreen == True and (app.cx == 40 and app.cy == -24) or 
            (app.cx == 40 and app.cy == -16)):
            app.mainScreen = False
            app.homeScreen = True
        if (app.homeScreen == True and (app.cx > -24 and app.cx < 24) and 
              (app.cy > 0)):
              app.homeScreen = False
              app.mainScreen = True
        if (app.mainScreen == True and (app.cx == -504 and app.cy > -72 
              and app.cy < 40)):
              app.mainScreen = False
              app.mazeScreen = True
              app.cx = 0
              app.cy = 0
              app.flower = True
        if (app.mazeScreen == True and app.flower == False):
            app.mazeScreen = False
            app.mainScreen = True
            app.cx = -488
            app.cy = -16
    elif event.key == "c":
        if (app.cookingScreen == True and (app.cx > -168 and app.cx < -56) and 
            (app.cy >= -296 and app.cy < -272)):
            app.cookingScreen = False
        else:
            if (app.cookingScreen == False and (app.cx > -168 and app.cx < -56) 
                and (app.cy >= -296 and app.cy < -272)):
                app.cookingScreen = True
    elif event.key == "Backspace":
        app.addedToInventory = False
        app.jamMakingScreen = False
        app.cookingScreen = False
        app.notEnoughForJam = False
        app.payDebtScreen = False
        app.buySellScreen = True

def getMazePoints(app):
    if app.cx > -32 and app.cx < 32 and app.cy > -40 and app.cy < 24:
        return (0, 0)

def screen(x, y):
    if x - 32 >= 896 or y - 32 >= 640 or x + 32 <= 0 or y + 32 <= 0:
        return False
    return True

def drawLoadingScreen(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "azure")
    canvas.create_image(6 * 64 + 40, 2 * 64 + 32, image = app.logo)
    canvas.create_text(6 * 64 + 40, 4 * 64 + 32, text = "112 Paradise",
                       font = "Verdana 26 bold", fill = "darkgoldenrod")
    canvas.create_rectangle(4 * 64, 5 * 64 + 15, 9 * 64 + 32, 9 * 64,
                            fill = "cornsilk", outline = "darkgoldenrod",
                            width = 2)
    canvas.create_text(6 * 64 + 40, 5 * 64 + 40, text = "How To Play",
                       fill = "darkgoldenrod", font = "Verdana 18 bold")
    canvas.create_text(6 * 64 + 45, 6 * 64 + 20, 
                        text = "Press 'Tab' to check your inventory\nPress 'F' to pick up items",
                        fill = "black", font = "Verdana 14")
    canvas.create_text(6 * 64 + 40, 7 * 64, 
                        text = "Go to the kitchen to cook!\nThe path with flowers is the maze",
                        fill = "black", font = "Verdana 14")                    
    canvas.create_text(6 * 64 + 48, 7 * 64 + 45, 
                        text = "The path with sprouts is the garden\nIsabelle will collect debt your debt!",
                        fill = "black", font = "Verdana 14")
    canvas.create_text(6 * 64 + 45, 8 * 64 + 20, 
                        text = "Press 'Enter' to start!",
                        fill = "black", font = "Verdana 14")

def isLegalMain(x, y):
    if (x > -120 and x < 120 and y > -272 and y < -24):
        return False
    elif (x < -1080 or x > 824 or y < -472 or y > 760):
        return False
    elif (x > 576 and x < 816 and y < 48 and y > -192):
        return False
    elif (x > 808 and y < 24 and y > -152):
        return False
    elif (x > 656 and x < 688 and y < 64 and y > -192):
        return False
    elif (x < -504 and x > -968 and y > -216 and y < 184):
        return False
    return True

def isLegalHome(x, y):
    if (x < -184 or x > 184 or y > 8 or y < -352):
        return False
    elif (x > 120 and x < 176 and y > -352 and y < -288):
        return False
    elif (x > -112 and x < -16 and y > -256 and y < -168):
        return False
    elif (x > -176 and x < -128 and y > -344 and y < -288):
        return False
    elif (x > -128 and x < -56 and y > -352 and y < -296):
        return False
    return True

def isLegalMaze(m, x, y):
    row = math.floor((32 + x) / 64)
    col = math.floor((32 + y) / 64)
    if x < -8 or x > 584 or y < -6 or y > 584:
        return False
    elif m[row][col] == -1:
        return False
    return True

def drawMapChange(app, canvas):
    canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                            outline = "black", width = 2)
    canvas.create_text(6 * 64 + 42,  8 * 64 + 32, 
                        text = "Wait! Maze is changing :O",
                        font = "Verdana 14")


def isabelleDialoge(app, canvas):
    if app.cx > 72 and app.cx < 120 and app.cy < 0 and app.cy > -88:
        canvas.create_rectangle(0, 7 * 64 + 32, app.width, 9 * 64 + 32, 
                                fill = "white", outline = "black", width = 2)
        canvas.create_text(7 * 64,  7 * 64 + 60, text = "Hi! I'm Isabelle.",
                            font = "Verdana 14")
        canvas.create_text(7 * 64,  8 * 64 + 15, 
                           text = "Prof. Taylor has built this house for you!",
                            font = "Verdana 14")
        canvas.create_text(7 * 64,  8 * 64 + 35, 
                           text = "However, you do need to repay him! Currently you are 100 Bells in debt.",
                            font = "Verdana 14")
        canvas.create_text(7 * 64,  9 * 64 + 5, 
                           text = "*Click to continue*", fill = "black",
                            font = "Verdana 14")

def isabelleFinalDialogue(app, canvas):
    if app.cx > 72 and app.cx < 120 and app.cy < 0 and app.cy > -88:
        canvas.create_rectangle(0, 7 * 64 + 32, app.width, 9 * 64 + 32, 
                                fill = "white", outline = "black", width = 2)
        canvas.create_text(7 * 64,  7 * 64 + 60, text = "You can pay off your debt by selling me some peach jam!",
                            font = "Verdana 14")
        canvas.create_text(7 * 64,  8 * 64 + 15, 
                           text = "To make peach jam, gather some peaches and come by my house later to buy the sugar.",
                            font = "Verdana 14")
        canvas.create_text(7 * 64,  8 * 64 + 35, 
                           text = "There will also be stars you can collect which will give you some extra bells!",
                            font = "Verdana 14")
        canvas.create_text(7 * 64,  9 * 64 + 5, 
                           text = "I'll see you later! *Click to exit*", fill = "black",
                            font = "Verdana 14")

def drawFlowers(app, canvas):
    canvas.create_image(3 * 64 + 40 - app.cx, 4 * 64 - 20 - app.cy, 
                        image = app.pflower)
    canvas.create_image(3 * 64 + 40 - app.cx, 6 * 64 + 20 - app.cy, 
                        image = app.pflower)
    canvas.create_image(6 * 64 + 10 - app.cx, 8 * 64 + 15 - app.cy, 
                        image = app.baby_tree)
    canvas.create_image(9 * 64 - 10 - app.cx, 8 * 64 + 15 - app.cy, 
                        image = app.baby_tree)

def drawTrees(app, canvas):
    canvas.create_image(5 * 64 - 10 - app.cx, 11 * 64 - app.cy, 
                        image = app.peach_tree)
    canvas.create_image(6 * 64 - 20 - app.cx, 13 * 64 - app.cy, 
                        image = app.peach_tree)
    canvas.create_image(10 * 64 - app.cx, 10 * 64 - app.cy, 
                        image = app.peach_tree)
    canvas.create_image(9 * 64 + 10 - app.cx, 12 * 64 - app.cy, 
                        image = app.peach_tree)

def drawPeach1(app, canvas):
    if app.peach1 == True:
        locationX1 = app.peachx1Left * 64 - 32 - app.cx
        locationY1 = app.peachy1Left * 64 - 32 - app.cy
        canvas.create_image(locationX1, locationY1, image = app.peachFruit)

def drawPeach2(app, canvas):
    if app.peach2 == True:
        locationX3 = app.peachx2Left * 64 - 32 - app.cx
        locationY3 = app.peachy2Left * 64 - 32 - app.cy
        canvas.create_image(locationX3, locationY3, image = app.peachFruit)

def drawPeach3(app, canvas):
    if app.peach3 == True:    
        locationX2 = app.peachx3Right * 64 - 32 - app.cx
        locationY2 = app.peachy3Right * 64 - 32 - app.cy
        canvas.create_image(locationX2, locationY2, image = app.peachFruit)

def drawPeach4(app, canvas):
    if app.peach4 == True:  
        locationX4 = app.peachx4Right * 64 - 32 - app.cx
        locationY4 = app.peachy4Right * 64 - 32 - app.cy
        canvas.create_image(locationX4, locationY4, image = app.peachFruit)
       
def drawGrassyGround(app, canvas):
    for x in range(-20, 30):
        for y in range(-10, 35):
            if screen(x * 64 + 32 - app.cx, y * 64 + 32 - app.cy):
                canvas.create_image(x * 64 + 32 - app.cx, y * 64 + 32 - app.cy, image = app.grass)

def drawGrassPatch(app, canvas):
    for x in range(5, 10):
        for y in range(3, 7):
            canvas.create_image(x * 64 + 32 - app.cx, y * 64 + 32 - app.cy, 
                                image = app.grass1)
    for x in range(5, 10):
        canvas.create_image(x * 64 + 32 - app.cx, 2 * 64 + 32 - app.cy, 
                            image = app.grass1)
        canvas.create_image(x * 64 + 32 - app.cx, 7 * 64 + 32 - app.cy, 
                            image = app.grass1)
    for y in range(3, 7):
        canvas.create_image(4 * 64 + 32 - app.cx, y * 64 + 32 - app.cy, 
                            image = app.grass1)
        canvas.create_image(10 * 64 + 32 - app.cx, y * 64 + 32 - app.cy, 
                            image = app.grass1)
    canvas.create_image(4 * 64 + 32 - app.cx, 2 * 64 + 32 - app.cy, 
                        image = app.grass1)
    canvas.create_image(10 * 64 + 32 - app.cx, 2 * 64 + 32 - app.cy, 
                        image = app.grass1)
    canvas.create_image(4 * 64 + 32 - app.cx, 7 * 64 + 32 - app.cy, 
                        image = app.grass1)
    canvas.create_image(10 * 64 + 32 - app.cx, 7 * 64 + 32 - app.cy, 
                        image = app.grass1)

def drawHouse(app, canvas):
    canvas.create_image(7 * 64 - app.cx, 3 * 64 - app.cy, image = app.house)

def drawIsahouse(app, canvas):
    canvas.create_image(18 * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy, image = app.isahouse)

def drawStonePath(app, canvas):
    canvas.create_image(3 * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy, 
                        image = app.brick_corn1)
    canvas.create_image(3 * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy, 
                        image = app.brick_corn3)   
    canvas.create_image(7 * 64 - app.cx, 8 * 64 + 32 - app.cy, 
                        image = app.brick_corn0)      
    canvas.create_image(8 * 64 - app.cx, 8 * 64 + 32 - app.cy, 
                        image = app.brick_corn1) 
    canvas.create_image(11 * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy, 
                        image = app.brick_corn0)
    canvas.create_image(11 * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy, 
                        image = app.brick_corn2)                    
    for x in range(-1, 3):
        if screen(x * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy):
            canvas.create_image(x * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy, 
                                image = app.brick_edge0)
    for x in range(-1, 3):
        if screen(x * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy):
            canvas.create_image(x * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy, 
                                image = app.brick_edge1)
    for y in range(9, 17):
        if screen(7 * 64 - app.cx, y * 64 + 32 - app.cy):
            canvas.create_image(7 * 64 - app.cx, y * 64 + 32 - app.cy, 
                                image = app.brick_edge2)
    for y in range(9, 17):
        if screen(8 * 64 - app.cx, y * 64 + 32 - app.cy):
            canvas.create_image(8 * 64 - app.cx, y * 64 + 32 - app.cy, 
                                image = app.brick_edge3)
    for x in range(12, 16):
        if screen(x * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy):
            canvas.create_image(x * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy, 
                                image = app.brick_edge0)
    for x in range(12, 16):
        if screen(x * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy):
            canvas.create_image(x * 64 + 32 - app.cx, 5 * 64 + 32 - app.cy, 
                                image = app.brick_edge1)

def drawFence(app, canvas):
    for x in range(-10, 20):
        canvas.create_image(x * 64 + 32 - app.cx, 30 * 35 + 32 - app.cy, image = app.fence)
        canvas.create_image(x * 64 + 32 - app.cx, -6 * 35 + 32 - app.cy, image = app.fence)
    

def drawGorl(app, canvas):
    if app.dir == "front":
        canvas.create_image(app.width / 2, app.height / 2, 
                            image = app.gorl_front)
    elif app.dir == "left":
        canvas.create_image(app.width / 2, app.height / 2, 
                            image = app.gorl_left)
    elif app.dir == "right":
        canvas.create_image(app.width / 2, app.height / 2, 
                            image = app.gorl_right)
    elif app.dir == "back":
        canvas.create_image(app.width / 2, app.height / 2, 
                            image = app.gorl_back)    

def drawGorlInMaze(app, canvas):
    if app.dir == "front":
        canvas.create_image(32 + app.cx, 32 + app.cy, 
                            image = app.gorl_front)
    elif app.dir == "left":
        canvas.create_image(32 + app.cx, 32 + app.cy, 
                            image = app.gorl_left)
    elif app.dir == "right":
        canvas.create_image(32 + app.cx, 32 + app.cy, 
                            image = app.gorl_right)
    elif app.dir == "back":
        canvas.create_image(32 + app.cx, 32 + app.cy, 
                            image = app.gorl_back) 

def drawIsabelle(app, canvas):
    canvas.create_image(8 * 64 + 32 - app.cx, 4 * 64 + 32 - app.cy, 
                        image = app.isabelle)

def drawStar(app, canvas):
    if app.star == True:
        locationX = app.starx * 64 - 32 - app.cx
        locationY = app.stary * 64 - 32 - app.cy
        canvas.create_image(locationX, locationY, image = app.starpoints)

def drawInventoryBox(app, canvas):
    if app.inventoryBox == False:
        canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                7 * 64 + 32, fill = "peachpuff", 
                                outline = "saddlebrown", width = 3)
        canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                3 * 64 + 20, fill = "sandybrown", 
                                outline = "saddlebrown", width = 3)
        canvas.create_text(7 * 64, 3 * 64 - 5, text = "My Inventory",
                           font = 'Verdana 16 bold')
        if "Peach" in storage.getInventory():
            number = storage.inventory["Peach"]
            canvas.create_image(4 * 64 + 25, 4 * 64 - 10, image = app.peachFruit)
            canvas.create_text(4 * 64 + 25, 4 * 64 + 10, 
                               text = f'Peach x{number}',
                               font = 'Verdana 10 bold', anchor = 'n') 
        if "Star" in storage.getInventory():
            number = storage.inventory["Star"]
            canvas.create_image(4 * 64 + 25, 5 * 64 - 10, image = app.starpoints)
            canvas.create_text(4 * 64 + 25, 5 * 64 + 10, 
                               text = f'Star x{number}',
                               font = 'Verdana 10 bold', anchor = 'n')
        if "Sugar" in storage.getInventory():
            number = storage.inventory["Sugar"]
            canvas.create_image(6 * 64 + 16, 4 * 64 - 14, image = app.sugar)
            canvas.create_text(6 * 64 + 16, 4 * 64 + 10, 
                               text = f'Sugar x{number}',
                               font = 'Verdana 10 bold', anchor = 'n')   
        if "Jam" in storage.getInventory():
            number = storage.inventory["Jam"]
            canvas.create_image(7 * 64 + 60, 4 * 64 - 16, image = app.jam)
            canvas.create_text(7 * 64 + 60, 4 * 64 + 10, 
                               text = f'Jam x{number}',
                               font = 'Verdana 10 bold', anchor = 'n')
        if "Flower" in storage.getInventory():
            number = storage.inventory["Flower"]
            canvas.create_image(9 * 64 + 35, 4 * 64 - 16, image = app.tulip)
            canvas.create_text(9 * 64 + 35, 4 * 64 + 10, 
                               text = f'Tulip x{number}',
                               font = 'Verdana 10 bold', anchor = 'n')
                              

def goingIntoHouse(app, canvas):
    if (app.cx == 40 and app.cy == -24) or (app.cx == 40 and app.cy == -16):
        canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                                outline = "black", width = 2)
        canvas.create_text(6 * 64 + 42,  8 * 64 + 32, text = "Press e to enter",
                            font = "Verdana 14")

def goingOutHouse(app, canvas):
    if (app.cx > -24 and app.cx < 24) and (app.cy > 0):
        canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                                outline = "black", width = 2)
        canvas.create_text(6 * 64 + 42,  8 * 64 + 32, text = "Press e to exit",
                            font = "Verdana 14")


def drawInsideHouse(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "black")
    for x in range(4, 10):
        for y in range(6):
            canvas.create_image(x * 64 + 32 - app.cx, y * 64 - app.cy,
                                image = app.wooden)
    canvas.create_image(9 * 64 + 20 - app.cx, 15 - app.cy, image = app.bed)
    canvas.create_image(4 * 64 + 40 - app.cx, 15 - app.cy, image = app.fridge)
    canvas.create_image(5 * 64 + 32 - app.cx, 15 - app.cy, image = app.stove)
    canvas.create_image(6 * 64 - app.cx, 2 * 64 - app.cy, image = app.table)
    canvas.create_rectangle(6 * 64 + 32 - app.cx, 5 * 64 + 22 - app.cy,
                            7 * 64  + 32- app.cx, 5 * 64 + 32 - app.cy,
                            fill = "sienna")

class Collection():
    def __init__(self, money, receipeBook, priceBook, debt, allItems):
        self.money = money
        self.inventory = dict()
        self.receipeBook = receipeBook
        self.priceBook = priceBook
        self.debt = debt
        self.allItems = allItems
        
    def getMoney(self):
        return self.money

    def getInventory(self):
        return self.inventory

    def getDebt(self):
        return self.debt
    
    def getAllItems(self):
        return self.allItems
    
    def getPriceBook(self):
        return self.priceBook

    def getItemNum(self, item):
        self.inventory[item] = self.inventory.get(item, 0)
        return self.inventory[item]

    def addInventory(self, item, num):
        self.inventory[item] = self.inventory.get(item, 0) + num
    
    def makingJam(self, item1, item2):
        if (item1, item2) in self.receipeBook:
            product1 = self.receipeBook[(item1, item2)]
            self.inventory[product1] = self.inventory.get(product1, 0) + 1
            return product1
        else:
            if (item2, item1) in self.receipeBook:
                product2 = self.receipeBook[(item2, item1)]
                self.inventory[product2] = self.inventory.get(product2, 0) + 1
                return product2

    def sellItem(self, item, quantity):
        if item not in self.inventory:
            return "Not in inventory."
        elif self.inventory[item] < quantity:
            return "Not enough in inventory!"
        else:
            self.money += self.priceBook[item] * quantity
            self.inventory[item] = self.inventory.get(item) - quantity
            if quantity > 1 and item != "Peach":
                return f'Sold {quantity} {item}s!'
            elif quantity > 1 and item == "Peach":
                return f'Sold {quantity} {item}es!'
            else:
                if quantity < 1:
                    return f'Sold {quantity} {item}!'

    def buyItem(self, item, quantity):
        if self.money < self.priceBook[item] * quantity:
            return "Insufficient Funds!"
        else:
            self.money -= self.priceBook[item]
            self.inventory[item] = self.inventory.get(item, 0) + quantity
            return f'Bought {quantity} {item}!'
    
    def payOffDebt(self):
        if self.money < 100 and self.debt != 0:
            return "Not enough bells :( Click backspace to exit"
        else:
            if self.money >= 100:
                self.money += self.debt
                self.debt = 0
            return "You've paid off your debt! Congratulations :)"
            

allItems = {"Peach", "Sugar", "Jam", "Flower", "Star"}
receipeBook = {("Peach", "Sugar"): "Jam", 
               ("Sugar", "Peach"): "Jam"}
priceBook = {"Peach": 5, "Sugar": 10, "Jam": 50, "Flower": 20, "Star": 30}
storage = Collection(0, receipeBook, priceBook, -100, allItems)


def drawMoneyBar(app, canvas):
    canvas.create_rectangle(15, 15, 2 * 64 + 32, 50, fill = "oldlace",
                            outline = "saddlebrown", width = 2)
    canvas.create_text(48, 45, text = f'Bells: {storage.getMoney()}', fill = "black",
                       font = "Fixedsys 16", anchor = "sw")
    canvas.create_image(30, 33, image = app.bell)

def drawStartCooking(app, canvas):
    if (app.cx > -168 and app.cx < -56) and (app.cy >= -296 and app.cy < -272):
        canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                                outline = "black", width = 2)
        canvas.create_text(6 * 64 + 42,  8 * 64 + 32, text = "Press c to start cooking!",
                            font = "Verdana 14")

def drawReceipeScreen(app, canvas):
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                7 * 64 + 32, fill = "aliceblue", 
                                outline = "cadetblue", width = 3)
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                3 * 64 + 20, fill = "powderblue", 
                                outline = "cadetblue", width = 3)
    canvas.create_text(7 * 64, 3 * 64 - 5, text = "My Receipes",
                           font = 'Verdana 16 bold')
    canvas.create_image(4 * 64 + 32, 4 * 64 - 10, image = app.jam)
    canvas.create_text(4 * 64 + 32, 4 * 64 + 15, text = 'Peach Jam',
                       font = 'Verdana 10 bold', anchor = 'n') 
    canvas.create_rectangle(4 * 64 - 10, 4 * 64 + 40, 5 * 64 + 10, 4 * 64 + 60,
                            fill = "paleturquoise", outline = "cadetblue",
                            width = 2)
    canvas.create_text(4 * 64 + 32, 4 * 64 + 50, text = 'Make',
                       font = 'Verdana 10 bold') 

def mousePressed(app, event):
    if app.cookingScreen == True:
        app.makeButton1 = event.x
        app.makeButton2 = event.y
        app.buySellScreen = False
        app.sellScreen = False
        app.buyScreen = False
        if ((app.makeButton1 > 4 * 64 - 10 and app.makeButton1 < 5 * 64 + 10) and
            (app.makeButton2 > 4 * 64 + 40 and app.makeButton2 < 4 * 64 + 60)):
            app.jamMakingScreen = True
    if app.jamMakingScreen == True:
        app.cookButton1 = event.x
        app.cookButton2 = event.y
        if ((app.cookButton1 > 6 * 64 + 10 and app.cookButton1 < 8 * 64) and
            (app.cookButton2 > 6 * 64 + 15 and app.cookButton2 < 7 * 64)): 
            if (storage.getInventory()["Peach"] - 4 >= 0 and 
                storage.getInventory()["Sugar"] - 2 >= 0):
                app.addedToInventory = True
                storage.addInventory("Jam", 1)
                storage.getInventory()["Peach"] -= 4
                storage.getInventory()["Sugar"] -= 2  
            elif (storage.getInventory()["Peach"] - 4 < 0 or 
                storage.getInventory()["Sugar"] - 2 < 0):
                app.notEnoughForJam = True
    if app.introDialogue == True:
        if (event.x > 0 and event.x < app.width and event.y > 7 * 64 + 32 and
            event.y <  9 * 64 + 32):
            app.finalDialogue = True
            app.introDialogue = False
    else:
        if app.finalDialogue == True:
            if (event.x > 0 and event.x < app.width and event.y > 7 * 64 + 32 and
                event.y <  9 * 64 + 32):
                app.finalDialogue = False
                app.introDialogue = False
                app.drawIsabelle = False
                app.isabelleAtHome = True
    if app.buySellScreen == True:
        app.buyScreen = False
        app.cookingScreen = False
        app.jamMakingScreen = False
        if (event.x > 4 * 64 + 40 and event.x < 6 * 64 + 40 and 
            event.y > 4 * 64 and event.y < 5 * 64 + 10):
            app.sellScreen = True
            app.buySellScreen = False
            app.payDebtScreen = False
            app.buySellScreen = False
        elif (event.x > 7 * 64 + 20 and event.x < 9 * 64 + 20 and 
              event.y > 4 * 64 and event.y < 5 * 64 + 10):
              app.buyScreen = True
              app.sellScreen = False
              app.payDebtScreen = False
              app.buySellScreen = False
        elif (event.x > 6 * 64 - 15 and event.x < 8 * 64 + 10 and 
              event.y > 6 * 64 - 15 and event.y < 7 * 64 - 10):
              app.payDebtScreen = True
              app.sellScreen = False
              app.buyScreen = False
              app.buySellScreen = False
    if app.sellScreen == True:
        if (event.x > 4 * 64 - 10 and event.x < 5 * 64 + 10 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.sellItem("Peach", 1)
        if (event.x > 4 * 64 - 10 and event.x < 5 * 64 and event.y > 6 * 64 + 24
            and event.y < 7 * 64 - 20):
            storage.sellItem("Star", 1)
        if (event.x > 5 * 64 + 45 and event.x < 7 * 64 - 10 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.sellItem("Sugar", 1)
        if (event.x > 7 * 64 + 25 and event.x < 8 * 64 + 32 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.sellItem("Jam", 1)
        if (event.x > 9 * 64 and event.x < 10 * 64 + 10 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.sellItem("Flower", 1)
        if (event.x > 6 * 64 + 24 and event.x < 8 * 64 - 24 and 
            event.y > 6 * 64 + 49 and event.y < 7 * 64 + 16):
                app.sellScreen = False
                app.buySellScreen = False
                app.payDebtScreen = False
                app.buySellScreen = True
    if app.buyScreen == True:
        if (event.x > 4 * 64 - 10 and event.x < 5 * 64 + 10 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.buyItem("Peach", 1)
        if (event.x > 5 * 64 + 45 and event.x < 7 * 64 - 10 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.buyItem("Sugar", 1)
        if (event.x > 7 * 64 + 25 and event.x < 8 * 64 + 32 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.buyItem("Jam", 1)
        if (event.x > 9 * 64 and event.x < 10 * 64 + 10 and event.y > 4 * 64 + 40
            and event.y < 4 * 64 + 60):
            storage.buyItem("Flower", 1)
        if (event.x > 6 * 64 + 24 and event.x < 8 * 64 - 24 and 
            event.y > 6 * 64 + 49 and event.y < 7 * 64 + 16):
            app.sellScreen = False
            app.buySellScreen = False
            app.payDebtScreen = False
            app.buySellScreen = True

def drawIsabelleAtHome(app, canvas):
    canvas.create_image(17 * 64 + 32 - app.cx, 6 * 64 - 15 - app.cy, 
                        image = app.isabelle)

def drawJamMaking(app, canvas):
    peachNum = storage.getItemNum("Peach")
    sugarNum = storage.getItemNum("Sugar")
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                7 * 64 + 32, fill = "lavenderblush", 
                                outline = "palevioletred", width = 3)
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                3 * 64 + 20, fill = "pink", 
                                outline = "palevioletred", width = 3)
    canvas.create_text(7 * 64, 3 * 64 - 5, text = "Peach Jam",
                           font = 'Verdana 16 bold')
    canvas.create_image(6 * 64, 4 * 64 - 10, image = app.sugar)
    canvas.create_text(7 * 64 + 32, 4 * 64 - 10, text = "Sugar x2", 
                       fill = "black", font = 'Verdana 14 bold')
    canvas.create_image(6 * 64, 4 * 64 + 40, image = app.peachFruit)
    canvas.create_text(7 * 64 + 32, 4 * 64 + 40, text = "Peach x4", 
                       fill = "black", font = 'Verdana 14 bold')
    canvas.create_text(7 * 64, 6 * 64 - 25, text = f"You have: {sugarNum} sugar(s) and {peachNum} peach(es)", 
                       fill = "black", font = 'Verdana 12 bold')
    canvas.create_rectangle(6 * 64 + 10, 6 * 64 + 15, 8 * 64, 7 * 64,
                            fill = "pink", outline = "palevioletred",
                            width = 2)
    canvas.create_text(7 * 64 + 5, 6 * 64 + 40, text = 'Cook!',
                       font = 'Verdana 14 bold') 

def drawNotEnoughForJam(app, canvas):
    canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                                outline = "black", width = 2)
    canvas.create_text(6 * 64 + 42,  8 * 64 + 32, text = "Not enough materials. Press backspace to exit.",
                            font = "Verdana 14")

def drawAddedToInventory(app, canvas):
    canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                                outline = "black", width = 2)
    canvas.create_text(6 * 64 + 42,  8 * 64 + 32, 
                       text = "Added to inventory! Press backspace to exit.",
                       font = "Verdana 14")

def drawBuySellScreen(app, canvas):
    if app.cx > 656 and app.cx < 696 and app.cy > 64 and app.cy < 80:
        app.buySellScreen = True
        canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                    7 * 64 + 32, fill = "lavender", 
                                    outline = "mediumpurple", width = 3)
        canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                                    3 * 64 + 20, fill = "thistle", 
                                    outline = "mediumpurple", width = 3)
        canvas.create_text(7 * 64, 3 * 64 - 5, text = "Choose Option",
                            font = 'Verdana 14 bold')
        canvas.create_rectangle(4 * 64 + 40, 4 * 64, 6 * 64 + 40, 5 * 64 + 10,
                                fill = "thistle", outline = "mediumpurple",
                                width = 3)
        canvas.create_text(5 * 64 + 38, 4 * 64 + 40, text = 'Sell', 
                            font = 'Verdana 14 bold') 
        canvas.create_rectangle(7 * 64 + 20, 4 * 64, 9 * 64 + 20, 5 * 64 + 10,
                                fill = "thistle", outline = "mediumpurple",
                                width = 3)
        canvas.create_text(8 * 64 + 20, 4 * 64 + 40, text = 'Buy',
                            font = 'Verdana 14 bold') 
        canvas.create_rectangle(6 * 64 - 15, 6 * 64 - 15, 8 * 64 + 10, 7 * 64 - 10,
                                fill = "thistle", outline = "mediumpurple",
                                width = 3)
        canvas.create_text(7 * 64 - 5, 6 * 64 + 20, text = 'Pay Debt',
                            font = 'Verdana 14 bold') 

def drawSellScreen(app, canvas):
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                            7 * 64 + 32, fill = "lavender", 
                            outline = "mediumpurple", width = 3)
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                            3 * 64 + 20, fill = "thistle", 
                            outline = "mediumpurple", width = 3)
    canvas.create_text(7 * 64, 3 * 64 - 5, text = "Sell",
                       font = 'Verdana 16 bold')
    if "Peach" in storage.getAllItems(): 
        number = 0 
        if "Peach" in storage.getInventory():  
            number = storage.inventory["Peach"]
        canvas.create_image(4 * 64 + 25, 4 * 64 - 10, image = app.peachFruit)
        canvas.create_text(4 * 64 + 25, 4 * 64 + 10, 
                           text = f'You have x{number}',
                           font = 'Verdana 10 bold', anchor = 'n') 
        canvas.create_rectangle(4 * 64 - 10, 4 * 64 + 40, 5 * 64 + 10, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(4 * 64 + 32, 4 * 64 + 50, text = 'Sell',
                           font = 'Verdana 10 bold') 
    if "Star" in storage.getAllItems():
        number = 0
        if "Star" in storage.getInventory():
            number = storage.inventory["Star"]
        canvas.create_image(4 * 64 + 25, 5 * 64 + 40, image = app.starpoints)
        canvas.create_text(4 * 64 + 25, 5 * 64 + 60, 
                           text = f'You have x{number}',
                           font = 'Verdana 10 bold', anchor = 'n')
        canvas.create_rectangle(4 * 64 - 10, 6 * 64 + 24, 5 * 64, 7 * 64 - 20,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(4 * 64 + 26, 6 * 64 + 34, text = 'Sell',
                           font = 'Verdana 10 bold') 
    if "Sugar" in storage.getAllItems():
        number = 0
        if "Sugar" in storage.getInventory():
            number = storage.inventory["Sugar"]
        canvas.create_image(6 * 64 + 16, 4 * 64 - 14, image = app.sugar)
        canvas.create_text(6 * 64 + 16, 4 * 64 + 10, 
                           text = f'You have x{number}',
                           font = 'Verdana 10 bold', anchor = 'n') 
        canvas.create_rectangle(5 * 64 + 45, 4 * 64 + 40, 7 * 64 - 10, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(6 * 64 + 16, 4 * 64 + 50, text = 'Sell',
                           font = 'Verdana 10 bold')   
    if "Jam" in storage.getAllItems():
        number = 0
        if "Jam" in storage.getInventory():
            number = storage.inventory["Jam"]
        canvas.create_image(8 * 64, 4 * 64 - 16, image = app.jam)
        canvas.create_text(7 * 64 + 60, 4 * 64 + 10, 
                           text = f'You have x{number}',
                           font = 'Verdana 10 bold', anchor = 'n')
        canvas.create_rectangle(7 * 64 + 25, 4 * 64 + 40, 8 * 64 + 32, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(7 * 64 + 60, 4 * 64 + 50, text = 'Sell',
                           font = 'Verdana 10 bold') 
    if "Flower" in storage.getAllItems():
        number = 0
        if "Flower" in storage.getInventory():
            number = storage.inventory["Flower"]
        canvas.create_image(9 * 64 + 35, 4 * 64 - 16, image = app.tulip)
        canvas.create_text(9 * 64 + 35, 4 * 64 + 10, 
                           text = f'You have x{number}',
                           font = 'Verdana 10 bold', anchor = 'n')
        canvas.create_rectangle(9 * 64, 4 * 64 + 40, 10 * 64 + 10, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(9 * 64 + 36, 4 * 64 + 50, text = 'Sell',
                           font = 'Verdana 10 bold') 
        canvas.create_rectangle(6 * 64 + 24, 6 * 64 + 49, 8 * 64 - 24, 7 * 64 + 16,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(7 * 64, 7 * 64, text = "Done", 
                        font = 'Verdana 12 bold')


def drawBuyScreen(app, canvas):
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                            7 * 64 + 32, fill = "lavender", 
                            outline = "mediumpurple", width = 3)
    canvas.create_rectangle(3 * 64 + 32, 2 * 64 + 32, 10 * 64 + 32, 
                            3 * 64 + 20, fill = "thistle", 
                            outline = "mediumpurple", width = 3)
    canvas.create_text(7 * 64, 3 * 64 - 5, text = "Buy",
                       font = 'Verdana 16 bold')
    if "Peach" in storage.getAllItems():
        price = storage.getPriceBook()["Peach"]
        canvas.create_image(4 * 64 + 25, 4 * 64 - 10, image = app.peachFruit)
        canvas.create_text(4 * 64 + 25, 4 * 64 + 10, 
                           text = f'{price} bells',
                           font = 'Verdana 10 bold', anchor = 'n') 
        canvas.create_rectangle(4 * 64 - 10, 4 * 64 + 40, 5 * 64 + 10, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(4 * 64 + 32, 4 * 64 + 50, text = 'Buy',
                           font = 'Verdana 10 bold') 
    if "Sugar" in storage.getAllItems():
        price = storage.getPriceBook()["Sugar"]
        canvas.create_image(6 * 64 + 16, 4 * 64 - 14, image = app.sugar)
        canvas.create_text(6 * 64 + 16, 4 * 64 + 10, 
                           text = f'{price} bells',
                           font = 'Verdana 10 bold', anchor = 'n') 
        canvas.create_rectangle(5 * 64 + 45, 4 * 64 + 40, 7 * 64 - 10, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(6 * 64 + 16, 4 * 64 + 50, text = 'Buy',
                           font = 'Verdana 10 bold')   
    if "Jam" in storage.getAllItems():
        price = storage.getPriceBook()["Jam"]
        canvas.create_image(8 * 64, 4 * 64 - 16, image = app.jam)
        canvas.create_text(7 * 64 + 60, 4 * 64 + 10, 
                           text = f'{price} bells',
                           font = 'Verdana 10 bold', anchor = 'n')
        canvas.create_rectangle(7 * 64 + 25, 4 * 64 + 40, 8 * 64 + 32, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(7 * 64 + 60, 4 * 64 + 50, text = 'Buy',
                           font = 'Verdana 10 bold') 
    if "Flower" in storage.getAllItems():
        price = storage.getPriceBook()["Flower"]
        canvas.create_image(9 * 64 + 35, 4 * 64 - 16, image = app.tulip)
        canvas.create_text(9 * 64 + 35, 4 * 64 + 10, 
                           text = f'{price} bells',
                           font = 'Verdana 10 bold', anchor = 'n')
        canvas.create_rectangle(9 * 64, 4 * 64 + 40, 10 * 64 + 10, 4 * 64 + 60,
                                fill = "thistle", outline = "mediumpurple",
                                width = 2)
        canvas.create_text(9 * 64 + 36, 4 * 64 + 50, text = 'Buy',
                           font = 'Verdana 10 bold')
    canvas.create_rectangle(6 * 64 + 24, 6 * 64 + 49, 8 * 64 - 24, 7 * 64 + 16,
                            fill = "thistle", outline = "mediumpurple",
                            width = 2)
    canvas.create_text(7 * 64, 7 * 64, text = "Done", 
                       font = 'Verdana 12 bold')

def drawPayDebtScreen(app, canvas):
    dialogue = storage.payOffDebt()
    canvas.create_rectangle(0, 7 * 64 + 32, app.width, 9 * 64 + 32, 
                                fill = "white", outline = "black", width = 2)
    canvas.create_text(7 * 64,  8 * 64 + 35, text = f'{dialogue}', 
                       font = "Verdana 14")

def drawMazePatch(app, canvas):
    for x in range(-8, -1):
        for y in range(2, 8):
            if screen(x * 64 + 32 - app.cx, y * 64 + 32 - app.cy):
                canvas.create_image(x * 64 + 32 - app.cx, y * 64 + 32 - app.cy,
                                    image = app.hedge_sq)


def goingIntoMaze(app, canvas):
    if app.cx == -504 and app.cy > -72 and app.cy < 40:
        canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                                outline = "black", width = 2)
        canvas.create_text(6 * 64 + 42,  8 * 64 + 32, 
                           text = "Press e to enter maze and get the tulip!",
                           font = "Verdana 14")


def drawMaze(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "black")
    for i in range(len(finalmaze.m)):
        for j in range(len(finalmaze.m[0])):
            canvas.create_image(i * 64 + 32, j * 64 + 32, image = app.dirt)
            if finalmaze.m[i][j] == 0:
                canvas.create_image(i * 64 + 32, j * 64 + 32, image = app.dirt)
            elif finalmaze.m[i][j] == -1:
                canvas.create_image(i * 64 + 32, j * 64 + 32, image = app.bush)
            else:
                canvas.create_image(i * 64 + 32, j * 64 + 32, image = app.dirt)
    
def drawTulip(app, canvas):
    canvas.create_image(9 * 64 + 32, 9 * 64 + 32, image = app.tulip)


def drawExitMaze(app, canvas):
    canvas.create_rectangle(0, 8 * 64, app.width, 9 * 64, fill = "white",
                            outline = "black", width = 2)
    canvas.create_text(6 * 64 + 42,  8 * 64 + 32, 
                    text = "Press e to exit",
                    font = "Verdana 14")


def redrawAll(app, canvas):
    if app.loadingScreen == True:
        drawLoadingScreen(app, canvas)
    if app.mainScreen == True:
        drawGrassyGround(app, canvas)
        drawGrassPatch(app, canvas)
        drawHouse(app, canvas)
        drawIsahouse(app, canvas)
        drawStonePath(app, canvas)
        drawPeach1(app, canvas)
        drawPeach2(app, canvas)
        drawPeach3(app, canvas)
        drawPeach4(app, canvas)
        drawFlowers(app, canvas)
        if app.drawIsabelle == True:
            drawIsabelle(app, canvas)
        if app.isabelleAtHome == True:
            drawIsabelleAtHome(app, canvas)
        drawMazePatch(app,canvas)
        goingIntoHouse(app, canvas)
        drawGorl(app, canvas)
        drawTrees(app, canvas)
        goingIntoMaze(app, canvas)
        if app.buySellScreen == True:
            drawBuySellScreen(app, canvas)
        if app.introDialogue == True:
            isabelleDialoge(app, canvas)
        if app.finalDialogue == True:
            isabelleFinalDialogue(app, canvas)
        if app.sellScreen == True:
            drawSellScreen(app, canvas)
        if app.buyScreen == True:
            drawBuyScreen(app, canvas)
        if app.payDebtScreen == True:
            drawPayDebtScreen(app, canvas)
        drawFence(app, canvas)
        drawMoneyBar(app, canvas)
        drawFence(app, canvas)
        drawMoneyBar(app, canvas)
        drawMoneyBar(app, canvas)
    if app.homeScreen == True:
        drawInsideHouse(app, canvas)
        drawStar(app, canvas)
        drawGorl(app, canvas)
        goingOutHouse(app, canvas)
        if app.cookingScreen == False:
            drawStartCooking(app, canvas)
        if app.cookingScreen == True:
            drawReceipeScreen(app, canvas)
        if app.jamMakingScreen == True:
            drawJamMaking(app, canvas)
        if app.addedToInventory == True:
            drawAddedToInventory(app, canvas)
        if app.notEnoughForJam == True:
            drawNotEnoughForJam(app, canvas)
        drawMoneyBar(app, canvas)
    if app.mazeScreen == True:
        drawMaze(app,canvas)
        if app.flower == True:
            drawTulip(app, canvas)
        drawGorlInMaze(app, canvas)
        if app.flower == False:
            drawExitMaze(app, canvas)
        if app.mapChange:
            drawMapChange(app, canvas)
    drawInventoryBox(app, canvas)
    canvas.create_text(896 - 32, 32, text = f'{app.cx}  {app.cy}', fill = "white")

runApp(width = 896, height = 640) # 14 x 10

