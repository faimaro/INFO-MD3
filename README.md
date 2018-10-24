# info-md3-tp

para ejecutar es necesario tener como minimo python 3.5 

los puntos estan en diferentes archivos.
- en imprimir Tabla, se puede ver como imprime una serie de transiciones en funciones de los estados que se ingrese

- en ejecucion de maquina está lo mejor... allí hay funciones q su nombre describe lo que hacen:
    - crearMaquina() : pide estados y pasos-- genera 10 maquinas y las hace procesar...
    - crearCinta() : crea una lista con 1000 '0'.. nuestra cinta de entrada
    - procesar() : metodo oscuro que procesa una maquina X con la condicion de devolver : 
        - si la maquina se ejecuto en menos pasos de los que pasamos => devuelve esa maquina
        - si llege al FIN o supero esos pasos => devuelvo None
    - enumerarMaquinas() : toma el parametro del tamaño y me crea ALEATOREAMENTE 10  maquinas con estados aleatorios . la unica "inteligencia" que tiene este metodo es que solo coloca 1 FIN.. 


