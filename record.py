import sqlite3

class Record:
    def setup_db(self):
        self.db_conn = sqlite3.connect("record.db")
        self.theCursor = self.db_conn.cursor()
        
        try:
            self.db_conn.execute("CREATE TABLE IF NOT EXISTS WinnersTictactoe(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name TEXT NOT NULL, Dimensions TEXT NOT NULL);")
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("1 : Couldn't Create a Table")
            
    def submit_score(self, name, dimensions):
        try:
            self.db_conn.execute("INSERT INTO WinnersTictactoe(Name, Dimensions) VALUES('" + name + "', '" + dimensions + "');")
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("2 : Couldn't Submit a Score")
        
    def getScoreBoard(self):
        try:
            result = self.theCursor.execute("SELECT ID, Name, Dimensions FROM WinnersTictactoe;")
            print("\n\nWinners Information List")
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, Dimension: {row[2]}")
                
        except sqlite3.OperationalError:
            print("Failure to select values in the table.")
            
        
    def __init__(self, name, dimensions):
        self.setup_db()
        self.submit_score(name, dimensions)
        self.getScoreBoard()
        
    db_conn = None
    theCursor = None