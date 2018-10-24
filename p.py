class cambio:
  def __init__(self):
    self.nodo=None
    self.condicion=None
    self.accion=None
    self.mueveCinta=None

cinta=[]
e=0
ep=0
while(e<=0):
  e=int(input("Cuantos elementos tiene su alfabeto: "))
  if(e<=0):
    print "\nEl alfabeto debe tener mas de cero elementos!!!!!!!!!!\n"

print "\nIngresando elementos al alfabeto...\n"
alfabeto=[]
for i in range(e):
  aux=raw_input("Digite el elemento "+str(i+1)+": ")
  alfabeto.append(aux)
alfabeto.append("b")

#while(ep<=0):
ep=int(input("Cuantos elementos tiene su alfabeto de turing : "))
 # if(ep<=0):
  #  print "\nEl alfabeto debe tener mas de cero elementos!!!!!!!!!!\n"

alfabetoTuring=[]
for i in range(ep):
  aux=raw_input("Digite el elemento "+str(i+1)+": ")
  alfabetoTuring.append(aux)
alfabetoTuring.append("b")


n=0
while(n<=1):
  n=int(input("Cuantos nodos tiene su grafo: "))
  if(n<=1):
    print "\nEl grafo  debe tener mas de UN elemento!!!!!!!!!!!\n"

def yaEsta(letra, nuevo):
  for i in range(len(nuevo)):
    if(letra==nuevo[i]):
      return True
  return False

nodo=[range(e+1) for i in range(n)]
for j in range(n):

      for i in range(len(alfabeto)):
        Auxpos=cambio()
        Auxpos.nodo=-1
        hay=raw_input("hay transicion del nodo "+str(j)+" con el elemento "+alfabeto[i]+"?(s/n): ")
        if(hay=="s" or hay=="S"):
          while(int(Auxpos.nodo)<0 or int(Auxpos.nodo)>=n):
            Auxpos.nodo=int(input("Nodo: "))
            if(int(Auxpos.nodo)<0 or int(Auxpos.nodo)>=n):
              print "\nEl nodo al que se llega debe ser: 0 =< nodo < "+str(n)+"!!!!!!!!!!\n"

          Auxpos.accion=raw_input("Accion: ")
          if(yaEsta(Auxpos.accion,alfabetoTuring)==False):
            print "\nLa accion debe estar dentro del alfabeto de turing!!!!!!!!!!\n"
          while(yaEsta(Auxpos.accion,alfabetoTuring)==False):
            Auxpos.accion=raw_input("Accion: ")
            if(yaEsta(Auxpos.accion,alfabetoTuring)==False):
              print "\nLa accion debe estar dentro del alfabeto de PILA!!!!!!!!!!\n"

          Auxpos.mueveCinta=raw_input("Moviemiento de la cinta(i/d): ")
          if(Auxpos.mueveCinta!="i" and Auxpos.mueveCinta!="d"):
            print "\nEl movimiento debe ser a Izquierda o Derecha (i/d) \n"
          while(Auxpos.mueveCinta!="i" and Auxpos.mueveCinta!="d"):
            Auxpos.mueveCinta=raw_input("Moviemiento de la cinta(i/d): ")
            if(Auxpos.mueveCinta!="i" and Auxpos.mueveCinta!="d"):
             print "\nEl movimiento debe ser a Izquierda o Derecha (i/d) \n"


          nodo[j][i]=Auxpos
        else:
          nodo[j][i]="Na"

finales=[]
f=input("Cuantos estados finales: ")
for i in range(f):
  auxi=input("Estado final "+ str(i+1)+": ")
  finales.append(auxi)

def buscar(letra):
    for i in range(len(alfabeto)):
      if(letra==alfabeto[i]):
        return i

pos_actual=1
nodo_actual=0

def verificar(cadena):
  global cinta,nodo_actual,pos_actual
  cinta.append("b")
  for i in cadena:
    cinta.append(i)
  cinta.append("b")
  while(True):
    prueba=nodo[nodo_actual][buscar(cinta[pos_actual])]
    if(prueba=="Na"):
      break
    else:
      nodo_actual=prueba.nodo
      cinta[pos_actual]=prueba.accion
      if(prueba.mueveCinta=="d"):
        pos_actual+=1
        if(pos_actual>(len(cinta)-1)):
          cinta.append("b")
      else:
        pos_actual-=1
        if(pos_actual<0):
          pos_actual=0
          cinta=["b"]+cinta

while(True):
  cadena=raw_input("Escribe la cadena que deseas probar: ")
  verificar(cadena)
  if(nodo_actual in finales):
    print "Cadena aceptada"
    print cinta
  else:
    print "Cadena rechazada"


  s=raw_input("Desea probar otro cadena?(s/n): ")
  if(s!="s" and s!="S"):
    break
