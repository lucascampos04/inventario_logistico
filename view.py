import sqlite3 as lite

# conectando com o banco de dados 
con = lite.connect("dados.db")

# ---------------------- CRUD -------------------------- #

# inserindo dados
def inserir_form(i):       
    with con:
        cur = con.cursor()
        query = "INSERT INTO tabela_de_inventario(nome,local,descricao,marca,data_de_compra,valor_da_compra,serie,imagem)VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# atualizando dados
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE tabela_de_inventario SET nome=?, local=?, descricao=?, marca=?, data_de_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# deletar dados 
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tabela_de_inventario WHERE id=?"
        cur.execute(query, i)

# ver dados 
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM tabela_de_inventario"
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            ver_dados.append(rows)
    return ver_dados

# ver dados individulamente 
def ver_item(id): 
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM tabela_de_inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()

        for row in rows:
            ver_dados_individual.append(rows)