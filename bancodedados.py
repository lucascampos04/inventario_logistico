import sqlite3 as lite

# criando conexão com o banco de dados 
con = lite.connect('dados.db')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, lecal TEXT, descricao TEXT, marca TEXT, data_de_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")

