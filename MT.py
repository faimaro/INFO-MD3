from tabulate import tabulate

# x = raw_input("Ingrese la entrada [0,1]* : ")
# f = raw_input("Ingrese las transiciones (ejemplo: 0 < a)")
# from numpy import *
# from tabulate import tabulate
def crearMaquina():
    # estados = []
    estados = eval(input("Ingrese lista de estados (ej:['q1','FIN'] => "))
    # a = 'FIN' in estados
    crearFuncion(estados)
       

def crearFuncion ( q ):
    alfa = ['0','1']   
    n_filas = len(q)-1 #le resto el estado FIN
    m_col = 3
    print (n_filas)   
    a = [[0] * m_col for i in range(n_filas)]
    print (a)   
    
    for i in range (0,n_filas):
        # e = q[i]
        a[i][0]= q[i]
        e = input("ingrese transicion 0")
        a[i][1] = e
        b = input("ingrese transicion 1")
        a[i][2] = b
    
    print(tabulate(a,headers=['0', '1']))

 
# Menos intuitiva pero mas eficiente
# matriz = [None] * numero_filas
# for i in range(numero_filas):
#     matriz[i] = [None] * numero_columnas

crearMaquina()



#implementacion de matrices en python : https://snakify.org/es/lessons/two_dimensional_lists_arrays/







