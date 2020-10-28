
class Tictactoe:
    def checkDiags2(self, sy):
        for i in range(self.sizeX - 2):
            for j in range(self.sizeY - 2):
                if self.tuple[i][j + 2] == sy and self.tuple[i + 1][j + 1] == sy and self.tuple[i + 2][j] == sy:
                    return True
        return False
        
    def checkDiags1(self, sy):
        for i in range(self.sizeX - 2):
            for j in range(self.sizeY - 2):
                if self.tuple[i][j] == sy and self.tuple[i + 1][j + 1] == sy and self.tuple[i + 2][j + 2] == sy:
                    return True
        return False
        
    def checkVertical(self, sy):
        for i in range(self.sizeX - 2):
            for j in range(self.sizeY):
                if self.tuple[i][j] == sy and self.tuple[i + 1][j] == sy and self.tuple[i + 2][j] == sy:
                    return True
        return False
        
    def checkHorizontal(self, sy):
        for i in range(self.sizeX):
            for j in range(self.sizeY - 2):
                if self.tuple[i][j] == sy and self.tuple[i][j + 1] == sy and self.tuple[i][j + 2] == sy:
                    return True
        return False
        
    def checkWin(self, s):
        for check in (self.checkVertical, self.checkHorizontal, self.checkDiags1, self.checkDiags2):
            if check(s):
                return True
        return False
        
    def drawRoof(self):
        for i in range(self.sizeY * 4):
            print(end="-")
        print()
        
    def drawBoard(self):
        for i in range(self.sizeX):
            self.drawRoof()
            for j in range(self.sizeY):
                print(end=f"| {self.tuple[i][j]} ")
            print("|")
            
        self.drawRoof()
        
    def setDimensions(self, row, col):
        self.sizeX = row
        self.sizeY = col
        self.noOfTurns  = row * col
        
        self.tuple = tuple([["-"] * col for i in range(row)])
        
    def __init__(self, sizeX=3, sizeY=3):
        self.setDimensions(sizeX, sizeY)
        self.symbolList = ("X", "O")
        
class CompAI:
    @staticmethod
    def dfDiagonal2(tuple, sym):
        for i in range(len(tuple) - 2):
            for j in range(len(tuple[0]) - 2):
                if tuple[i][j + 2] == sym and tuple[i + 1][j + 1] == sym and tuple[i + 2][j] == "-":
                    CompAI.xy = i + 2, j
                    return True
                if tuple[i][j + 2] == sym and tuple[i + 1][j + 1] == "-" and tuple[i + 2][j] == sym:
                    CompAI.xy = i + 1, j + 1
                    return True
                if tuple[i][j + 2] == "-" and tuple[i + 1][j + 1] == sym and tuple[i + 2][j] == sym:
                    CompAI.xy = i, j + 2
                    return True
        return False
        
    @staticmethod
    def dfDiagonal1(tuple, sym):
        for i in range(len(tuple) - 2):
            for j in range(len(tuple[0]) - 2):
                if tuple[i][j] == sym and tuple[i + 1][j + 1] == sym and tuple[i + 2][j + 2] == "-":
                    CompAI.xy = i + 2, j + 2
                    return True
                if tuple[i][j] == sym and tuple[i + 1][j + 1] == "-" and tuple[i + 2][j + 2] == sym:
                    CompAI.xy = i + 1, j + 1
                    return True
                if tuple[i][j] == "-" and tuple[i + 1][j + 1] == sym and tuple[i + 2][j + 2] == sym:
                    CompAI.xy = i, j
                    return True
        return False
        
    @staticmethod
    def dfHorizontal(tuple, sym):
        for i in range(len(tuple)):
            for j in range(len(tuple[0]) - 2):
                if tuple[i][j] == sym and tuple[i][j + 1] == sym and tuple[i][j + 2] == "-":
                    CompAI.xy = i, j + 2
                    return True
                if tuple[i][j] == sym and tuple[i][j + 1] == "-" and tuple[i][j + 2] == sym:
                    CompAI.xy = i, j + 1
                    return True
                if tuple[i][j] == "-" and tuple[i][j + 1] == sym and tuple[i][j + 2] == sym:
                    CompAI.xy = i, j
                    return True
        return False
        
    @staticmethod
    def dfVertical(tuple, sym):
        for i in range(len(tuple) - 2):
            for j in range(len(tuple[0])):
                if tuple[i][j] == sym and tuple[i + 1][j] == sym and tuple[i + 2][j] == "-":
                    CompAI.xy = i + 2, j
                    return True
                if tuple[i][j] == sym and tuple[i + 1][j] == "-" and tuple[i + 2][j] == sym:
                    CompAI.xy = i + 1, j
                    return True
                if tuple[i][j] == "-" and tuple[i + 1][j] == sym and tuple[i + 2][j] == sym:
                    CompAI.xy = i, j
                    return True
        return False
        
    @staticmethod
    def doDefend(tuple, sym):
        for defend in (CompAI.dfHorizontal, CompAI.dfVertical, CompAI.dfDiagonal1, CompAI.dfDiagonal2):
            if defend(tuple, sym):
                return True, CompAI.xy
        return False, None
        
    @staticmethod
    def twDiagonal2(tuple, sym):
        for i in range(len(tuple) - 2):
            for j in range(len(tuple[0]) - 2):
                if tuple[i][j + 2] == sym and tuple[i + 1][j + 1] == sym and tuple[i + 2][j] == "-":
                    CompAI.xy = i + 2, j
                    return True
                if tuple[i][j + 2] == sym and tuple[i + 1][j + 1] == "-" and tuple[i + 2][j] == sym:
                    CompAI.xy = i + 1, j + 1
                    return True
                if tuple[i][j + 2] == "-" and tuple[i + 1][j + 1] == sym and tuple[i + 2][j] == sym:
                    CompAI.xy = i, j + 2
                    return True
        return False
        
    @staticmethod
    def twDiagonal1(tuple, sym):
        for i in range(len(tuple) - 2):
            for j in range(len(tuple[0]) - 2):
                if tuple[i][j] == sym and tuple[i + 1][j + 1] == sym and tuple[i + 2][j + 2] == "-":
                    CompAI.xy = i + 2, j + 2
                    return True
                if tuple[i][j] == sym and tuple[i + 1][j + 1] == "-" and tuple[i + 2][j + 2] == sym:
                    CompAI.xy = i + 1, j + 1
                    return True
                if tuple[i][j] == "-" and tuple[i + 1][j + 1] == sym and tuple[i + 2][j + 2] == sym:
                    CompAI.xy = i, j
                    return True
        return False
        
    @staticmethod
    def twHorizontal(tuple, sym):
        for i in range(len(tuple)):
            for j in range(len(tuple[0]) - 2):
                if tuple[i][j] == sym and tuple[i][j + 1] == sym and tuple[i][j + 2] == "-":
                    CompAI.xy = i, j + 2
                    return True
                if tuple[i][j] == sym and tuple[i][j + 1] == "-" and tuple[i][j + 2] == sym:
                    CompAI.xy = i, j + 1
                    return True
                if tuple[i][j] == "-" and tuple[i][j + 1] == sym and tuple[i][j + 2] == sym:
                    CompAI.xy = i, j
                    return True
        return False
    
    @staticmethod
    def twVertical(tuple, sym):
        for i in range(len(tuple) - 2):
            for j in range(len(tuple[0])):
                if tuple[i][j] == sym and tuple[i + 1][j] == sym and tuple[i + 2][j] == "-":
                    CompAI.xy = i + 2, j
                    return True
                if tuple[i][j] == sym and tuple[i + 1][j] == "-" and tuple[i + 2][j] == sym:
                    CompAI.xy = i + 1, j
                    return True
                if tuple[i][j] == "-" and tuple[i + 1][j] == sym and tuple[i + 2][j] == sym:
                    CompAI.xy = i, j
                    return True
        return False
        
    @staticmethod
    def thinkWin(tuple, sym):
        for win in (CompAI.twHorizontal, CompAI.twVertical, CompAI.twDiagonal1, CompAI.twDiagonal2):
            if win(tuple, sym):
                return True, CompAI.xy
        return False, None
        
    xy = None