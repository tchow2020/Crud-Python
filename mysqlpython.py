from unittest import result
from zipapp import create_archive
from django.db import DEFAULT_DB_ALIAS
import mysql.connector
import datetime

data = datetime.date.today()

#conexão com o banco
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="desafio"
)

database = banco.cursor()

#criando a tabela
#database.execute('CREATE TABLE user (user_id int(50) not null auto_increment primary key,name varchar(35),email varchar(50),password varchar(50))')

#crud insert
database.execute("INSERT INTO user (name, email, password) VALUES(%s,%s,%s)" , ('Teste', 'teste@outlook.com', '123456'))
banco.commit()
print(database.rowcount, "dados inseridos", data)

#crud Select
#database.execute('SELECT * FROM user')
#result = database.fetchall()
#for name in result:
#    print(name)
#print(database.rowcount, "resultados encontrados")

#crud Delete
#dell = "DELETE FROM user WHERE name='Gustavo' "
#database.execute(dell)
#banco.commit()
#print(database.rowcount, "coluna deletada")

#crud Update
#att = "UPDATE user SET name = 'Gustavo' WHERE name = 'teste' "
#database.execute(att)
#banco.commit()
#print(database.rowcount, "Atualizado com sucesso")

