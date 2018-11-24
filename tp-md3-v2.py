#Trabajo práctico COLOQUIO - Aimaro Franco- MD 3 
from tabulate import tabulate
import random 
from collections import deque
import copy

def crearMaquina():
    canti_maquinas = eval (input("Cuántas maquinas aleatorias querés generar ? :"))
    est = eval(input("Cuántos estados ? :"))
    pasos = eval(input("Cuántos pasos como máximo ? :"))
    b = input("Desea enumerar SOLO maquinas no borrantes ? (s/n):")
    maq = enumerarMaquinas(est,canti_maquinas,b)      #Se genera la enumeración de las maquinas aleatorioamente
    mayor_pasos = [0]                               #Lista de cantidad de pasos

    for h in range(0,len(maq),2):                   #En este bucle, mando a procesar cada maquina que enumeré antes
        pass
        estados = maq[h+1]
        trans = maq[h]
        test = procesar(trans,estados,pasos)      #pruebo la maquina X . me devuelve pasos, tabla de trancision y borrante
        if (test!=None):
            print("\n")
            print("********************")
            print(tabulate(test[1],headers=['0', '1'], tablefmt='fancy_grid')) #imprimo la MT como tabla
            print("Cantidad de pasos: ",test[0])
            mayor_pasos.append(test[0])
            
            print("********************")
    print("\n")
    print("\n")
    print('INFORME')
    print("********************")
    print ('Cantidad maxima de pasos:  ',max(mayor_pasos))
    print ('Solo hay ',len(mayor_pasos)-1,' maquinas INTERESANTES.')
        

def procesar(trans,estados,cant_pasos):      #esta funcion PROCESA una sola maquina que se le pasa como param

    cinta = deque('0')                                  # estructura para agregar elementos al inicio más eficazmente
    cabezal = 0                                         # posicion del cabezal inicial
    pasos = 0                                           # contador de pasos de cada corrida
    estado_str = estados[0]                             # estado inicial a
    x = len(estados)                                    # cota inferior de corte corrida en maquinas interesantes
    estado_idx = 0                                      # index estado inicial a 
    while estado_str != 'N':                            # El corte del proceso es detectar el FIN en alguno de los pasos
        a = list()                                      # Lista de proceso   
        entrada = cinta[cabezal]
        if entrada=='0' and estado_str == trans[estado_idx][0]:
            a = trans [estado_idx][1]
            if a[0]=='0':
                cinta[cabezal] = '0'
            if a[0]=='1':
                cinta[cabezal] = '1'
            if a[1]=='>':    
                cinta.append('0')            
                cabezal += 1
            if a[1]=='<':
                if cabezal==0:
                    cinta.appendleft('0')
                    cabezal = 0
                if cabezal >= 1:
                    cabezal -= 1 
            if(a[2]=='N'):
                estado_str = a[2]
                if pasos > x and pasos < cant_pasos:
                    result=[pasos,trans]
                    return(result)                
            else:
                estado_str = a[2]
                estado_idx = estados.index(a[2])                    
                
        if entrada=='1' and estado_str == trans[estado_idx][0]:        
            a = trans [estado_idx][2]
            if a[0]=='0':
                cinta[cabezal] = '0'
            if a[0]=='1':
                cinta[cabezal] = '1'
            if a[1]=='>':   
                cinta.append('0')             
                cabezal +=1
            if a[1]=='<':
                if cabezal==0:
                    cinta.appendleft('0')
                    cabezal = 0 
                if cabezal >= 1:
                    cabezal -= 1   
            if(a[2]=='N'):                
                estado_str = a[2]
                if pasos > x and pasos < cant_pasos:
                    result=[pasos,trans]
                    return(result)

            else:
                estado_str = a[2]
                estado_idx = estados.index(a[2])    
                

        pasos += 1          #incremento 1 paso más
        if pasos == cant_pasos:
            return(None)    #si la maquina no LLEGO al FIN y ya supero los pasos, se retorna none.. (Seguiría corriendo)
        
    return(None)        

    
def enumerarMaquinas(tam,cant,borrantes):         # Enumero las maquinas. aleatoriamente
    maquinas =[]
    maq_est=[]
    general=[]
    estados_gen = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for z in range (0,cant):
        a = [[0] * 3 for i in range(tam)]    
        estados = estados_gen[0:tam]
        for i in range (0,tam):
            a[i][0]= estados[i] 
            aux = copy.copy(estados)        # uso copy para duplicar la lista.. a = b , no me sirve acá
            e1 = random.choice(estados) 
            if (i == 0):                    #no permito que en la posicion 0 y estado inicial sea el mismo estado ni '<'
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
            if borrantes == 's':                # no borrante :
                c2 = '1'                        # si leo un '1' , entonces le coloco '1' solamente.
            else:                               # borrante
                c2 = random.choice(['0','1'])   # si leo un '1' , entonces le coloco '0' o '1'
            d2 = random.choice(['<','>'])
            a[i][2] = c2 + d2 + e2
        
        i_aux=random.randrange(len(estados))
        j_aux=random.randint(1,2)
        if i_aux == 0 and j_aux == 1:
            a[0][2] = 'FIN'                     #evito enumerar maq de 1 paso..
        else:
            a[i_aux][j_aux] = 'FIN'             #coloco una instruccion FIN aleatoriamente SOLO 1
        maquinas.append(a)
        maq_est.append(estados)
        general.append(maquinas[z])
        general.append(maq_est[z])
    return (general)


crearMaquina() #FUNCION QUE ARRANCA 