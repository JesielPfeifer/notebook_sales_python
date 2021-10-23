from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import csv
import re

def botoesSuperior(arg):
    cmdLocalizaNome = Button(arg, text='Localizar por notebook', command=buttonLocalizaNome).pack(side = LEFT, fill = 'x')
    cmdLocalizaEspaco = Button(arg, text='Filtrar por espaco em disco', command=buttonLocalizaEspaco).pack(side = LEFT, fill = 'x')
    cmdLocalizaMarca = Button(arg, text='Filtrar por Data e Marca', command=buttonLocalizaDataMarca).pack(side = LEFT, fill = 'x')
    cmdAplicaDesconto = Button(arg, text='Aplicar desconto', command=buttonAplicarDesconto).pack(side = LEFT, fill = 'x')
    cmdAvaliacoes = Button(arg, text='Mostrar avaliacoes', command=ContagemRating).pack(side = LEFT, fill = 'x')

def importaDados():
    global data, filename

    window = Tk()
    window.title("Selecione um arquivo")
    window.geometry("300x300")
    
    Label(window, text="Selecione um arquivo CSV", borderwidth=2, relief="groove").pack(fill = BOTH, expand = True)

    filename = filedialog.askopenfilename()
    if(filename):
        data = []
        arq = open(filename)
        reader = csv.reader(arq)
        data = list(reader)
        arq.close()
        window.destroy()
    else:
        messagebox.showerror("Error","Arquivo nao foi aberto, encerrando programa!")

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

def LocalizaEspaco():
    if diskSpace.get() == "":
        messagebox.showinfo('Buscar','Necessario uma informação para pesquisar!')
    else:
        global aux
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
        aux = [[col[brand], col[laptopName], col[discount], float(col[list]) - float(col[discount]), col[list]] for col in dados if diskSpace.get().lower() in col[disk].lower()]
        
        window = Tk()
        window.title("Pesquisa por espaco")
        window.geometry('1000x600')

        tree1 = ttk.Treeview(window, columns=("Brand", "LaptopName", "Discount Price", "Discount Amount", "List Price"), height=400, selectmode="extended")

        tree1.heading('Brand', text="Brand", anchor=W)
        tree1.heading('LaptopName', text="LaptopName", anchor=W)
        tree1.heading('Discount Price', text="Discount Price", anchor=W)
        tree1.heading('Discount Amount', text="Discount Amount", anchor=W)
        tree1.heading('List Price', text="List Price", anchor=W)

        tree1.column('#0', stretch=NO, minwidth=0, width=0)
        tree1.column('#1', stretch=NO, minwidth=0, width=100)
        tree1.column('#2', stretch=NO, minwidth=0, width=100)
        tree1.column('#3', stretch=NO, minwidth=0, width=110)
        tree1.column('#4', stretch=NO, minwidth=0, width=160)
        tree1.pack()

        
        for i in range(len(aux)):
            tree1.insert("", 'end', values=(aux[i][0], aux[i][1], aux[i][2], aux[i][3], aux[i][4]))
        
def LocalizaDataMarca():
    if lpData.get() and lpBrand.get() == "":
        messagebox.showinfo('Buscar', 'Digite uma data e marca para buscar')
    else:
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
        aux = [[col[laptopName], col[display], col[disk], col[discount], col[rating]] for col in dados if lpData.get().lower() in col[date].lower() and lpBrand.get().lower() in col[brand].lower()]
        aux.sort()
        
        window = Tk()
        window.title("Pesquisa por data e Marca")
        window.geometry('1000x600')

        tree2 = ttk.Treeview(window, columns=("Laptop Name", "Display Size", "Disk Space", "Discount Price", "Rating"), height=400, selectmode="extended")

        tree2.heading('Laptop Name', text="Laptop Name", anchor=W)
        tree2.heading('Display Size', text="Display Size", anchor=W)
        tree2.heading('Disk Space', text="Disk Space", anchor=W)
        tree2.heading('Discount Price', text="Discount Price", anchor=W)
        tree2.heading('Rating', text="Rating", anchor=W)

        tree2.column('#0', stretch=NO, minwidth=0, width=0)
        tree2.column('#1', stretch=NO, minwidth=0, width=100)
        tree2.column('#2', stretch=NO, minwidth=0, width=100)
        tree2.column('#3', stretch=NO, minwidth=0, width=110)
        tree2.column('#4', stretch=NO, minwidth=0, width=160)
        tree2.pack()

        for i in range(len(aux)):
           tree2.insert("", 'end', values=(aux[i][0], aux[i][1], aux[i][2], aux[i][3], aux[i][4]))

def AplicarDesconto():
    if valorI.get() == "" and valorF.get() == "" and pDiscount.get() == "" and nomeArq.get() == "":
        messagebox.showinfo('Buscar', 'Digite um valor inicial e um final e a porcentagem de desconto para buscar')
    else:
        desc = re.split("%", pDiscount.get())
        desconto = float(desc[0])
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
        i = 0

        for i in range(len(dados)):
           if float(valorI.get()) <= float(dados[i][list]) and float(valorF.get()) >= float(dados[i][list]):
                dados[i][discount] = float(dados[i][list]) - (( float(dados[i][list]) * desconto) / 100)
        
        newArq = open(nomeArq.get(),'w',newline='')
        writer = csv.writer(newArq)
        writer.writerow(cabecalho)
        writer.writerows(dados)
        newArq.close()

        messagebox.showinfo("Aplicar desconto","Novo arquivo gerado e salvo com sucesso")

def ContagemRating():
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
    #print(dados)
    rat = 0.0
    i = 0

    window = Tk()
    window.title("Contagem Rating")
    window.geometry('1000x600')

    tree4 = ttk.Treeview(window, columns=("Avaliações 0 - 0.9", "Avaliações 1 - 1.9", "Avaliações 2 - 2.9", "Avaliações 3 - 3.9", "Avaliações 4 - 4.9", "Avaliações 5"), height=400, selectmode="extended")
    
    tree4.heading('Avaliações 0 - 0.9', text="Avaliações 0 - 0.9", anchor=W)
    tree4.heading('Avaliações 1 - 1.9', text="Avaliações 1 - 1.9", anchor=W)
    tree4.heading('Avaliações 2 - 2.9', text="Avaliações 2 - 2.9", anchor=W)
    tree4.heading('Avaliações 3 - 3.9', text="Avaliações 3 - 3.9", anchor=W)
    tree4.heading('Avaliações 4 - 4.9', text="Avaliações 4 - 4.9", anchor=W)
    tree4.heading('Avaliações 5', text="Avaliações 5", anchor=W)
    tree4.column('#0', stretch=NO, minwidth=0, width=0)
    tree4.column('#1', stretch=NO, minwidth=0, width=100)
    tree4.column('#2', stretch=NO, minwidth=0, width=100)
    tree4.column('#3', stretch=NO, minwidth=0, width=110)
    tree4.column('#4', stretch=NO, minwidth=0, width=160)
    tree4.column('#5', stretch=NO, minwidth=0, width=160)
    tree4.pack()

    um = 0
    dois = 0
    tres  = 0
    quatro = 0 
    cinco = 0
    seis = 0

    for i in range(len(dados)):
        rat = re.split("/", dados[i][rating])
        if float(rat[0]) >= 0 and float(rat[0]) <= 0.9:
            um = um + 1
        elif float(rat[0]) >= 1 and float(rat[0]) <= 1.9:
            dois = dois + 1
        elif float(rat[0]) >= 2 and float(rat[0]) <= 2.9:
            tres = tres + 1
        elif float(rat[0]) >= 3 and float(rat[0]) <= 3.9:
            quatro = quatro + 1
        elif float(rat[0]) >= 4 and float(rat[0]) <= 4.9:
            cinco = cinco + 1
        else:
            seis = seis + 1
    
    tree4.insert("", 'end', values=(um, dois, tres, quatro, cinco, seis))

def buttonLocalizaNome():
    global lpName

    root = Tk()
    root.title("Pesquisa")
    root.geometry("400x100") 

    Label(root, text="Digite um modelo para pesquisar: ").grid(row = 1, column = 0)
    lpName = Entry(root, width=20)
    lpName.grid(row = 1, column =1)
    
    btnBuscar = Button(root, text="Buscar", command=lambda:[LocalizarNome(),root.destroy()]).grid(row=2, column=1)

def buttonLocalizaEspaco():
    global diskSpace

    root = Tk()
    root.title("Pesquisa")
    root.geometry("400x100") 

    Label(root, text="Digite um tamanho de armazenamento para pesquisar: ").grid(row = 1, column = 0)
    diskSpace = Entry(root, width=20)
    diskSpace.grid(row = 1, column =1)
    
    btnBuscar = Button(root, text="Buscar", command=lambda:[LocalizaEspaco(),root.destroy()]).grid(row=2, column=1)

def buttonLocalizaDataMarca():
    global lpData, lpBrand

    root = Tk()
    root.title("Pesquisa")
    root.geometry("400x100") 

    Label(root, text="Digite uma data para pesquisar: ").grid(row = 0, column = 0)
    Label(root, text="Digite uma marca para pesquisar: ").grid(row = 1, column = 0)
    lpData = Entry(root, width=20)
    lpBrand = Entry(root, width=20)
    lpData.grid(row = 0, column = 1)
    lpBrand.grid(row = 1, column = 1)

    btnBuscar = Button(root, text="Buscar", command=lambda:[LocalizaDataMarca(),root.destroy()]).grid(row=2, column=1)

def buttonAplicarDesconto():
    global valorI, valorF, pDiscount, nomeArq
    
    root = Tk()
    root.title("Pesquisa")
    root.geometry("480x120") 

    Label(root, text="Digite um valor inicial: ").grid(row = 0, column = 0)
    Label(root, text="Digite um valor final: ").grid(row = 1, column = 0)
    Label(root, text="Digite um percentual de desconto: ").grid(row = 2, column = 0)
    Label(root, text="Digite o nome do novo arquivo: ").grid(row = 3, column = 0)

    valorI = Entry(root, width=20)
    valorF = Entry(root, width=20)
    pDiscount = Entry(root, width=20)
    nomeArq = Entry(root, width=20)
    
    valorI.grid(row = 0, column = 1)
    valorF.grid(row = 1, column = 1)
    pDiscount.grid(row = 2, column = 1)
    nomeArq.grid(row = 3, column = 1)
    
    btnBuscar = Button(root, text="Buscar", command=lambda:[AplicarDesconto(),root.destroy()]).grid(row=4, column=1)

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
    tree.column('#4', stretch=NO, minwidth=0, width=160)
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
root.geometry('1400x600')
root.resizable(True, True)

#config botoes
configButtonUpper = Frame(root)
configButtonUpper.pack(side = TOP)

#chama botoes pra tela
botoesSuperior(configButtonUpper)

#chama menu e tabelas
criaTabela()

root.mainloop()

