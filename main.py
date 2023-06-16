import tkinter as tk
from tkinter import StringVar,ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import filedialog as fg
from tkinter import messagebox
# Importandi o banco de dados
from view import *


# funções
global tree

def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_area.get()
    descricao = e_desc.get()
    modelo = e_marca.get()
    data = e_calendario.get()
    valor = e_valorCompra.get()
    serie = e_numSerie.get()
    
    lista_inserir = [nome, local, descricao, modelo, data, valor, serie]

    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        
    inserir_form(lista_inserir)

    messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso.")

    e_nome.delete(0, 'end')
    e_area.delete(0, 'end')
    e_desc.delete(0, 'end')
    e_marca.delete(0, 'end')
    e_calendario.delete(0, 'end')
    e_valorCompra.delete(0, 'end')
    e_numSerie.delete(0, 'end')

    mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = [int(treev_lista[0])]

        e_nome.delete(0, 'end')
        e_area.delete(0, 'end')
        e_desc.delete(0, 'end')
        e_marca.delete(0, 'end')
        e_calendario.delete(0, 'end')
        e_valorCompra.delete(0, 'end')
        e_numSerie.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_area.insert(0, treev_lista[2])
        e_desc.insert(0, treev_lista[3])
        e_marca.insert(0, treev_lista[4])
        e_calendario.insert(0, treev_lista[5])
        e_valorCompra.insert(0, treev_lista[6])
        e_numSerie.insert(0, treev_lista[7])

        imagem = ""
        def update():
            global imagem, imagem_string, l_imagem
            nome = e_nome.get()
            local = e_area.get()
            descricao = e_desc.get()
            modelo = e_marca.get()
            data = e_calendario.get()
            valor = e_valorCompra.get()
            serie = e_numSerie.get()

            imagem = e_numSerie.insert(0, treev_lista[7])

            if imagem == "":
                messagebox.showerror('Error', 'Preencha o campo de imagem')
                return

            lista_atualizar = [nome, local, descricao, modelo, data, valor, serie, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Error', 'Preencha todos os campos')
                    return

            atualizar_dados(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_area.delete(0, 'end')
            e_desc.delete(0, 'end')
            e_marca.delete(0, 'end')
            e_calendario.delete(0, 'end')
            e_valorCompra.delete(0, 'end')
            e_numSerie.delete(0, 'end')

        b_confirmar = tk.Button(frameSection, command=update, text="Confirmar".upper(), width=15, overrelief="ridge", font=("Ivy 8"))
        b_confirmar.place(x=330, y=130)




    except IndexError:
        messagebox.showerror("Erro", 'Seleciona os dados na tabela')
    

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values'] 
        valor = treev_lista[0]
        

        deletar_form([valor])
        
        messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

        mostrar()
    
    except IndexError:
        messagebox.showerror("Erro", 'Seleciona os dados na tabela')


# ---------- cores ----------- #
cor1 = "#FF0000"  # Vermelho
cor2 = "#00FF00"  # Verde
cor3 = "#0000FF"  # Azul
cor4 = "#FFFF00"  # Amarelo
cor5 = "#FF00FF"  # Magenta
cor6 = "#00FFFF"  # Ciano
cor7 = "#FFA500"  # Laranja
cor8 = "#800080"  # Roxo
cor9 = "#008000"  # Verde Escuro
cor10 = "#000080"  # Azul Escuro
cor11 = "#F5F5F5"  # Branco escuro
cor12 = "#000000" # preto

window = tk.Tk()
window.title('Inventario domestico')
window.geometry('900x600')
window.configure(background=cor12)
window.resizable(width=False, height=False)

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Frame1.TFrame", background=cor11)

# ----------------- CRIAÇÃO DOS FRAMES ---------------- #
frameNav = ttk.Frame(window, width=1043, height=80, style="Frame1.TFrame")
frameNav.grid(row=0, column=0)

frameSection = ttk.Frame(window, width=1043, height=305, style="Frame1.TFrame")
frameSection.grid(row=1, column=0, pady=0)

frameFotter = ttk.Frame(window, width=1043, height=305, style="Frame1.TFrame")
frameFotter.grid(row=2, column=0, pady=0, sticky="nsew")

# abrindo img
app_img = Image.open('img/task.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = tk.Label(frameNav, image=app_img, text='Inventário Logistico', width=900, compound="left", relief="raised", anchor="nw", font=('Verdana 20 bold'), bg=cor11, fg=cor12)
app_logo.place(x=0, y=0)

# estilizando o frame meio 

# nome
l_nome = tk.Label(frameSection, text='Nome', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_nome.place(x=10, y=10)
e_nome = tk.Entry(frameSection, width=30, justify="left", relief="solid")
e_nome.place(x=130, y=11)

# area
l_area = tk.Label(frameSection, text='Area', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_area.place(x=10, y=37)
e_area = tk.Entry(frameSection, width=30, justify="left", relief="solid")
e_area.place(x=130, y=38)

# descrição
l_desc = tk.Label(frameSection, text='Descrição', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_desc.place(x=10, y=65)
e_desc = tk.Entry(frameSection, width=30, justify="left", relief="solid")
e_desc.place(x=130, y=66)

# marca modelo
l_marca = tk.Label(frameSection, text='Marca/Modelo', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_marca.place(x=10, y=95)
e_marca = tk.Entry(frameSection, width=30, justify="left", relief="solid")
e_marca.place(x=130, y=96)

# calendario
l_calendario = tk.Label(frameSection, text='Data', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_calendario.place(x=10, y=125)
e_calendario = DateEntry(frameSection, width=12, Background=cor1, bordewidth=2,year=2023)
e_calendario.place(x=130, y=126)

# valor da compra
l_valorCompra = tk.Label(frameSection, text='Valor da compra', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_valorCompra.place(x=10, y=165)
e_valorCompra = tk.Entry(frameSection, width=30, justify="left", relief="solid")
e_valorCompra.place(x=130, y=166)

# numero de serie
l_numSerie = tk.Label(frameSection, text='Número de serie', height=1, anchor="nw", font=("Ivy 10 bold"), bg=cor11, fg=cor12)
l_numSerie.place(x=10, y=195)
e_numSerie = tk.Entry(frameSection, width=30, justify="left", relief="solid")
e_numSerie.place(x=130, y=196)

# ----------------- criando os botões ---------------#

# botão inserir
add_img = Image.open('img/plus.png')
add_img = add_img.resize((20, 20))
add_img = ImageTk.PhotoImage(add_img)

b_inserir = tk.Button(frameSection,image=add_img,command=inserir,text="         adicionar".upper(),width=155,compound="left",overrelief="ridge", anchor='nw',font=("Ivy 8"),justify='left')
b_inserir.place(x=130, y=226)

# botão deletar
remove_img = Image.open('img/remove.png')
remove_img = remove_img.resize((20, 20))
remove_img = ImageTk.PhotoImage(remove_img)

b_inserir = tk.Button(frameSection,image=remove_img, text="  deletar".upper(),command=deletar,width=95,compound="left",overrelief="ridge", anchor='nw',font=("Ivy 8"),justify='left')
b_inserir.place(x=330, y=226)

# botão de atualizar 
atualizar_img = Image.open('img/refresh.png')
atualizar_img = atualizar_img.resize((20, 20))
atualizar_img = ImageTk.PhotoImage(atualizar_img)

b_inserir = tk.Button(frameSection,image=atualizar_img, text="  Atualizar".upper(),width=95,compound="left",command=atualizar,overrelief="ridge", anchor='nw',font=("Ivy 8"),justify='left')
b_inserir.place(x=330, y=180)

# labels - quantidade total e valores
l_total = tk.Label(frameSection, text='',width=17, height=4, anchor="center", font=("Ivy 17 bold"), bg=cor12, fg=cor10)
l_total.place(x=455, y=20)
l_total_ = tk.Label(frameSection, text='Valor total de todos os itens'.upper(), height=2, anchor="center", font=("Ivy 10 bold"), bg=cor12, fg=cor11)
l_total_.place(x=455, y=22)

l_qntd = tk.Label(frameSection, text='',width=17, height=4, pady=5, anchor="center", font=("Ivy 17 bold"),bg=cor12)
l_qntd.place(x=455, y=170)
l_qtnd_ = tk.Label(frameSection, text=' Quantidade total de itens '.upper(), height=2, anchor="center", font=("Ivy 10 bold"), bg=cor12, fg=cor11)
l_qtnd_.place(x=455, y=170)

def mostrar():
    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']
    
    lista_itens = ver_form()

    tree = ttk.Treeview(frameFotter, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameFotter, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameFotter, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameFotter.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor='center')
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
         tree.insert('', 'end', values=(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))


    quantidade = [0]

    for iten in lista_itens:
        if len(iten) >= 7:
            quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qntd['text'] = Total_itens
    
mostrar()

window.mainloop()
