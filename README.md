# TRABAJO PRÁCTICO MD3

-para ejecutar es necesario tener como minimo python 3.5 
-instalar tabulate...

El probrama lo que hace es lo siguiente: 

Pide cantidad X de maquinas aleatorias, cantidad de estados de esas maquinas y cantidad de pasos a prosesar.

Genera/Enumera las X maquinas, teniendo en cuenta que:

         a- no empiece con bucle infinito 
         b- además que no pueda ir a izq la 1° instrucc.
         c- solo coloca 1 vez el estado FIN

Luego de generar/enumerar estas maquinas con sus tablas de transiciones, las manda a procesar.

en este punto pregunto que TAN interesantes quiero las maquinas? es decir doy 3 opciones : 

         1- Muy interesante : devuelve maquinas que se ejecutan en un rango de entre el 90% y el 100% de la cantidad de pasos
         2- Maso: devuelve maquinas que se ejecutan en un rango de entre el 60% y el 100% de la cantidad de pasos
         3- Poco: devuelve maquinas que se ejecutan en un rango de entre el 30% y el 100% de la cantidad de pasos (muy poco interesantes...)
         
Bajo estas condiciones procesa las maquinas y luego informa 2 cosas: 

        -Cantidad de maquinas interesantes  
        -Imprime dichas maquinas
        -Imprime los pasos de cada una
        -Imprime la maxima cantidad de pasos de esas interesantes

Para procesar cada maquina se usa como condicion de corte 2 cosas: 

        a) si encuentra FIN . 
        b) si la cantidad de pasos supera a la que ingresó el usuario.


