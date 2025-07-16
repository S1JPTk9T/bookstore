
import sqlite3 as db

class Database:
    def __init__(self):
        conn = db.connect('book.db'); 
        cursor  = conn.cursor(); 

        
        self.cursor = cursor
        self.conn = conn 
      

