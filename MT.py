
# x = raw_input("Ingrese la entrada [0,1]* : ")
# f = raw_input("Ingrese las transiciones (ejemplo: 0 < a)")
# from numpy import *

def crearMaquina():
    estados = []
    estados = input("Ingrese lista de estados (ej:['q1','FIN'] => ")
    # a = 'FIN' in estados
    crearFuncion(estados)
       

def crearFuncion ( q ):
    alfa = ['0','1']
    numero_filas = len(q)-1     #le resto el estado FIN
    matriz = [range(2) for i in range(numero_filas)]
    print (matriz)   
    
    for i in range (0,numero_filas):
        e = q[i]
        a = input("ingrese transicion estado {e}")
        matriz[i][0] = a
        b = input("ingrese transicion")
        matriz[i][1] = b
    print (matriz)

 
# Menos intuitiva pero mas eficiente
# matriz = [None] * numero_filas
# for i in range(numero_filas):
#     matriz[i] = [None] * numero_columnas

crearMaquina()



#implementacion de matrices en python : http://www.cristalab.com/tutoriales/crear-matrices-en-python-utilizando-listas-c103122l/







