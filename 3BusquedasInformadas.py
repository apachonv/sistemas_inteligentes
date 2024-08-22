'''
TECNICAS DE RESOLUCIÓN DE PROBLEMAS 
- generate and test (generador y evaluador)

- means-ends analysis (aplica operación y calcula heurística)
    Busca calcular la diferencia entre el nuevo estado y el destino, mediante una heurística.
    Despues de haber generado múltiples estados posibles se elige el camino que minimiza la distancia entre estado actual y el destino. 

- problem reduction (identificar estado intermedio)
'''
'''
BUSQUEDAS INFORMADAS
 HEURÍSTICAS 
 La busqueda heurística dispone de alguna información que permita conocer que tan próximo puede estar un estado objetivo y sobre cuales caminos son mas prometedores.
 Función de evaluación heurística: h(n)

 BUSQUEDA POR PRIMERO EL MEJOR:
 • Utilizar una función de evaluación de cada nodo f(n) que
   estima que tan “prometedor” es el nodo.
 • Analizar preferentemente los nodos o estados con heurística
   más baja.
 • También llamada búsqueda voraz o codiciosa (del inglés
   “greedy”), porque siempre elige expandir lo que estima que
   está más “cerca” del objetivo.

 ej:Problema 8-puzle
    Un tablero cuadrado (3x3) en el que hay situadas 8 fichas cuadradas numeradas, dejando un hueco. El
    juego busca ir desde un estado inicial hasta una posición final mediante el deslizamiento de los bloques
    
    |2|8|3|              |1|2|3|
    |1|6|4|              |8| |4|
    |7| |5|              |7|6|5|
    Estado inicial       Estado final

    Heurísitca 1: numero de piezas descolocadas de su posicion en el estado final
        Estado inicial -> H=4
        Estado final -> H=0

    Heurística 2: suma de las distancias manhattan de cada pieza a donde debería estar en el estado final
        Estado inicial -> H=1+1+0+0+0+1+0+2=5
        Estado final -> H=0+0+0+0+0+0+0+0=0

 BUSQUEDA A*:
 - Objetivos de la búsqueda A*:
    Conseguir buenas soluciones (óptimas).
    Ganar en eficiencia (reduciendo el árbol de búsqueda).
 - f(n) = g(n) + h(n)
    • g(n): costo del camino hasta n
    • h(n): heurística del nodo, estimación del costo de un camino desde n hasta un estado final.
    • f(n): estimación del coste total de una solución óptima que pasa por n

 ej:Problema 8-puzle
    Un tablero cuadrado (3x3) en el que hay situadas 8 fichas cuadradas numeradas, dejando un hueco. El
    juego busca ir desde un estado inicial hasta una posición final mediante el deslizamiento de los bloques
    
    |1|2|3|              |1|2|3|
    |6|4| |              |8| |4|
    |8|7|5|              |7|6|5|
    Estado inicial       Estado final
    
    Heurísitca 1: numero de piezas descolocadas de su posicion en el estado final
                         |1|2|3|             
                         |6|4| |  F*=0+4=4           
                         |8|7|5|
       _____________________|_____________________  
       |                    |                    |
    |1|2| |              |1|2|3|              |1|2|3|
    |6|4|3|  F*=1+5=6    |6| |4|  F*=1+3=4    |6|4|5|  F*=1+5=6   
    |8|7|5|              |8|7|5|              |8|7| |
       _____________________|_____________________ 
       |                    |                    |                       
    |1| |3|              |1|2|3|              |1|2|3|
    |6|2|4|  F*=2+4=6    | |6|4|  F*=2+3=5    |6|7|4|  F*=2+3=5   
    |8|7|5|              |8|7|5|              |8| |5|
                            |                    |
                            |                    |
    ...                                 
    
    Heurística 2: suma de las distancias manhattan de cada pieza a donde debería estar en el estado final
                         |1|2|3|             
                         |6|4| |  F*=0+(0+0+0+1+0+2+1+1)=5           
                         |8|7|5|
       _____________________|_____________________  
       |                    |                    |
    |1|2| |              |1|2|3|              |1|2|3|
    |6|4|3|  F*=1+6=7    |6| |4|  F*=1+4=5    |6|4|5|  F*=1+6=7   
    |8|7|5|              |8|7|5|              |8|7| |
       _____________________|_____________________ 
       |                    |                    |                       
    |1| |3|              |1|2|3|              |1|2|3|
    |6|2|4|  F*=2+5=7    | |6|4|  F*=2+3=5    |6|7|4|  F*=2+5=7   
    |8|7|5|              |8|7|5|              |8| |5|
                            |                    
                            |                    
    ... 
'''
'''
¿CUAL ES EL MEJOR MÉTODO?
- profundidad es bueno cuando se sabe (con seguridad) que el árbol no es muy profundo.
- anchura es bueno cuando el factor de ramificación no es muy grande.
- los métodos heurísticos son adecuados cuando existe una medida natural de la distancia entre casa estado y estado meta.
'''