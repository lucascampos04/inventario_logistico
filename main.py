import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

window = tk.Tk()
window.title('Inventario domestico')
window.geometry('900x600')
window.configure(background=cor2)
window.resizable(width=False, height=False)

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Frame1.TFrame", background=cor11)

# ----------------- CRIAÇÃO DOS FRAMES ---------------- #
frameNav = ttk.Frame(window, width=1043, height=80, style="Frame1.TFrame")
frameNav.grid(row=0, column=0)

frameSection = ttk.Frame(window, width=1043, height=305, style="Frame1.TFrame")
frameSection.grid(row=1, column=0, pady=1)

frameFotter = ttk.Frame(window, width=1043, height=305, style="Frame1.TFrame")
frameFotter.grid(row=2, column=0, pady=1)

# abrindo img
app_img = Image.open('task.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = tk.Label(frameNav, image=app_img, text='Inventário Domestico', width=900, compound="left", relief="raised", anchor="nw", font=('Verdana 20 bold'), bg=cor11, fg=cor2)
app_logo.place(x=0, y=0)

window.mainloop()
