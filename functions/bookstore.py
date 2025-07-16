
from functions.database import Database

class BookStore(Database):
    def __init__ (self):
        super().__init__()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL
        )
        ''')
        self.conn.commit()
        
        

    def create(self,titulo):
        if titulo != None:
            self.cursor.execute("insert into livros (titulo) values (?)",(titulo,))
            self.conn.commit()
        
    
    def read(self,id):
            self.cursor.execute('select * from livros where id=(?)',(id,))
            self.formatOut(self.cursor.fetchall())
    
    def readAll(self):
         self.cursor.execute('select * from livros')
         self.formatOut(self.cursor.fetchall())

    
    def formatOut(self,data):
        for id, livro  in data:
             print("id: {} livro: {}".format(id,livro))
         