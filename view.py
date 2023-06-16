import sqlite3 as lite

# conectando com o banco de dados 
con = lite.connect("dados.db")

# ---------------------- CRUD -------------------------- #

# inserindo dados
def inserir_form(i):       
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario_logistico(nome,local,descricao,marca,data_de_compra,valor_da_compra,serie)VALUES(?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# atualizando dados
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario_logistico SET nome=?, local=?, descricao=?, marca=?, data_de_compra=?, valor_da_compra=?, serie=? WHERE id=?"
        cur.execute(query, i)

# deletar dados 
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario_logistico WHERE id=?"
        cur.execute(query, i)

def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario_logistico"
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            ver_dados.append(row)
    return ver_dados


# ver dados individulamente 
def ver_item(id): 
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario_logistico WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()

        for row in rows:
            ver_dados_individual.append(rows)