from tabulate import tabulate
def crearMaquina():
    estados = eval(input("Ingrese lista de estados (ej:['q1','FIN'] => "))
    crearFuncion(estados)
       
def crearFuncion ( q ):
    n_filas = len(q)-1 #le resto el estado FIN
    m_col = 3
    print (n_filas)   
    a = [[0] * m_col for i in range(n_filas)]
    
    for i in range (0,n_filas):
        a[i][0]= q[i]
        e1 = input("ingrese transicion Entrada: 0, Estado: "+q[i]+" : ")
        a[i][1] = e1
        e2 = input("ingrese transicion Entrada: 1, Estado: "+q[i]+" : ")
        a[i][2] = e2
    print(tabulate(a,headers=['0', '1'], tablefmt='fancy_grid')) #imprimo la MT como tabla

crearMaquina()


#implementacion de matrices en python : https://snakify.org/es/lessons/two_dimensional_lists_arrays/







