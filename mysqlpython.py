from unittest import result
from zipapp import create_archive
from django.db import DEFAULT_DB_ALIAS
import mysql.connector
import datetime

data = datetime.datetime.today()

#conexão com o banco
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="desafio",
)

database = banco.cursor()

#criando a tabela
#database.execute('CREATE TABLE user (user_id int(50) not null auto_increment primary key,name varchar(35),email varchar(50),password varchar(50))')

def Insert():
    
    database = banco.cursor()  
    
    database.execute("INSERT INTO user (name, email, password, createdAt) VALUES(%s,%s,%s,%s)" , ('Teste2', 'teste@outlook.com', '123456', data))
    banco.commit()
    print(database.rowcount, "dados inseridos")


def Select():
     
    database = banco.cursor()  
     
    database.execute('SELECT * FROM user')
    result = database.fetchall()
    for name in result:
        print(name)
    print(database.rowcount, "resultados encontrados")


def Delete():
    
    dell = "DELETE FROM user WHERE user_id in () "
    database.execute(dell)
    banco.commit()
    print(database.rowcount, "coluna deletada")
    

def Update():
    
    att = f"UPDATE user SET name =  'Cleiton', password = '123Cleitin', email = 'nadinho@gmail.com', updatedAT = '{data}'  WHERE user_id =  26 "
    database.execute(att)
    banco.commit()
    print(database.rowcount, "Atualizado com sucesso")


Update()