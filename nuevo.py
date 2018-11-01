from tabulate import tabulate
import random 
from collections import deque
import copy

def crearMaquina():
    # print(enumerarMaquinas(6)[0])
    canti_maquinas = eval (input("Cuantas maquinas aleatorias querés generar? :"))
    est = eval(input("Cuantos estados ? :"))
    pasos = eval(input("Cuantos pasos máximo ? :"))
    i = eval(input("Elegí que TAN interante te gustaría ? 1 - MUY, 2 - MASO, 3 - POCO :"))  
    if (i==1):
        x = 90
    else:
        if (i==2):
            x = 60
        else:
            if (i==3):
                x = 30
            else:
                x = 10
    
    maq = enumerarMaquinas(est,canti_maquinas)
    for h in range(0,len(maq),2):#len(maq)):
        pass
        estados = maq[h+1]#['a','b','FIN']#eval(input("Ingrese lista de estados (ej:['q1','FIN'] => "))
        trans = maq[h]
        # cinta = crearCinta()
        test = procesar(trans,estados,pasos,x) #pruebo la cantidad de pasos=3
        if (test!=None):
            print("\n")
            print("********************")
            print(tabulate(test[1],headers=['0', '1'], tablefmt='fancy_grid')) #imprimo la MT como tabla
            print("Cantidad de pasos: ",test[0])
            print("********************")
        
    

def crearCinta():    
    cinta = [] #lista de strings
    # for i in range (0,9):
    #     cinta.insert(0,'0')
    for i in range (0,1000):
        cinta.append('0') 
    return (cinta)

def procesar(trans,estados,cant_pasos,importante):

    cinta = deque('0')
    cabezal = 0 #posicion del cabezal
    pasos = 0
    # fin = estados.pop()
    estado_str = estados[0] #estado inicial a
    estado_idx = 0 #estado inicial a
    
    #chequeo si la maquina es buena
    # if trans[0][1][1] == '<' or trans[0][1][1] == 'FIN' :
    #     return(None)

    while estado_str != "FIN": 
        if pasos==cant_pasos:
            break
        a = list()
        # if trans[estado_idx][0]=='FIN':
        #     return(None)       
        entrada = cinta[cabezal]
        if entrada=='0' and estado_str == trans[estado_idx][0]:
            pasos += 1
            a = trans [estado_idx][1]
            if a[0]=='0':
                cinta[cabezal] = '0'
            if a[0]=='1':
                cinta[cabezal] = '1'
            if a[1]=='>':    
                cinta.append('0')            
                cabezal +=1
            if a[1]=='<':
                if len(cinta)==0:
                    cinta.appendleft('0')
                    cabezal = 0
            if a[2] != 'N' :   
            # print(estado_idx)         
                estado_str = a[2]
                estado_idx = estados.index(a[2]) 
            else:break
                 

        if entrada=='1' and estado_str == trans[estado_idx][0]:
            pasos += 1
            a = trans [estado_idx][2]
            if a[0]=='0':
                cinta[cabezal] = '0'
            if a[0]=='1':
                cinta[cabezal] = '1'
            if a[1]=='>':   
                cinta.append('0')             
                cabezal +=1
            if a[1]=='<':
                if len(cinta)==0:
                    cinta.appendleft('0')
                    cabezal = 0        
            if a[2] != 'N' :
                # print(estado_idx)         
                estado_str = a[2]
                estado_idx = estados.index(a[2])
            else:break     

    limite = Porcentaje(importante,cant_pasos)

    if  pasos>limite and pasos<cant_pasos:                          #pasos<cant_pasos and pasos>1:
        result=[pasos,trans]
        return(result)
    else:
        return(None)

def Porcentaje(X,Y):
    return (int(X*Y/100))
    
def enumerarMaquinas(tam,cant):
    maquinas =[]
    maq_est=[]
    general=[]
    for z in range (0,cant):
        a = [[0] * 3 for i in range(tam)]
        estados = []        
        while len(estados)<tam:
            e = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w'])
            if e in estados:
                pass
            else:
                estados.append(e)
                
        for i in range (0,tam):
            a[i][0]= estados[i] #VER ESTADOS...
            # e1 = random.choice(estados)
            aux = copy.copy(estados)
            e1 = random.choice(estados)
            if (i == 0):
                d1='>'
                c1 = random.choice(['0','1'])
                if (e1 == estados[0]):
                    aux.pop(0)
                    e1 = random.choice(aux)
                    pass   
            else: 
                c1 = random.choice(['0','1'])
                d1 = random.choice(['<','>'])
            a[i][1] =  c1 + d1 + e1
            e2 = random.choice(estados)
            c2 = random.choice(['0','1'])
            d2 = random.choice(['<','>'])
            a[i][2] = c2 + d2 + e2
        
        a[random.randrange(len(estados))][random.randint(1,2)] = 'FIN'
        maquinas.append(a)
        maq_est.append(estados)
        general.append(maquinas[z])
        general.append(maq_est[z])
    return (general)


crearMaquina()
