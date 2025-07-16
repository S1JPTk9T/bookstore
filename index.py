
from functions import *


sqdb = BookStore(); 
users = Users(); 
book = BookStore()
line = Line()
loan = Loan()


#cadastrar livros

def cadastroLivro(value):
    if value is not False:
        book.create(value)
    else:
        print("Erro ao criar o livro {}".format(value))



line.getCommand('cbook',lambda value: cadastroLivro(value))


#criar emprestimos de livros
def loanBook(value):
    v1,v2 = value
    if v1 and v2:
        loan.create(v1,v2)


line.getTwoCommand('lbook',lambda value: loanBook(value))

#listar livros emprestados de um usuario

def losBook(value=""):
    if(value != ""):
        loan.show(value)
        

line.getCommand('losbook',lambda value: losBook(value))

#listar livros

def showBook(value):
    if(value is not False):
        book.read(value)
    else:
        book.readAll()
        
    
line.getCommand('sbook',lambda value: showBook(value))


#criar usuario
def createUsers(value):
    if value is not False:
        users.create(value)
        print("Usuario {} criado com sucesso!".format(value))
    else:
        print('erro ao criar o usuario')



line.getCommand("cuser",lambda value: createUsers(value))



#relatorios

#se for passado um id apo o suser e listado um usuario em especifico

def listarUsuarios(value):
    if value is not False:
        users.read(int(value))
    else:
        users.readAll()


line.getCommand("suser",lambda value: listarUsuarios(value))




