#Associando ao banco de dados SQLite3

import sqlite3


# Conecta ao banco de dados SQLite, como não existe ainda esse arquivo 'dados.db' ele irá cria se o arquivo não existir
conexao = sqlite3.connect("dados.db")

#criando a tabela do banco. 

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas(
	nome TEXT,
	idade INTEGER,
	salario INTEGER,
	cidade TEXT,
	cpf TEXT
)
""")

#Grava e fecha a conexão
conexao.commit()
conexao.close()
