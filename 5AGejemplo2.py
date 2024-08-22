import random
import numpy as np

# Problema de la mochila
# Objeto1 -> utilidad=4 y peso=7
# Objeto2 -> utilidad=5 y peso=6
# Objeto3 -> utilidad=6 y peso=8
# Objeto4 -> utilidad=3 y peso=2

# Z=(4*X1)+(5*X2)+(6*X3)+(3*X4)
# RESTRICCIÓN -> (7*X1)+(6*X2)+(8*X3)+(2*X4)<=15
# https://docs.google.com/spreadsheets/d/1gVMwvzvU1HZwD1VS_HIlfVl3fy6YwQpIKa1zZRdFYjI/edit?gid=0#gid=0

def evalua(n,x,poblIt,utilidad):
    suma=0
    total=0
    for i in range(0, n):
      for j in range(0,x):
        suma+=poblIt[i,j]*utilidad[j]
      fitness[i]=suma
      total+=suma
      suma=0
    return fitness,total

'''creado por alejandra'''
def calcularPeso(n,x,poblIt,pesos):
    suma=0
    for i in range(0, n):
        for j in range(0,x):
            suma+=poblIt[i,j]*pesos[j]
        pesoF[i]=suma
        suma=0
    return pesoF
   
'''modificado por alejandra, con el nuevo parámetro pesoF y el print'''
def imprime(n,total,fitness,pesoF,poblIt):
    #Tabla de evaluación de la Población
    acumula=0
    print ('\nTabla Iteración:')
    for i in range(0, n):
      probab=fitness[i]/total
      acumula+=probab
      print([i+1]," ",poblIt[i],"  ",fitness[i]," ",pesoF[i]," ","{0:.3f}".format(probab)," ","{0:.3f}".format(acumula))
      acumulado[i]=acumula
    print("Total Fitness:      ", total)
    return acumulado

'''modificado por alejandra, el nuevo parámetro'''
# def seleccion(acumulado, numero):
def seleccion(acumulado):
    escoje=np.random.rand()
    #escoje=numero
    print("escoje:      ", escoje)
    for i in range(0,n):
      if acumulado[i]>escoje:
         padre=poblIt[i]
         break
    return (padre)

'''Modificado por alejandra, se agrega un parámetro X que se encarga de definir la longitud del corte'''
def cruce(a1,p1,p2,x):
    if a1<Pcruce:
      print("Mas grande", Pcruce, "que ", a1, "-> Si Cruzan")
       
      corte=np.random.randint(1,x)
      #corte = 1
      print('corte:',corte)
      temp1=p1[0:corte] #[i:j] corta desde [i a j)
      temp2=p1[corte:x]
      print(temp1,temp2)
      temp3=p2[0:corte]
      temp4=p2[corte:x]
      print(temp3,temp4)
      hijo1 = list(temp1)
      hijo1.extend(list(temp4))
      hijo2 = list(temp3)
      hijo2.extend(list(temp2))
      print("Cruce:")
    else:
      print("Menor", Pcruce, "que ", a1, "-> NO Cruzan")
      hijo1=p1
      hijo2=p2
    
    return hijo1,hijo2

'''creado por alejandra'''    
def mutacion(hijo,x):
    for i in range(x):
        num = np.random.rand()
        if (num<0.1):
            if(hijo[i]==0):
                hijo[i]=1
            else:
                hijo[i]=0
    return hijo

'''creado por alejandra'''
def pesoHijo(hijo,x):
    suma=0
    for i in range(x):
        suma+=hijo[i]*pesos[i]
    return suma

'''creado por alejandra'''
def soluciónFinal(poblIt, pesosFinales, utilidad):
    maximo = max(pesosFinales)
    posiciones = np.where(pesosFinales == maximo)[0]
    individuoSeleccionado = poblIt[posiciones[0]]
    objetos = np.where(individuoSeleccionado == 1)[0]
    print("El individuo seleccionado es:", individuoSeleccionado)
    print("Por lo tanto los objetos a llevar son los: ",objetos)
    print("Que tiene una utilidad de: ",utilidad[posiciones[0]]," y un peso de: ",pesosFinales[posiciones[0]])

    
#### Parametros - variables globales #####

x=4  #numero de variables de decision - Elementos diferentes: x
n=4  #numero de individuos en la poblacion - cromosomas: n
Pcruce=0.98  #Probabilidad de Cruce
Pmuta=0.1   #Probabilidad de Mutación

fitness= np.empty((n))
acumulado= np.empty((n))
suma=0
total=0

'''creado por alejandra'''
pesoF= np.empty((n))  
probabilidad = np.empty((n))  

'''poblacion inicial de alejandra'''
cromosoma1 = [1, 1, 0, 0]
cromosoma2 = [1, 1, 0, 1]
cromosoma3 = [0, 0, 0, 0]
cromosoma4 = [1, 0, 0, 1]
poblInicial = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4])
pesos = [7, 6, 8, 2] #son los de las funciones, es decir los valores que van a maultiplicar
utilidad = [4, 5, 6, 3] #son los de las funciones, es decir los valores que van a maultiplicar

print("Poblacion inicial:","\n", poblInicial)
print("Utilidad:", utilidad) 
print("Pesos", pesos )   
poblIt=poblInicial

#### FIN DE LOS DATOS INICIALES ###


### Inicio de las Iteraciones ###

'''Creado por alejandra, ciclo for y aglomerar los llamados de las funciones en él'''
#numero de iteraciones, ingresar en el for la cantidad deseada
for i in range(10):
    print("\nIteración : ", i+1)

    #Llama función evalua, para calcular el fitness de cada individuo
    fitness,total=evalua(n,x,poblIt,utilidad)

    #llama funcion calcularPeso, para calcular el peso de cada individuo
    '''creado por alejandra'''
    pesoF = calcularPeso(n,x,poblIt,pesos)

    #imprime la tabla de la iteracion
    imprime(n,total,fitness,pesoF,poblIt)

    hijos = []
    contador=0
    iter = 1
    while (contador<n):
        print("\nIteración: ", iter)

        #papa1=seleccion(acumulado,0.96036) # Padre 1
        papa1=seleccion(acumulado) # Padre 1
        print("padre 1:", papa1)
        #papa2=seleccion(acumulado,0.65842) # Padre 2
        papa2=seleccion(acumulado) # Padre 2
        print("padre 2:", papa2)

        #hijoA,hijoB=cruce(0.52676,papa1,papa2,x)
        hijoA,hijoB=cruce(np.random.rand(),papa1,papa2,x)
        print("hijo1: ", hijoA)
        print("hijo2: ", hijoB)

        hijo1=mutacion(hijoA,x)
        hijo2=mutacion(hijoB,x)
        pesoHijo1=pesoHijo(hijo1,x)
        pesoHijo2=pesoHijo(hijo2,x)
        print("Mutación:")
        print("hijo1 mutado: ", hijo1," con un peso: ",pesoHijo1)
        print("hijo2 mutado: ", hijo2," con un peso: ",pesoHijo2)

        if(pesoHijo1<=15 and contador<n):
            hijos.append(hijo1)
            contador+=1
        if(pesoHijo2<=15 and contador<n):
            hijos.append(hijo2)
            contador+=1

        iter+=1

    poblIt = np.array(hijos)
    print('\nNueva generación: \n',poblIt)

fitness,total=evalua(n,x,poblIt,utilidad)
pesoF = calcularPeso(n,x,poblIt,pesos)
soluciónFinal(poblIt,pesoF,fitness)
