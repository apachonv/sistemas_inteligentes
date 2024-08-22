import random
import numpy as np

# ESTE ALGORITMO PROCESA DATOS ENTEROS

'''creado por alejandra'''
def pasarAEnteros(poblacionGenotipo):
    for i in range(0, n):
        for j in range(0,x,2):
            poblacionFenotipo[i,int(j/2)]=((poblacionGenotipo[i,j]*2)+(poblacionGenotipo[i,(j+1)]*1))
    return poblacionFenotipo

def calcularFitnessYTotal(n, x, poblacionFenotipo, utilidad):
    suma = 0
    totalFitness = 0
    for i in range(0, n):
        for j in range(0, int(x/2)):  # Corrección aquí
            suma += poblacionFenotipo[i,j] * utilidad[j]
        fitness[i] = suma
        totalFitness += suma
        suma = 0
    return fitness, totalFitness
   
def calcularPesoYFactibilidad(n , x, poblacionFenotipo, pesos):
    suma = 0
    for i in range(0, n):
        for j in range(0, int(x/2)):
            suma += poblacionFenotipo[i,j] * pesos[j]
        pesoFinal[i] = suma
        if pesoFinal[i]<60:
            factibilidad[i]='SI'
        else:
            factibilidad[i]='NO'
        suma = 0
    return pesoFinal, factibilidad

def calcularFitnessMejorIndividuo(n, fitness, factibilidad):
    fitnessMejorIndividuo = fitness[0]
    for i in range(0, n):
        if(fitness[i]>fitnessMejorIndividuo and factibilidad[i]=='SI'):
            fitnessMejorIndividuo = fitness[i]
    return fitnessMejorIndividuo

def calcularLaMedia(n, fitness):
    suma = 0
    for i in range(0, n):
        suma += fitness[i]
    mediaEntreTodosLosIndividuos = suma / n
    return mediaEntreTodosLosIndividuos

def imprimirTabla(n, totalFitness, fitness, pesoFinal, poblacionGenotipo, poblacionFenotipo, factibilidad):
    acumula=0
    print ('\nTabla Iteración:')
    for i in range(0, n):
      probabilidad=fitness[i]/totalFitness
      acumula+=probabilidad
      print([i+1]," ",poblacionGenotipo[i]," ",poblacionFenotipo[i],"  ",fitness[i]," ",pesoFinal[i]," ",factibilidad[i]," ","{0:.3f}".format(probabilidad)," ","{0:.3f}".format(acumula))
      probabilidadAcumulada[i]=acumula
    print("Total Fitness:                           ", totalFitness)
    print("Mejor Individuo:                         ", calcularFitnessMejorIndividuo(n, fitness, factibilidad))
    print("Media entre todos los individuos:        ", calcularLaMedia(n, fitness))
    return probabilidadAcumulada

def seleccion(probabilidadAcumulada, poblacionGenotipo):
    # def seleccion(probabilidadAcumulada, poblacionGenotipo, numero):
    escoje=np.random.rand()
    #escoje=numero
    print("Escoje: ", escoje)
    for i in range(0, n):
      if probabilidadAcumulada[i]>escoje:
         padre = poblacionGenotipo[i]
         break
    return (padre)

def cruce(numeroAleatorio, papa1, papa2, x):
    if numeroAleatorio<Puntocruce:
      print("Mas grande", Puntocruce, "que ", numeroAleatorio, "-> Si Cruzan")
      corte=np.random.randint(1,x)
      #corte = 5
      print('corte:',corte)
      temp1 = papa1[0:corte] #[i:j] corta desde [i a j)
      temp2 = papa1[corte:x]
      print(temp1,temp2)
      temp3 = papa2[0:corte]
      temp4 = papa2[corte:x]
      print(temp3,temp4)
      hijo1 = list(temp1)
      hijo1.extend(list(temp4))
      hijo2 = list(temp3)
      hijo2.extend(list(temp2))
    else:
      print("Menor", Puntocruce, "que ", numeroAleatorio, "-> NO Cruzan")
      hijo1 = papa1
      hijo2 = papa2
    
    return hijo1, hijo2

def mutacion(hijo,x):
    for i in range(x):
        numeroAleatorio = np.random.rand()
        if (numeroAleatorio<0.1):
            if(hijo[i]==0):
                hijo[i]=1
            else:
                hijo[i]=0
    return hijo

def pesoHijo(hijo, pesos, x):
    hijoFenotipo = np.empty((int(x/2))) 
    peso = 0
    for j in range(0, x, 2):
        hijoFenotipo[int(j/2)] = ((hijo[j]*2)+(hijo[(j+1)]*1))
        peso += hijoFenotipo[int(j/2)] * pesos[int(j/2)]
    return peso
 
def calcularMejorIndividuo(n, fitness, poblacionGenotipo, factibilidad):
    fitnessMejorIndividuo = calcularFitnessMejorIndividuo(n, fitness, factibilidad)
    for i in range(0,n):
        if (fitness[i] == fitnessMejorIndividuo):
            mejorIndividuo = poblacionGenotipo[i]
    return mejorIndividuo

#### Parametros - variables globales #####

x = 8  #numero de variables de decision - Elementos diferentes: x
n = 8  #numero de individuos en la poblacion - cromosomas: n
Puntocruce = 0.98  #Probabilidad de Cruce
Puntomutacion = 0.1   #Probabilidad de Mutación
fitness = np.empty((n))
probabilidadAcumulada = np.empty((n))
pesoFinal = np.empty((n))  
probabilidad = np.empty((n))  
totalFitness = 0
factibilidad = np.empty(n, dtype=object)
mejorIndividuo = 0
fitnessMejorIndividuo = 0
mediaEntreTodosLosIndividuos = 0

utilidad = [4, 5, 6, 3] #son los de las funciones, es decir los valores que van a maultiplicar
pesos = [7, 6, 8, 2] #son los de las funciones, es decir los valores que van a maultiplicar

'''poblacion inicial de alejandra'''
cromosoma1 = [0,0,1,1,1,1,0,1]
cromosoma2 = [0,1,0,1,1,0,0,0]
cromosoma3 = [1,1,0,1,0,1,1,1]
cromosoma4 = [1,1,0,1,1,0,0,0]
cromosoma5 = [0,0,0,1,1,1,1,0]
cromosoma6 = [1,1,1,1,0,1,1,1]
cromosoma7 = [1,0,0,0,1,1,0,1]
cromosoma8 = [1,0,0,1,1,1,0,0]

poblacionGenotipo = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4,cromosoma5, cromosoma6, cromosoma7, cromosoma8])
poblacionFenotipo = np.empty((n, int(x/2)))

print("Poblacion inicial en genotipo:","\n", poblacionGenotipo)
print("Poblacion inicial en fenotipo:","\n", pasarAEnteros(poblacionGenotipo))
print("Utilidad:", utilidad) 
print("Pesos", pesos )   

#### FIN DE LOS DATOS INICIALES ###


### Inicio de las Iteraciones ###

#numero de iteraciones, ingresar en el for la cantidad deseada
for i in range(1):
    print("\nIteración : ", i+1)

    #calcular la poblacion fenotipo
    poblacionFenotipo = pasarAEnteros(poblacionGenotipo)

    #calcular el fitness de cada individuo
    fitness, totalFitness = calcularFitnessYTotal(n, x, poblacionFenotipo, utilidad)

    #llama funcion calcularPeso, para calcular el peso de cada individuo
    pesoFinal, factibilidad = calcularPesoYFactibilidad(n, x, poblacionFenotipo, pesos)

    #imprime la tabla de la iteracion
    imprimirTabla(n, totalFitness, fitness, pesoFinal, poblacionGenotipo, poblacionFenotipo, factibilidad)

    hijos = []
    mejorIndividuo = calcularMejorIndividuo(n, pesoFinal, poblacionGenotipo, factibilidad)
    hijos.append(mejorIndividuo)
    contador=1
    while (contador<n):
        print('mejor individuo es: ', mejorIndividuo)
        print('\nSelección:')
        #papa1 = seleccion(probabilidadAcumulada, poblacionGenotipo, 0.118) # Padre 1
        papa1 = seleccion(probabilidadAcumulada, poblacionGenotipo) # Padre 1
        print("padre 1:", papa1)
        #papa2 = seleccion(probabilidadAcumulada, poblacionGenotipo, 0.249) # Padre 2
        papa2 = seleccion(probabilidadAcumulada, poblacionGenotipo) # Padre 2
        print("padre 2:", papa2)

        print('\nCruce:')
        #hijoA,hijoB = cruce(0.035, papa1, papa2, x)
        hijoA,hijoB = cruce(np.random.rand(), papa1, papa2, x)
        print("hijo1: ", hijoA)
        print("hijo2: ", hijoB)

        print('\nMutación:')
        hijo1 = mutacion(hijoA, x)
        hijo2 = mutacion(hijoB, x)
        pesoHijo1 = pesoHijo(hijo1, pesos, x)
        pesoHijo2 = pesoHijo(hijo2, pesos, x)
        print("hijo1 mutado: ", hijo1, " con un peso: ", pesoHijo1)
        print("hijo2 mutado: ", hijo2, " con un peso: ", pesoHijo2)

        if(pesoHijo1<=60 and contador<n):
            hijos.append(hijo1)
            contador+=1
        if(pesoHijo2<=60 and contador<n):
            hijos.append(hijo2)
            contador+=1

    poblacionGenotipo = np.array(hijos)
    print('\nNueva generación: \n',poblacionGenotipo)
