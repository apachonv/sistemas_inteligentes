'''
METODOS DE OPTIMIZACIÓN
 • Exactos: garantiza encontrar el óptimo global
 • Heurísticos o Metaheurísticos: solo permiten aproximarse a los óptimos globales

METAHEURÍSTICOS
 • Son basados en principios generales de Inteligencia Artificial (IA).
 • No garantizan la optimalidad de la solución encontrada
 • Su propósito es encontrar una solución cercana al óptimo en un tiempo razonable. 
'''
'''
ALGORITMOS GENÉTICOS
 - Usan el mecanismo de la selección natural para buscar a través del espacio de decisión, soluciones óptimas.
 - Buenas características se propagan y se mejoran de generación en generación. Malas características desaparecen genéticamente.
 - La técnica intenta que un conjunto inicial diverso converja a una única solución

 Características
 • Soluciones en un espacio limitado de búsqueda, preferiblemente discreto. 
 • La función objetivo (función adaptativa) define el problema de optimización a resolver, debe ser maximizada o minimizada y debe ser
   posible saber si una solución es buena o mala, lo que permite premiar las mejores y castigar las segundas (función de aptitud)
                (Individuo - Genotipo)                 (Fitness)
    Inicio -> Geración población inicial -> Evaluación de la función objetivo -> Criterios de optimización alcanzados ? -> Mejor individuo -> Solución
                                                          |                                        |
                                                          |                                        NO
                                                          |     Generar                            |
                                                          |      Nueva                         Selección
                                                          |    Población                           |
                                                          |                                   Recombinación
                                                          |                                        |
                                                          |___________________________________  Mutación     

 • Cadena o Cromosoma: conjunto de genes que representa una solución
 • Gen: representan a las variables de decisión. Una variable de decisión puede ser representada por un gen o por un grupo de genes. 
 • Individuo: potencial solución
 • Población: conjunto de individuos
 • Fitness: calidad del individuo como solución
 • Selección: Reglas que sirven para elegir a los progenitores de la siguiente generación
 • Cruce: Operador explotador de la calidad
 • Mutación: Operador explorador del espacio
'''
'''
 ej:
    Maximizar -> Z = 4X1^(2)+6(X2+X3)^(1/3)+X4+X5X6
    Probabilidad Cruce -> 0,1
    https://docs.google.com/spreadsheets/d/1K5bZQeSmAp7bMX-wGnduTSQzxy-dXf6_LPp2SypsNIo/edit?gid=0#gid=0
    


'''