# 1. Write a Python program to sum all the items in a list
def questao1():
    lista = [1, 2, 4, 7, 9]
    somalista = 0
    for i in lista:
        somalista = i + somalista
    print(somalista)
questao1()

# 2. Write a Python program to multiply all the items in a list
def questao2():
    lista = [1, 2, 4, 7, 9]
    multLista = 1
    for i in lista:
        multLista = i * multLista
    print(multLista)
questao2()

# 3. Write a Python script to add a key to a dictionary
def questao3():
    dica = {0: 10, 1:20}
    dicb = {2:40, 3: 50}
    dicc = {4:70, 5:80}
    z= {}
    z.update(dica)
    z.update(dicb)
    z.update(dicc)
    print(z)
questao3()
    
    


    
