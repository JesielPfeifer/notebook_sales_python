from tkinter.ttk import *
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import csv
import os.path

def botoesSuperior(arg):
    cmdLocalizaNome = Button(arg, text='Localizar por notebook', command=buttonLocalizaNome).pack(side = LEFT, fill = 'x')
    cmdLocalizaEspaco = Button(arg, text='Filtrar por espaco em disco', command=buttonLocalizaEspaco).pack(side = LEFT, fill = 'x')
    cmdLocalizaMarca = Button(arg, text='Filtrar por Data e Marca', command=LocalizaDataMarca).pack(side = LEFT, fill = 'x')
    cmdAplicaDesconto = Button(arg, text='Aplicar desconto', command='''LocalizarLaptopName''').pack(side = LEFT, fill = 'x')
    cmdAvaliacoes = Button(arg, text='Mostrar avaliacoes', command='''LocalizarLaptopName''').pack(side = LEFT, fill = 'x')
    
def menuBarra():
    menubar = Menu(root)
    #config menu abrir
    filemenu = Menu(menubar)
    filemenu.add_command(label="Salvar", command= lambda : optSalvar())
    filemenu.add_command(label="Sair", command=root.destroy)
    menubar.add_cascade(label="Arquivo", menu=filemenu)
    #config menu ajuda
    helpmenu = Menu(menubar)
    helpmenu.add_command(label="Informacoes")
    helpmenu.add_command(label="Sobre")
    menubar.add_cascade(label="Ajuda", menu=helpmenu) 
    
    root.config(menu=menubar)

def importaDados():
    global data, filename
    filename = 'notebooks_sale.csv'
    data = []
    arq = open(filename)
    reader = csv.reader(arq)
    data = list(reader)
    arq.close()

def LocalizarNome():
    if lpName.get() == "":
        messagebox.showinfo('Buscar', 'Necessario uma informação para pesquisar!')
    else:
        tree.delete(*tree.get_children())
        cabecalho = [data[0]]
        date = 0
        brand = 1
        laptopName = 2
        display = 3
        processor = 4
        graphics = 5 
        disk = 6
        discount = 7
        list = 8
        rating = 9
        dados = [[col[date], col[brand], col[laptopName], col[display], col[processor], col[graphics], col[disk], col[discount], col[list], col[rating]] for col in data[1::]]
        aux = [[col[date], col[brand], col[laptopName], col[display], col[processor], col[graphics], col[disk], col[discount], col[list], col[rating]] for col in dados if lpName.get().lower() in col[laptopName ].lower()]
       
        for i in range(len(aux)):
            tree.insert("", 'end', values=(aux[i][date], aux[i][brand], aux[i][laptopName], aux[i][display], aux[i][processor], aux[i][graphics], aux[i][disk], aux[i][discount], aux[i][list], aux[i][rating]))

'''def LocalizaEspaco():
    if diskSpace.get() == "":
        messagebox.showinfo('Buscar','Necessario uma informação para pesquisar!')
    else:
        tree.delete(*tree.get_children())
        cabecalho = [data[0]]
        date = 0
        brand = 1
        laptopName = 2
        display = 3
        processor = 4
        graphics = 5 
        disk = 6
        discount = 7
        list = 8
        rating = 9
        dados = [[col[date], col[brand], col[laptopName], col[display], col[processor], col[graphics], col[disk], col[discount], col[list], col[rating]] for col in data[1::]]

        for col in dados:
            if diskSpace.get().lower() in dados:
                discount_amount = float(dados[col][list]) - float(dados[col][discount])

        aux = [[col[brand], col[laptopName], col[discount], col[list], discount_amount] for col in dados if diskSpace.get().lower() in col[disk].lower()]

        for i in range(len(aux)):
            tree.insert("", 'end', values=(aux[i][brand], aux[i][laptopName], discount_amount, aux[i][list]))'''

def LocalizaDataMarca():
    if lpData.get() and lpBrand.get() == "":
        messagebox.showinfo('Buscar', 'Digite uma data e marca para buscar')
    else:
        tree.delete(*tree.get_children())
        cabecalho = [data[0]]
        date = 0
        brand = 1
        laptopName = 2
        display = 3
        processor = 4
        graphics = 5 
        disk = 6
        discount = 7
        list = 8
        rating = 9
        dados = [[col[date], col[brand], col[laptopName], col[display], col[processor], col[graphics], col[disk], col[discount], col[list], col[rating]] for col in data[1::]]
        
        #aux = [[col[date], col[brand], col[laptopName], col[display], col[processor], col[graphics], col[disk], col[discount], col[list], col[rating]] for col in dados if lpData.get().lower() in col[date].lower() and if lpBrand.get().lower() in col[brand].lower()]
        for col in dados:
            if lpData.get().lower() in col[date].lower():
                if lpBrand.get().lower() in col[brand].lower():
                    aux = col[laptopName], col[display], col[disk], col[discount]

        for i in dados:
           tree.insert("", 'end', values=(aux[i][laptopName], aux[i][disk], aux[i][disk], aux[i][discount]))

    
def buttonLocalizaNome():
    global lpName

    root = Tk()
    root.title("Pesquisa")
    root.geometry("400x200") 

    Label(root, text="Digite um modelo para pesquisar: ").grid(row = 1, column = 0)
    lpName = Entry(root, width=20)
    lpName.grid(row = 1, column =1)
    
    btnBuscar = Button(root, text="Buscar", command=lambda:[LocalizarNome(),root.destroy()]).grid(row=2, column=1)

def buttonLocalizaEspaco():
    global diskSpace

    root = Tk()
    root.title("Pesquisa")
    root.geometry("400x200") 

    Label(root, text="Digite um tamanho de armazenamento para pesquisar: ").grid(row = 1, column = 0)
    diskSpace = Entry(root, width=20)
    diskSpace.grid(row = 1, column =1)
    
    btnBuscar = Button(root, text="Buscar", command=lambda:[LocalizaEspaco(),root.destroy()]).grid(row=2, column=1)

def buttonLocalizaDataMarca():
    global lpData, lpBrand

    root = Tk()
    root.title("Pesquisa")
    root.geometry("400x200") 

    Label(root, text="Digite uma data para pesquisar: ").grid(row = 0, column = 0)
    Label(root, text="Digite uma marca para pesquisar: ").grid(row = 1, column = 0)
    lpData = Entry(root, width=20)
    lpBrand = Entry(root, width=20)
    lpData.grid(row = 0, column = 1)
    lpBrand.grid(row = 1, column = 1)

    btnBuscar = Button(root, text="Buscar", command=lambda:[LocalizaDataMarca(),root.destroy()]).grid(row=2, column=1)

def optSalvar():
    files = [('Todos os arquivos', '*.*'),
             ('Python', '*.py'),
             ('Modo texto','*.txt')]
    filename = asksaveasfilename(filetypes = files, defaultextension = files)

def criaTabela():
    global tree
    
    tree = ttk.Treeview(root, columns=("Date", "Brand", "LaptopName", "Display Size", "Processor", "Graphics Card", "Disk Space", "Discount", "List Price", "Rating"), height=400, selectmode="extended")

    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Brand', text="Brand", anchor=W)
    tree.heading('LaptopName', text="LaptopName", anchor=W)
    tree.heading('Display Size', text="Display Size", anchor=W)
    tree.heading('Processor', text="Processor", anchor=W)
    tree.heading('Graphics Card', text="Graphics Card", anchor=W)
    tree.heading('Disk Space', text="Disk Space", anchor=W)
    tree.heading('Discount', text="Discount", anchor=W)
    tree.heading('List Price', text="List Price", anchor=W)
    tree.heading('Rating', text="Rating", anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=110)
    tree.column('#5', stretch=NO, minwidth=0, width=160)
    tree.column('#6', stretch=NO, minwidth=0, width=160)
    tree.column('#7', stretch=NO, minwidth=0, width=160)
    tree.column('#8', stretch=NO, minwidth=0, width=160)
    tree.column('#9', stretch=NO, minwidth=0, width=160)
    tree.pack()
    mostraTabela()

def mostraTabela():
    cabecalho = [data[0]]
    date = 0
    brand = 1
    laptopName = 2
    display = 3
    processor = 4
    graphics = 5
    disk = 6
    discount = 7
    list = 8
    rating = 9
    
    dados = [[col[date], col[brand], col[laptopName], col[display], col[processor], col[graphics], col[disk], col[discount], col[list], col[rating]] for col in data[1::]]
    
    for i in range(len(dados)):
        tree.insert("", 'end', values=(dados[i][0], dados[i][1], dados[i][2], dados[i][3], dados[i][4], dados[i][5], dados[i][6], dados[i][7], dados[i][8], dados[i][9]))

''' MAIN '''
#importa arquivo
importaDados()

#Tamanho Janela inicial
root = Tk()
root.title("Notebook Sales")
#root.geometry('800x600')
root.resizable(True, True)

#config botoes
configButtonUpper = Frame(root)
configButtonUpper.pack(side = TOP)

#chama botoes pra tela
botoesSuperior(configButtonUpper)

#chama menu e tabelas
menuBarra()
criaTabela()

root.mainloop()
