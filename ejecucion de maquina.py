from tabulate import tabulate
import random 


def crearMaquina():
    # print(enumerarMaquinas(6)[0])
    maq = enumerarMaquinas(2)
    estados = maq[1]#['a','b','FIN']#eval(input("Ingrese lista de estados (ej:['q1','FIN'] => "))
    print(maq[0][1])
    print(estados)
    trans = maq[0][1]
    
    #[['a', '1>b', '1<a'], ['b', '0<a', 'fin']] #crearTabla(estados)
    # trans = [['a', 'fin', '1<a'], ['b', 'fin', 'fin']]
    # trans = [['a', '1>b', '1<a'], ['b', '1>c', '0>c'], ['c', '1<a', 'fin']]
    # trans = [['a', '1>b', '1<a'], ['b', '0<a', 'fin']]
    cinta = crearCinta()
    test = procesar(trans,cinta,estados,3) #pruebo la cantidad de pasos=3
    print("kk",test)

       
# def crearTabla ( q ):
#     n_filas = len(q)-1 #le resto el estado FIN
#     m_col = 3
#     print (n_filas)   
#     a = [[0] * m_col for i in range(n_filas)]
    
#     for i in range (0,n_filas):
#         a[i][0]= q[i]
#         e1 = input("ingrese transicion Entrada: 0, Estado: "+q[i]+" : ")
#         a[i][1] = e1
#         e2 = input("ingrese transicion Entrada: 1, Estado: "+q[i]+" : ")
#         a[i][2] = e2
#     print(tabulate(a,headers=['0', '1'], tablefmt='fancy_grid')) #imprimo la MT como tabla
#     # print(a)
#     return (a)
    

def crearCinta():    
    cinta = [] #lista de strings
    # for i in range (0,9):
    #     cinta.insert(0,'0')
    for i in range (0,100):
        cinta.append('0') 
    return (cinta)

def procesar(trans,cinta_entrada,estados,cant_pasos):
    cinta = cinta_entrada
    # print(cinta)
    cabezal = int(len(cinta)/2) #posicion del cabezal
    pasos = 0
    # fin = estados.pop()
    # print(estados)
    estado_str = estados[0] #estado inicial a
    estado_idx = 0 #estado inicial a
    
    #leo
    while estado_str != "fin" or  estado_str != "FIN"  : 
        a = list()
        if trans[estado_idx][0]=='fin' or trans[estado_idx][0]=='FIN':
            return(pasos)       
        entrada = cinta[cabezal]
        if entrada=='0' and estado_str == trans[estado_idx][0]:
            pasos += 1
            a = trans [estado_idx][1]
            if a[0]=='0':
                cinta[cabezal] = '0'
            if a[0]=='1':
                cinta[cabezal] = '1'
            if a[1]=='>':                
                cabezal +=1
            if a[1]=='<':
                cabezal -= 1         
                 

        if entrada=='1' and estado_str == trans[estado_idx][0]:
            pasos += 1
            a = trans [estado_idx][2]
            if a[0]=='0':
                cinta[cabezal] = '0'
            if a[0]=='1':
                cinta[cabezal] = '1'
            if a[1]=='>':                
                cabezal +=1
            if a[1]=='<':
                cabezal -= 1
            

        if a[2] != 'n' and a[2] != 'N' :            
            estado_str = a[2]
            estado_idx = estados.index(a[2])
        else:break
    # print(cinta)        
              
  
    if pasos<=cant_pasos:
        return(True)
    else:
        return(False)

    
def enumerarMaquinas(tam):
    maquinas =[]
    maq_est=[]
    for z in range (0,10):
        # buena=True
        a = [[0] * 3 for i in range(tam)]
        estados = []
        
        while len(estados)<2:
            e = random.choice(['a','b','c','d','e','f','g','h','i','j','k'])
            if e in estados:
                # e = random.choice(['a','b','c','d','e','f','g','h','i'])
                pass
            else:
                estados.append(e)
        for i in range (0,len(estados)):
            a[i][0]= estados[i] #VER ESTADOS...
            e1 = random.choice(estados)
            c1 = random.choice(['0','1'])
            d1 = random.choice(['<','>'])
            a[i][1] =  c1 + d1 + e1
            e2 = random.choice(estados)
            c2 = random.choice(['0','1'])
            d2 = random.choice(['<','>'])
            a[i][2] = c2 + d2 + e2

        a[random.randrange(len(estados))][random.randint(1,2)] = 'FIN'
        # print(a)
        # print(str)
        maquinas.append(a)
    maq_est.append(maquinas)
    maq_est.append(estados)
    return (maq_est)


crearMaquina()
