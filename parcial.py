import random
import numpy as np
import matplotlib.pyplot as plt


def generarCromosomaIncial(x):
    contador = 1
    cromosomaFenotipo = np.empty((7)) 
    while(contador>0):
        cromosoma = [random.choice([0, 1]) for _ in range(x)]
        cromosomaFenotipo[0] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))
        cromosomaFenotipo[1] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))
        cromosomaFenotipo[2] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))
        cromosomaFenotipo[3] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))
        cromosomaFenotipo[4] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))
        cromosomaFenotipo[5] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))
        cromosomaFenotipo[6] = ((cromosoma[0]*64)+(cromosoma[1]*32)+(cromosoma[2]*16)+(cromosoma[3]*8)+(cromosoma[4]*4)+(cromosoma[5]*2)+(cromosoma[6]*1))

        z=0
        for j in range(0, (len(cromosomaFenotipo))):
            z += ((cromosomaFenotipo[j] * 32) - (2*(cromosomaFenotipo[j])**2))
        pesoCromosomaFenotipo = z
        if (pesoCromosomaFenotipo<=pesoMaximo)and(pesoCromosomaFenotipo>=pesoMinimo):
            return cromosoma
        else:
            contador = 1

def pasarADecimal(poblacionGenotipo):
    for i in range(0, n):
        poblacionFenotipo[i] = round((((poblacionGenotipo[i, 0] * 64) +
                         (poblacionGenotipo[i, 1] * 32) +
                         (poblacionGenotipo[i, 2] * 16) +
                         (poblacionGenotipo[i, 3] * 8) +
                         (poblacionGenotipo[i, 4] * 4) +
                         (poblacionGenotipo[i, 5] * 2) +
                         (poblacionGenotipo[i, 6] * 1))) * 12 / ((2 ** 7) - 1), 1)
    return poblacionFenotipo

def calcularFitnessYTotal(n, poblacionFenotipo):
    totalFitness = 0
    for i in range(0, n):
        fitness[i] = ((32*poblacionFenotipo[i])-(2*(poblacionFenotipo[i]**2)))
        totalFitness += fitness[i]
    return fitness, totalFitness

# si población en la posicion [i] es igual a 78 o 96 quiere decir que tomo el valor de x=3 o x=4
def calcularFactibilidad(n , poblacionFenotipo):
    for i in range(0, n):
        if (poblacionFenotipo[i]==78)or(poblacionFenotipo[i]==96):
            factibilidad[i]='NO'
        else:
            factibilidad[i]='SI'
    return factibilidad

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

def imprimirTabla(n, totalFitness, fitness, poblacionGenotipo, poblacionFenotipo, factibilidad):
    acumula=0
    print ('\nTabla Iteración:')
    print('Población Genotipo ', 'Población Fenotipo ', 'Fitness ',  'Factibilidad ', 'Probabilidad ', 'Probabilidad Acumulada')
    for i in range(0, n):
      probabilidad=fitness[i]/totalFitness
      acumula+=probabilidad
      print([i]," ",poblacionGenotipo[i]," ",poblacionFenotipo[i],"  ",fitness[i],"     ",factibilidad[i],"       ","{0:.3f}".format(probabilidad),"         ","{0:.3f}".format(acumula))
      probabilidadAcumulada[i]=acumula
    print("Total Fitness:                        ", totalFitness)
    print("Mejor Individuo:                      ", calcularFitnessMejorIndividuo(n, fitness, factibilidad))
    print("Media entre todos los individuos:     ", calcularLaMedia(n, fitness))
    return probabilidadAcumulada

def seleccion(probabilidadAcumulada, poblacionGenotipo):
    # def seleccion(probabilidadAcumulada, poblacionGenotipo, numero):
    escoje = np.random.rand()
    print(escoje)
    #escoje=numero
    print("Escoje: ", escoje)
    for i in range(0, n):
      if probabilidadAcumulada[i]>escoje:
         padre = poblacionGenotipo[i]
         break
    return (padre)

def calcularMejorIndividuo(n, fitness, factibilidad):
    mejorFitness = calcularFitnessMejorIndividuo(n, fitness, factibilidad)
    for i in range(0,n):
        if fitness[i]==mejorFitness:
            mejorIndividuo = poblacionGenotipo[i]
    return mejorIndividuo, mejorFitness

def seleccion(probabilidadAcumulada, poblacionGenotipo):
    # def seleccion(probabilidadAcumulada, poblacionGenotipo, numero):
    escoje = np.random.rand()
    print(escoje)
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

def mutacion(hijo, x, Puntomutacion):
    for i in range(x):
        numeroAleatorio = np.random.rand()
        if (numeroAleatorio<Puntomutacion):
            if(hijo[i]==0):
                hijo[i]=1
            else:
                hijo[i]=0
    return hijo

def fitnesHijo(hijo):
    decimal = round(((hijo[0] * 64) +
                         (hijo[1] * 32) +
                         (hijo[2] * 16) +
                         (hijo[3] * 8) +
                         (hijo[4] * 4) +
                         (hijo[5] * 2) +
                         (hijo[6] * 1)))
    fitnessCromosomaFenotipo = ((32*decimal)-(2*(decimal**2)))
    return fitnessCromosomaFenotipo

def soluciónFinal(poblacionGenotipo, fitness):
    maximo = max(fitness)
    posiciones = np.where(fitness == maximo)[0]
    individuoSeleccionado = poblacionGenotipo[posiciones[0]]
    objetos = np.where(individuoSeleccionado == 1)[0]
    print("\nEl individuo seleccionado es:", individuoSeleccionado)
    print("Por lo tanto los objetos a llevar son los: ",posiciones)
    print("Que tiene un beneficio de: ",fitness[posiciones[0]]," y consume : ")

x = 7  #numero de variables de decision - Elementos diferentes: x
n = 7  #numero de individuos en la poblacion - cromosomas: n

Puntocruce = 0.8  #Probabilidad de Cruce
Puntomutacion = 0.1   #Probabilidad de Mutación
fitness = np.empty((n))
probabilidadAcumulada = np.empty((n))
pesoMaximo = 12
pesoMinimo = 0
probabilidad = np.empty((n))  
totalFitness = 0
factibilidad = np.empty(n, dtype=object)
mejorIndividuo = 0
fitnessMejorIndividuo = 0
mediaEntreTodosLosIndividuos = 0

mejorIndividuoPorIteracion = []
mediaPorIteracion = []

cromosoma1 = generarCromosomaIncial(x)
cromosoma2 = generarCromosomaIncial(x)
cromosoma3 = generarCromosomaIncial(x)
cromosoma4 = generarCromosomaIncial(x)
cromosoma5 = generarCromosomaIncial(x)
cromosoma6 = generarCromosomaIncial(x)
cromosoma7 = generarCromosomaIncial(x)

poblacionGenotipo = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4, cromosoma5 , cromosoma6, cromosoma7])
poblacionFenotipo = np.empty((n, 1))

print("Poblacion inicial en genotipo:","\n", poblacionGenotipo)
print("Poblacion inicial en fenotipo:","\n", pasarADecimal(poblacionGenotipo))

for i in range(100):
    print("\nIteración : ", i+1)
    #calcular la poblacion fenotipo
    poblacionFenotipo = pasarADecimal(poblacionGenotipo)
    #calcular el fitness de cada individuo
    fitness, totalFitness = calcularFitnessYTotal(n, poblacionFenotipo)
    #llama funcion calcularPeso, para calcular el peso de cada individuo
    factibilidad = calcularFactibilidad(n, poblacionFenotipo)
    #imprimir tabla
    imprimirTabla(n, totalFitness, fitness, poblacionGenotipo, poblacionFenotipo, factibilidad)
    
    hijos = np.empty((n, x))
    mejorIndividuo, fitnessDelMejorIndividuo = calcularMejorIndividuo(n, fitness, factibilidad)
    hijos[0] = mejorIndividuo

    mejorIndividuoPorIteracion.append(fitnessDelMejorIndividuo)
    media = calcularLaMedia(n, fitness)
    mediaPorIteracion.append(media)

    contador=1

    while (contador<n):
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
        hijo1 = mutacion(hijoA, x, Puntomutacion)
        hijo2 = mutacion(hijoB, x, Puntomutacion)
        fitnesHijo1 = fitnesHijo(hijo1)
        fitnesHijo2 = fitnesHijo(hijo2)
        print("hijo1 mutado: ", hijo1, " con un fitnes: ", fitnesHijo1)
        print("hijo2 mutado: ", hijo2, " con un fitnes: ", fitnesHijo2)

        if((fitnesHijo1!=78 or fitnesHijo1!=96) and contador<n):
            hijos[contador] = hijo1
            contador+=1
        if((fitnesHijo2!=78 or fitnesHijo2!=96) and contador<n):
            hijos[contador] = hijo2
            contador+=1

    poblacionGenotipo = np.array(hijos)
    print('\nNueva generación: \n',poblacionGenotipo)


mejorIndividuo, fitnessDelMejorIndividuo = calcularMejorIndividuo(n, fitness, factibilidad)
mejorIndividuoPorIteracion.append(fitnessDelMejorIndividuo)
media = calcularLaMedia(n, fitness)
mediaPorIteracion.append(media)

pasarADecimal(poblacionGenotipo)
fitness, totalFitness = calcularFitnessYTotal(n, poblacionFenotipo)
factibilidad = calcularFactibilidad(n, poblacionFenotipo)
imprimirTabla(n, totalFitness, fitness, poblacionGenotipo, poblacionFenotipo, factibilidad)
soluciónFinal(poblacionGenotipo, fitness)


