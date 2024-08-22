import random
import numpy as np
import matplotlib.pyplot as plt

# FUNCIONES PARA OPERADORES

def generarCromosomaIncial(x):
    contador = 1
    cromosomaFenotipo = np.empty((4)) 
    while(contador>0):
        cromosoma = [random.choice([0, 1]) for _ in range(x)]
        cromosomaFenotipo[0] = cromosoma[0]
        cromosomaFenotipo[1] = ((cromosoma[1]*2)+(cromosoma[2]*1))
        cromosomaFenotipo[2] = ((cromosoma[3]*2)+(cromosoma[4]*1))
        cromosomaFenotipo[3] = cromosoma[5]
        suma = 0
        for j in range(0, (len(cromosomaFenotipo))):
            suma += cromosomaFenotipo[j] * pesos[j]
        pesoCromosomaFenotipo = suma
        if pesoCromosomaFenotipo<=pesoMaximo:
            return cromosoma
        else:
            contador = 1
        
def pasarAEnteros(poblacionGenotipo):
    for i in range(0, n):
        poblacionFenotipo[i,0] = poblacionGenotipo[i,0]
        poblacionFenotipo[i,1] = ((poblacionGenotipo[i,1]*2)+(poblacionGenotipo[i,2]*1))
        poblacionFenotipo[i,2] = ((poblacionGenotipo[i,3]*2)+(poblacionGenotipo[i,4]*1))
        poblacionFenotipo[i,3] = poblacionGenotipo[i,5]
    return poblacionFenotipo

def calcularFitnessYTotal(n, poblacionFenotipo, utilidad):
    suma = 0
    totalFitness = 0
    for i in range(0, n):
        for j in range(0, (len(poblacionFenotipo[0]))):  
            suma += poblacionFenotipo[i,j] * utilidad[j]
        fitness[i] = suma
        totalFitness += suma
        suma = 0
    return fitness, totalFitness
   
def calcularPesoYFactibilidad(n , poblacionFenotipo, pesos, pesoMaximo):
    suma = 0
    for i in range(0, n):
        for j in range(0, (len(poblacionFenotipo[0]))):
            suma += poblacionFenotipo[i,j] * pesos[j]
        pesoFinal[i] = suma
        if pesoFinal[i]<pesoMaximo:
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
    print('Población Genotipo ', 'Población Fenotipo ', 'Fitness ', 'Peso ', 'Factibilidad ', 'Probabilidad ', 'Probabilidad Acumulada')
    for i in range(0, n):
      probabilidad=fitness[i]/totalFitness
      acumula+=probabilidad
      print([i]," ",poblacionGenotipo[i]," ",poblacionFenotipo[i],"  ",fitness[i],"  ",pesoFinal[i],"     ",factibilidad[i],"       ","{0:.3f}".format(probabilidad),"         ","{0:.3f}".format(acumula))
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

def pesoHijo(hijo, pesos):
    hijoFenotipo = np.empty((4))
    contador = 1
    cromosomaFenotipo = np.empty((4)) 
    cromosomaFenotipo[0] = hijo[0]
    cromosomaFenotipo[1] = ((hijo[1]*2)+(hijo[2]*1))
    cromosomaFenotipo[2] = ((hijo[3]*2)+(hijo[4]*1))
    cromosomaFenotipo[3] = hijo[5]
    suma = 0
    for j in range(0, (len(cromosomaFenotipo))):
        suma += cromosomaFenotipo[j] * pesos[j]
    pesoCromosomaFenotipo = suma
    return pesoCromosomaFenotipo
 
def calcularMejorIndividuo(n, fitness, factibilidad, pesoFinal, pesoMaximo):
    mejorFitness = calcularFitnessMejorIndividuo(n, fitness, factibilidad)
    for i in range(0,n):
        if fitness[i]==mejorFitness:
            mejorIndividuo = poblacionGenotipo[i]
    return mejorIndividuo, mejorFitness

def soluciónFinal(poblacionGenotipo, pesoFinal, fitness):
    maximo = max(fitness)
    posiciones = np.where(fitness == maximo)[0]
    individuoSeleccionado = poblacionGenotipo[posiciones[0]]
    objetos = np.where(individuoSeleccionado == 1)[0]
    print("\nEl individuo seleccionado es:", individuoSeleccionado)
    cromosomaFenotipo = np.empty((4)) 
    cromosomaFenotipo[0] = individuoSeleccionado[0]
    cromosomaFenotipo[1] = ((individuoSeleccionado[1]*2)+(individuoSeleccionado[2]*1))
    cromosomaFenotipo[2] = ((individuoSeleccionado[3]*2)+(individuoSeleccionado[4]*1))
    cromosomaFenotipo[3] = individuoSeleccionado[5]
    print("La mejor combinación es: ", cromosomaFenotipo)
    print("Por lo tanto los objetos a llevar son los: ",posiciones)
    print("Que tiene un beneficio de: ",fitness[posiciones[0]]," y consume : ",pesoFinal[posiciones[0]], " recursos")

#### Parametros - variables globales #####

x = 6  #numero de variables de decision - Elementos diferentes: x
n = 6  #numero de individuos en la poblacion - cromosomas: n

Puntocruce = 0.95  #Probabilidad de Cruce
Puntomutacion = 0.2   #Probabilidad de Mutación

fitness = np.empty((n))
probabilidadAcumulada = np.empty((n))
pesoFinal = np.empty((n))  
pesoMaximo = 174
probabilidad = np.empty((n))  
totalFitness = 0
factibilidad = np.empty(n, dtype=object)
mejorIndividuo = 0
fitnessMejorIndividuo = 0
mediaEntreTodosLosIndividuos = 0

mejorIndividuoPorIteracion = []
mediaPorIteracion = []

utilidad = [409, 171, 200, 208] #son los de las funciones, es decir los valores que van a maultiplicar
pesos = [41, 28, 33, 32] #son los de las funciones, es decir los valores que van a maultiplicar

cromosoma1 = generarCromosomaIncial(x)
cromosoma2 = generarCromosomaIncial(x)
cromosoma3 = generarCromosomaIncial(x)
cromosoma4 = generarCromosomaIncial(x)
cromosoma5 = generarCromosomaIncial(x)
cromosoma6 = generarCromosomaIncial(x)

poblacionGenotipo = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4,cromosoma5, cromosoma6])
poblacionFenotipo = np.empty((n, 4))

print("Poblacion inicial en genotipo:","\n", poblacionGenotipo)
print("Poblacion inicial en fenotipo:","\n", pasarAEnteros(poblacionGenotipo))
print("Utilidad:", utilidad) 
print("Pesos", pesos )   

#### FIN DE LOS DATOS INICIALES ###


### Inicio de las Iteraciones ###

#numero de iteraciones, ingresar en el for la cantidad deseada
for i in range(10):
    print("\nIteración : ", i+1)

    #calcular la poblacion fenotipo
    poblacionFenotipo = pasarAEnteros(poblacionGenotipo)

    #calcular el fitness de cada individuo
    fitness, totalFitness = calcularFitnessYTotal(n, poblacionFenotipo, utilidad)

    #llama funcion calcularPeso, para calcular el peso de cada individuo
    pesoFinal, factibilidad = calcularPesoYFactibilidad(n, poblacionFenotipo, pesos, pesoMaximo)

    #imprime la tabla de la iteracion
    imprimirTabla(n, totalFitness, fitness, pesoFinal, poblacionGenotipo, poblacionFenotipo, factibilidad)

    hijos = np.empty((n, x))
    mejorIndividuo, fitnessDelMejorIndividuo = calcularMejorIndividuo(n, fitness, factibilidad, pesoFinal, pesoMaximo)
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
        pesoHijo1 = pesoHijo(hijo1, pesos)
        pesoHijo2 = pesoHijo(hijo2, pesos)
        print("hijo1 mutado: ", hijo1, " con un peso: ", pesoHijo1)
        print("hijo2 mutado: ", hijo2, " con un peso: ", pesoHijo2)

        if(pesoHijo1<=pesoMaximo and contador<n):
            hijos[contador] = hijo1
            contador+=1
        if(pesoHijo2<=pesoMaximo and contador<n):
            hijos[contador] = hijo2
            contador+=1

    poblacionGenotipo = np.array(hijos)
    print('\nNueva generación: \n',poblacionGenotipo)


mejorIndividuo, fitnessDelMejorIndividuo = calcularMejorIndividuo(n, fitness, factibilidad, pesoFinal, pesoMaximo)
mejorIndividuoPorIteracion.append(fitnessDelMejorIndividuo)
media = calcularLaMedia(n, fitness)
mediaPorIteracion.append(media)

pasarAEnteros(poblacionGenotipo)
fitness, totalFitness = calcularFitnessYTotal(n, poblacionFenotipo, utilidad)
pesoFinal, factibilidad = calcularPesoYFactibilidad(n, poblacionFenotipo, pesos, pesoMaximo)
imprimirTabla(n, totalFitness, fitness, pesoFinal, poblacionGenotipo, poblacionFenotipo, factibilidad)
soluciónFinal(poblacionGenotipo, pesoFinal, fitness)

plt.plot(range(1, 12), mejorIndividuoPorIteracion, marker='o', linestyle='-', label='Mejor Individuo')
plt.plot(range(1, 12), mediaPorIteracion, marker='x', linestyle='-', label='Media de Individuos')
plt.xlabel('Iteración')
plt.ylabel('Valor')
plt.title('Comparación entre Mejor Individuo y Media por Iteración')
plt.legend()
plt.grid(True)
plt.show()