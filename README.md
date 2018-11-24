# COLOQUIO MD3

-para ejecutar es necesario tener como minimo python 3.5 
-instalar tabulate...

El programa hace lo siguiente: 

Pide cantidad X de maquinas aleatorias, cantidad de estados de esas maquinas, cantidad de pasos a prosesar y si deseas enumerar maquinas NO borrantes.

Genera/Enumera las X maquinas, teniendo en cuenta que:

         a- no empiece con bucle infinito 
         b- además que no pueda ir a izq la 1° instrucc.
         c- solo coloca 1 vez el estado FIN

Luego de generar/enumerar estas maquinas con sus tablas de transiciones, las manda a procesar.
         
Bajo estas condiciones procesa las maquinas y luego informa 2 cosas: 

        -Cantidad de maquinas interesantes  
        -Imprime dichas maquinas
        -Imprime la cantidad de pasos de cada una
        -Imprime la maxima cantidad de pasos de esas interesantes

Para procesar cada maquina se usa como condicion de corte 2 cosas: 

        a) si encuentra FIN . 
        b) si la cantidad de pasos supera a la que ingresó el usuario.


