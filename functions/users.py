from functions.database import Database


class Users(Database):

    def __init__(self):
          super().__init__()

          self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            )
            ''')   
          self.conn.commit()

    def create(self,nome):
          if nome is not None:
               self.cursor.execute('insert into users (nome) values (?)',(nome,))   
               self.conn.commit()
                
    
    def read(self,id):
          if isinstance(id, int):
               self.cursor.execute('select * from users where id = (?)',(id,))
               self.formatOut(self.cursor.fetchall())
         
    
    def readAll(self):
         self.cursor.execute('select * from users')
         self.formatOut(self.cursor.fetchall())
    
    def update(self):
         return True
    
    def delete(self):
         return True
    
    def formatOut(self,data):
         for id,nome in data:
           print("id: {} nome: {}".format(id,nome))
        
        
