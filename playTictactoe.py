import math

from random import randrange
from time import sleep
from tictactoe import Tictactoe
from tictactoe import CompAI
from record import Record

class PlayTictactoe:
    def drawRoof(self, limit):
        for i in range(limit):
            print(end="-")
        print()
        
    def drawSpaces(self, limit):
        for i in range(limit):
            print(end=" ")
        
    def centralizeWord(self, limit, word):
        gSpaceSize = lambda: int((limit - len(word)) / 2) if len(word) % 2 == 0 else int(((limit - len(word)) / 2) + 1)
        size = gSpaceSize()
        
        print()
        
        print(end="|")
        self.drawSpaces(size)
        
        print(end=word)
        self.drawSpaces(size)
        
        print("|")
        
    def menu(self):
        sizeX = 50
        
        self.drawRoof(sizeX)
        
        self.centralizeWord(sizeX - 2, "W  E  L  C  O  M   E")
        self.centralizeWord(sizeX - 2, "T  O    T  H  E ")
        self.centralizeWord(sizeX - 2, "T  I  C  T  A  C  T  O  E ")
        self.centralizeWord(sizeX - 2, "G  A  M  E")
        
        self.drawRoof(sizeX)
        
        input("Press enter to continue . . .")
        
    def enterPos(self, name, symbol, rounds):
        strError = "ERROR: Invalid position. Make sure the inputs are > -1 or <"
        if rounds != 0:
            while True:
                try:
                    sPos = input(f"Enter a position of '{symbol}', {name} <eg. 0 1>: ").split(" ")
                    posX = int(sPos[0])
                    posY = int(sPos[1])
                    
                    if posX < 0 or posX > self.tic.sizeX - 1:
                        print(end=f"{strError} {self.tic.sizeX}. ")
                        raise IndexError
                        
                    if posY < 0 or posY > self.tic.sizeY - 1:
                        print(end=f"{strError} {self.tic.sizeY}. ")
                        raise IndexError
                        
                    if self.tic.tuple[posX][posY] != "-":
                        raise Exception
                        
                    self.tic.tuple[posX][posY] = symbol
                    
                    if self.tic.checkWin(symbol):
                        self.tic.drawBoard()
                        print(f"{name} wins.")
                        Record(name, self.dimen)
                        
                        return -1
                    break
                except IndexError:
                    print("Invalid inputted index. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")
                except:
                    print(f"The position has already a value. Please try again.")
            self.tic.drawBoard()
            return rounds - 1
        self.tic.drawBoard()
        return 0
            
    def posAI(self, name, symbol, rounds):
        doWin = CompAI.thinkWin(self.tic.tuple, symbol)
        
        temp = lambda: "O" if symbol == "X" else "X"
        doDefend = (False, None)
        
        if not doWin[0]:
            doDefend = CompAI.doDefend(self.tic.tuple, temp())
        
        if rounds != 0 and doWin[0]:
            posX, posY = doWin[1]
            
            self.tic.tuple[posX][posY] = symbol
            
            print(f"{name} is thinking . . . ")
            
            sleep(randrange(2, 5))
            self.tic.drawBoard()
            
            print(f"{name} inputted x: {posX} and y: {posY}\n")
            print(f"{name} wins.")
            Record(name, self.dimen)
            
            return 0
            
        elif rounds != 0 and doDefend[0]:
            posX, posY = doDefend[1]
            self.tic.tuple[posX][posY] = symbol
            
            print(f"{name} is thinking . . . ")
            sleep(randrange(2, 5))
            self.tic.drawBoard()
            
            print(f"{name} inputted x: {posX} and y: {posY}\n")
            
            return rounds - 1
            
        elif rounds != 0:
            while True:
                posX = abs(randrange(0, self.tic.sizeX + 1))
                posY = abs(randrange(0, self.tic.sizeY + 1))
                
                if posX < 0 or posX > self.tic.sizeX - 1:
                    continue
                
                if posY < 0 or posY > self.tic.sizeY - 1:
                    continue
                
                if self.tic.tuple[posX][posY] != "-":
                    continue
                
                self.tic.tuple[posX][posY] = symbol
                
                print(f"{name} is thinking . . .")
                
                sleep(randrange(2, 5))
                self.tic.drawBoard()
                
                print(f"{name} inputted x: {posX} and y: {posY}\n")
                
                if not self.tic.checkWin(symbol):
                    break
                
                self.tic.drawBoard()
                print(f"{name} wins.")
                Record(name, self.dimen)
                
                return -1
            return rounds - 1
        return 0
    
    def doPvAI(self, brLoop):
        x     = self.tic.symbolList[0]
        o     = self.tic.symbolList[1]
        turns = self.tic.noOfTurns
        
        if self.sym1 == 0:
            turns = self.enterPos(self.name, x, turns)
            
            if brLoop(turns):
                return False
                
            turns = self.posAI("Computer AI", o, turns)
            
            if brLoop(turns):
                return False
            
        else: 
            turns = self.posAI("Computer AI", x, turns)
            
            if brLoop(turns):
                return False
                
            turns = self.enterPos(self.name, o, turns)
            
            if brLoop(turns):
                return False
            
        self.tic.noOfTurns = turns
        
        return not False
        
    def doPvP(self, brLoop):
        x     = self.tic.symbolList[0]
        o     = self.tic.symbolList[1]
        turns = self.tic.noOfTurns
        
        if self.sym1 == 0:
            turns = self.enterPos(self.p1name, x, turns)
            
            if brLoop(turns):
                return False
                
            turns = self.enterPos(self.p2name, x, turns)
            
            if brLoop(turns):
                return False
            
        else: 
            turns = self.enterPos(self.p2name, x, turns)
            
            if brLoop(turns):
                return False
                
            
            turns = self.enterPos(self.p1name, o, turns)
            
            if brLoop(turns):
                return False
            
        self.tic.noOfTurns = turns
        
        return not False
        
    def doAiVsAi(self, brLoop):
        x     = self.tic.symbolList[0]
        o     = self.tic.symbolList[1]
        turns = self.tic.noOfTurns
        
        if self.sym1 == 0:
            turns = self.posAI(self.nameAI1, x, turns)
            
            if brLoop(turns):
                return False
                
            turns = self.posAI(self.nameAI2, o, turns)
            
            if brLoop(turns):
                return False
            
        else: 
            turns = self.posAI(self.nameAI2, x, turns)
            
            if brLoop(turns):
                return False
                
            turns = self.posAI(self.nameAI1, o, turns)
            
            if brLoop(turns):
                return False
            
        self.tic.noOfTurns = turns
        
        return not False
        
    def playGame(self):
        loop = True
        i    = self.tic.noOfTurns
        
        totTurns = lambda: int(i / 2) if i % 2 == 0 else int((i / 2) + 1)
        brLoop   = lambda i: True if i == -1 or i == 0 else False
        
        rounds = totTurns()
        
        while loop:
            print(f"No of rounds left: {rounds}\n")
                
            if self.ai:
                loop = self.doAiVsAi(brLoop)
            elif self.pvp:
                loop = self.doPvP(brLoop)
            else:
                loop = self.doPvAI(brLoop)
                    
            if brLoop(self.tic.noOfTurns):
                loop = False
            rounds -= 1
            
        if rounds == 0:
            print("Both competetors tied.")
        
        print("Game Over")
        
    def dimensions(self):
        while True:
            try:
                self.dimen = input("\nEnter the tictactoe's dimensions <eg. 3x3>: ")
                val = self.dimen.lower().split("x")
                row = int(val[0])
                col = int(val[1])
                
                if row < 3 or col < 3 or row > 15 or col > 15:
                    raise ValueError
                
                return row, col
            
            except ValueError:
                print("The value must be an integer or not lesser than three or greater than 15.")
            except IndexError:
                print("Invalid inputted index.")
            
    def gameMode(self):
        print("Please choose:\n")
        print("\t1. Player vs AI")
        print("\t2. Player vs Player")
        print("\t3. AI vs AI")
        
        while True:
            try:
                choice =  int(input("\nChoose <1, 2 & 3 only>: "))
                if choice > 0 and choice < 4:
                    return choice
                raise ValueError
            except ValueError:
                print("ERROR: Invalid input. Make sure you entered 1, 2 and 3 only.")
                
    def inputP1S(self):
        mode = self.gameMode()
        if mode == 1:
            self.nameAI = "Computer"
            self.name = input("\nEnter your name: ")
            while True:
                try:
                    symbol = input("Choose between 'X' and 'O': ").capitalize()
                    
                    if symbol == 'X' or symbol == 'O':
                        return symbol
                    raise ValueError
                except ValueError:
                    print("ERROR: Invalid input. Choose only between 'X' and 'O'.")
        
        elif mode == 2:
            self.p1name = input("\nEnter your name player 1: ")
            self.pvp    = True
            while True:
                try:
                    symbol     = input("Choose between 'X 'and 'O': ").capitalize()
                    
                    if symbol == 'X' or symbol == 'O':
                        break
                    raise ValueError
                except ValueError:
                    print("ERROR: Invalid input. Choose only between 'X' and 'O'.")
                except:
                    print("ERRoR: Invalid input. Choose only between 'X' and 'O'.")
                    
            self.p2name = input("Enter your name player 2: ")
            return symbol
            
        self.nameAI1 = input("\nEnter the name of AI 1: ")
        self.nameAI1 = self.nameAI1 + " AI"
        self.ai = True
        while True:
            try:
                symbol     = input("Choose between 'X 'and 'O': ").capitalize()
                
                if symbol == 'X' or symbol == 'O':
                    break
                raise ValueError
            except ValueError:
                print("ERROR: Invalid input. Choose only between 'X' and 'O'.")
            except:
                print("ERRoR: Invalid input. Choose only between 'X' and 'O'.")
                
        self.nameAI2 = input("Enter the name of AI 2: ")
        self.nameAI2 = self.nameAI2 + " AI"
        return symbol
                
    def __init__(self):
        self.tic = None
        self.pvp = False
        self.ai = False
        self.dimen = "3x3"
        self.menu()
        
        temp = lambda: 0 if self.inputP1S() == "X" else 1
        self.sym1 = temp()
        row, col = self.dimensions()
        self.tic = Tictactoe(row, col)
        
        self.tic.drawBoard()
        self.playGame()
        
PlayTictactoe()