from functions.database import Database


class Loan(Database):
    def __init__ (self):
        super().__init__()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS loan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    
    def create(self,livro_id,user_id):
        self.cursor.execute('INSERT INTO loan (book_id,user_id) select livros.id, users.id  from livros,users where livros.id=? and users.id=?',(livro_id,user_id))
        self.conn.commit()
    
    def show(self,user_id):
        self.cursor.execute('select livros.titulo from loan ' \
        'inner join users on users.id == loan.user_id  ' \
        'inner join livros on livros.id == book_id')
        self.formatOut(self.cursor.fetchall())

    def formatOut(self,data):
        print(list(data))
        
        
        