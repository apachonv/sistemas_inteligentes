''' ALEJANDRA PACHÓN VARGAS '''

#%% Dependences
import random
import turtle
import time
from time import sleep
# Crear una pantalla
pantalla = turtle.Screen()
# variable encargada de medir el desempeño en tiempo el iniciar 
start_time = time.time()
#%% Variables
global t1,t2,t3,t4
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()

#%%main
t1.penup()
t1.begin_fill()
t1.setpos(-140,120)
t1.write("Lado A", align="center",font=("Arial",15,"normal"))
t1.end_fill()
t1.penup()

t2.penup()
t2.begin_fill()
t2.setpos(140,120)
t2.write("Lado B", align="center",font=("Arial",15,"normal"))
t2.end_fill()
t2.penup()

t3.penup()
t3.begin_fill()
t3.setpos(-140,-140)
t3.write("Lado C", align="center",font=("Arial",15,"normal"))
t3.end_fill()
t3.penup()

t4.penup()
t4.begin_fill()
t4.setpos(140,-140)
t4.write("Lado D", align="center",font=("Arial",15,"normal"))
t4.end_fill()
t4.penup()

class Ambiente(object):
    def __init__(self, estadoA, estadoB, estadoC, estadoD):
        # Estado limpio: 0   Estado Sucio: 1
        self.localizacion={"A":estadoA,"B":estadoB, "C":estadoC,"D":estadoD}
        print('\nEstado inicial ',self.localizacion)

        # crear las habitaciones que va a limpiar la aspiradora 
        self.A=turtle.Turtle()
        self.A.penup()
        self.A.setpos(-120,60)
        self.A.begin_fill()
        self.A.shape("square")
        self.A.turtlesize(5)
        if self.localizacion["A"]==0:
            self.A.color("#82E0AA")
        else:
            self.A.color("#F5CBA7")
        self.A.end_fill()
        self.A.penup()

        self.B=turtle.Turtle()
        self.B.penup()
        self.B.setpos(120,60)
        self.B.begin_fill()
        self.B.shape("square")
        self.B.turtlesize(5)
        if self.localizacion["B"]==0:
            self.B.color("#82E0AA")
        else:
            self.B.color("#F5CBA7")
        self.B.end_fill()
        self.B.penup()

        self.C=turtle.Turtle()
        self.C.penup()
        self.C.setpos(-120,-60)
        self.C.begin_fill()
        self.C.shape("square")
        self.C.turtlesize(5)
        if self.localizacion["C"]==0:
            self.C.color("#82E0AA")
        else:
            self.C.color("#F5CBA7")
        self.C.end_fill()
        self.C.penup()

        self.D=turtle.Turtle()
        self.D.penup()
        self.D.setpos(120,-60)
        self.D.begin_fill()
        self.D.shape("square")
        self.D.turtlesize(5)
        if self.localizacion["D"]==0:
            self.D.color("#82E0AA")
        else:
            self.D.color("#F5CBA7")
        self.D.end_fill()
        self.D.penup()


class IAspirador(Ambiente):
    def __init__(self,Ambiente):
        # Localización del aspirador
        global localizacionAspirador
        #localización de la aspiradora aleatoriamente
        localizacionAspirador=random.choice(["A","B","C","D"])
        #localización de la aspiradora elegida por el usuario
        #localizacionAspirador="D"
        print("\nEl ambiente esta: ",Ambiente.localizacion)
        
        # crear la aspiradora 
        global Asp
        Asp=turtle.Turtle()
        Asp.penup()
        Asp.setpos(0,0)
        Asp.begin_fill()
        Asp.shape("circle")
        Asp.turtlesize(2)
        Asp.color("#FF48A9")
        Asp.end_fill()
        Asp.penup()
        self.contador_pasos = 0

    # función encargada de localizar la aspiradora en alguna habitación todo el tiempo
    def verifica_estado_aspirador(self, Ambiente):
        if localizacionAspirador=="A":
            result1="El aspirador es colocado aleatoriamente en el lado A \n"
            Asp.speed(10)
            Asp.setpos(-120,60)
            return print(result1)
        elif localizacionAspirador=="B":
            result2="El aspirador es colocado aleatoriamente en el lado B \n"
            Asp.speed(10)
            Asp.setpos(120,60)
            return print(result2)
        elif localizacionAspirador=="C":
            result3="El aspirador es colocado aleatoriamente en el lado C \n"
            Asp.speed(10)
            Asp.setpos(-120,-60)
            return print(result3)
        elif localizacionAspirador=="D":
            result4="El aspirador es colocado aleatoriamente en el lado D \n"
            Asp.speed(10)
            Asp.setpos(120,-60)
            return print(result4)
    
    # Función encargada de validar todos los posibles estados 
    # fué una de las funciones más modificadas del código inicial, valida los estados planteados en la Heurística
    def verifica_estado_ambiente(self,Ambiente):
        # Si el lado A estuviese sucio
        if localizacionAspirador=="A":
            if Ambiente.localizacion["A"]==1:
                IAspirador.aspirar(self,Ambiente,"A")
            else:
                print("El lado A ya esta limpio")

            if (Ambiente.localizacion["B"]==1 and Ambiente.localizacion["C"]==1)or(Ambiente.localizacion["B"]==0 and Ambiente.localizacion["C"]==0):
                moverse=random.choice(["B","C"])
                if moverse=="B":
                    if Ambiente.localizacion["B"]==1:
                        IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                        IAspirador.aspirar(self,Ambiente,"B")
                        if Ambiente.localizacion["D"]==1:
                            IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")
                            IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseAbajo(self,Ambiente,"D","limpio")       
                            IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")       
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseDerecha(self,Ambiente,"B","limpio")    
                        if Ambiente.localizacion["D"]==1:
                            IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")       
                            print("El lado C ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado D ya esta limpio")
                            print("El lado C ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                else:
                    if Ambiente.localizacion["C"]==1:
                        IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                        IAspirador.aspirar(self,Ambiente,"C")   
                        if Ambiente.localizacion["D"]==1:
                            IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")       
                            IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")      
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseDerecha(self,Ambiente,"D","limpio")       
                            IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")      
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseAbajo(self,Ambiente,"C","limpio")   
                        if Ambiente.localizacion["D"]==1:
                            IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")      
                            print("El lado B ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado D ya esta limpio")
                            print("El lado B ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
            elif Ambiente.localizacion["B"]==1 and Ambiente.localizacion["C"]==0:
                IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                IAspirador.aspirar(self,Ambiente,"B")
                if Ambiente.localizacion["D"]==1:
                    IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                    IAspirador.aspirar(self,Ambiente,"D")
                    print("El lado C ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado D ya esta limpio")
                    print("El lado C ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
            else:
                IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                IAspirador.aspirar(self,Ambiente,"C")
                if Ambiente.localizacion["D"]==1:
                    IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                    IAspirador.aspirar(self,Ambiente,"D")
                    print("El lado B ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado D ya esta limpio")
                    print("El lado B ya esta limpio")
                    IAspirador.finalizarAspiradora(self)

        if localizacionAspirador=="B":
            if Ambiente.localizacion["B"]==1:
                IAspirador.aspirar(self,Ambiente,"B")
            else:
                print("El lado B ya esta limpio")
            
            if (Ambiente.localizacion["A"]==1 and Ambiente.localizacion["D"]==1)or(Ambiente.localizacion["A"]==0 and Ambiente.localizacion["D"]==0):
                moverse=random.choice(["A","D"])
                if moverse=="D":
                    if Ambiente.localizacion["D"]==1:
                        IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                        IAspirador.aspirar(self,Ambiente,"D")
                        if Ambiente.localizacion["C"]==1:
                            IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")
                            IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseIzquierda(self,Ambiente,"C","limpio")       
                            IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")       
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseAbajo(self,Ambiente,"D","limpio")    
                        if Ambiente.localizacion["C"]==1:
                            IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")       
                            print("El lado A ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado C ya esta limpio")
                            print("El lado A ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                else:
                    if Ambiente.localizacion["A"]==1:
                        IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                        IAspirador.aspirar(self,Ambiente,"A")   
                        if Ambiente.localizacion["C"]==1:
                            IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")       
                            IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")      
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseAbajo(self,Ambiente,"C","limpio")       
                            IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")      
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseIzquierda(self,Ambiente,"A","limpio")   
                        if Ambiente.localizacion["C"]==1:
                            IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")      
                            print("El lado D ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado C ya esta limpio")
                            print("El lado D ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
            elif Ambiente.localizacion["A"]==1 and Ambiente.localizacion["D"]==0:
                IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                IAspirador.aspirar(self,Ambiente,"A")
                if Ambiente.localizacion["C"]==1:
                    IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                    IAspirador.aspirar(self,Ambiente,"C")
                    print("El lado D ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado C ya esta limpio")
                    print("El lado D ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
            else:
                IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                IAspirador.aspirar(self,Ambiente,"D")
                if Ambiente.localizacion["C"]==1:
                    IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                    IAspirador.aspirar(self,Ambiente,"C")
                    print("El lado A ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado C ya esta limpio")
                    print("El lado A ya esta limpio")
                    IAspirador.finalizarAspiradora(self)

        if localizacionAspirador=="C":
            if Ambiente.localizacion["C"]==1:
                IAspirador.aspirar(self,Ambiente,"C")
            else:
                print("El lado C ya esta limpio")

            if (Ambiente.localizacion["A"]==1 and Ambiente.localizacion["D"]==1)or(Ambiente.localizacion["A"]==0 and Ambiente.localizacion["D"]==0):
                moverse=random.choice(["A","D"])
                if moverse=="D":
                    if Ambiente.localizacion["D"]==1:
                        IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                        IAspirador.aspirar(self,Ambiente,"D")
                        if Ambiente.localizacion["B"]==1:
                            IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")
                            IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseArriba(self,Ambiente,"B","limpio")       
                            IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")       
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseDerecha(self,Ambiente,"D","limpio")    
                        if Ambiente.localizacion["B"]==1:
                            IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")       
                            print("El lado A ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado B ya esta limpio")
                            print("El lado A ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                else:
                    if Ambiente.localizacion["A"]==1:
                        IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                        IAspirador.aspirar(self,Ambiente,"A")   
                        if Ambiente.localizacion["B"]==1:
                            IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")       
                            IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")      
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseDerecha(self,Ambiente,"B","limpio")       
                            IAspirador.moverseAbajo(self,Ambiente,"D","sucio")
                            IAspirador.aspirar(self,Ambiente,"D")      
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseArriba(self,Ambiente,"A","limpio")   
                        if Ambiente.localizacion["B"]==1:
                            IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")      
                            print("El lado D ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado B ya esta limpio")
                            print("El lado D ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
            elif Ambiente.localizacion["A"]==1 and Ambiente.localizacion["D"]==0:
                IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                IAspirador.aspirar(self,Ambiente,"A")
                if Ambiente.localizacion["B"]==1:
                    IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                    IAspirador.aspirar(self,Ambiente,"B")
                    print("El lado D ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado B ya esta limpio")
                    print("El lado D ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
            else:
                IAspirador.moverseDerecha(self,Ambiente,"D","sucio")
                IAspirador.aspirar(self,Ambiente,"D")
                if Ambiente.localizacion["B"]==1:
                    IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                    IAspirador.aspirar(self,Ambiente,"B")
                    print("El lado A ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado B ya esta limpio")
                    print("El lado A ya esta limpio")
                    IAspirador.finalizarAspiradora(self)

        if localizacionAspirador=="D":
            if Ambiente.localizacion["D"]==1:
                IAspirador.aspirar(self,Ambiente,"D")
            else:
                print("El lado D ya esta limpio")

            if (Ambiente.localizacion["B"]==1 and Ambiente.localizacion["C"]==1)or(Ambiente.localizacion["B"]==0 and Ambiente.localizacion["C"]==0):
                moverse=random.choice(["B","C"])
                if moverse=="B":
                    if Ambiente.localizacion["B"]==1:
                        IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                        IAspirador.aspirar(self,Ambiente,"B")
                        if Ambiente.localizacion["A"]==1:
                            IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")
                            IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseIzquierda(self,Ambiente,"A","limpio")       
                            IAspirador.moverseAbajo(self,Ambiente,"C","sucio")
                            IAspirador.aspirar(self,Ambiente,"C")       
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseArriba(self,Ambiente,"B","limpio")    
                        if Ambiente.localizacion["A"]==1:
                            IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")       
                            print("El lado C ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado A ya esta limpio")
                            print("El lado C ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                else:
                    if Ambiente.localizacion["C"]==1:
                        IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                        IAspirador.aspirar(self,Ambiente,"C")   
                        if Ambiente.localizacion["A"]==1:
                            IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")       
                            IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")      
                            IAspirador.finalizarAspiradora(self)
                        else:
                            IAspirador.moverseArriba(self,Ambiente,"A","limpio")       
                            IAspirador.moverseDerecha(self,Ambiente,"B","sucio")
                            IAspirador.aspirar(self,Ambiente,"B")      
                            IAspirador.finalizarAspiradora(self)
                    else:
                        IAspirador.moverseIzquierda(self,Ambiente,"C","limpio")   
                        if Ambiente.localizacion["A"]==1:
                            IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                            IAspirador.aspirar(self,Ambiente,"A")      
                            print("El lado B ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
                        else:
                            print("El lado A ya esta limpio")
                            print("El lado B ya esta limpio")
                            IAspirador.finalizarAspiradora(self)
            elif Ambiente.localizacion["B"]==1 and Ambiente.localizacion["C"]==0:
                IAspirador.moverseArriba(self,Ambiente,"B","sucio")
                IAspirador.aspirar(self,Ambiente,"B")
                if Ambiente.localizacion["A"]==1:
                    IAspirador.moverseIzquierda(self,Ambiente,"A","sucio")
                    IAspirador.aspirar(self,Ambiente,"A")
                    print("El lado C ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado A ya esta limpio")
                    print("El lado C ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
            else:
                IAspirador.moverseIzquierda(self,Ambiente,"C","sucio")
                IAspirador.aspirar(self,Ambiente,"C")
                if Ambiente.localizacion["A"]==1:
                    IAspirador.moverseArriba(self,Ambiente,"A","sucio")
                    IAspirador.aspirar(self,Ambiente,"A")
                    print("El lado B ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
                else:
                    print("El lado A ya esta limpio")
                    print("El lado B ya esta limpio")
                    IAspirador.finalizarAspiradora(self)
    
    # Función encargada de aspirar las habitaciones sucias 
    # recibe por parámetro el lado, es decir, la habitación que debe aspirar.
    def aspirar(self,Ambiente,lado):
        self.contador_pasos+=1
        Ambiente.localizacion[lado]=0
        print(f"El lado {lado.strip('')} fue limpiado")
        if lado=="A":
            Ambiente.A.color("#82E0AA")
        elif lado=="B":
            Ambiente.B.color("#82E0AA")
        elif lado=="C":
            Ambiente.C.color("#82E0AA")
        elif lado=="D":
            Ambiente.D.color("#82E0AA")
        sleep(2)
    
    # Funciones encargadas de mover la aspiradora ya sea para la derecha, izquierda, arriba o abajo
    # reciben por parámeto el lado, es decir, la habitación a la cual se debe desplazar la aspiradora
    # y recibe también por parámetro si la habitación está limpia o sucia para arrojar los mensajes
    def moverseDerecha(self,Ambiente,lado,limpio_sucio):
        self.contador_pasos+=1
        if limpio_sucio=="sucio":
            print(f"el lado {lado} está sucio")
        else:
            print(f"el lado {lado} está limpio")
        print(f"Se mueve para el lado {lado}")
        IAspirador.localizacionAspirador=lado
        Asp.speed(1)
        Asp.forward(240)

    def moverseIzquierda(self,Ambient,lado,limpio_sucio):
        self.contador_pasos+=1
        if limpio_sucio=="sucio":
            print(f"el lado {lado} está sucio")
        else:
            print(f"el lado {lado} está limpio")
        print(f"Se mueve para el lado {lado}")
        IAspirador.localizacionAspirador=lado
        Asp.speed(1)
        Asp.backward(240)

    def moverseAbajo(self,Ambiente,lado,limpio_sucio):
        self.contador_pasos+=1
        if limpio_sucio=="sucio":
            print(f"el lado {lado} está sucio")
        else:
            print(f"el lado {lado} está limpio")
        print(f"Se mueve para el lado {lado}")
        IAspirador.localizacionAspirador = lado
        Asp.speed(1)
        Asp.sety(Asp.ycor()-120)

    def moverseArriba(self,Ambiente,lado,limpio_sucio):
        self.contador_pasos+=1
        if limpio_sucio=="sucio":
            print(f"el lado {lado} está sucio")
        else:
            print(f"el lado {lado} está limpio")
        print(f"Se mueve para el lado {lado}")
        IAspirador.localizacionAspirador=lado
        Asp.speed(1)
        Asp.sety(Asp.ycor()+120)

    # Función encargada de finalizar la aspiradora regresándola al centro. 
    def finalizarAspiradora(self):
        Asp.setpos(0,0)
        return print("\nLa aspiradora termino")


# Instancias las clases 
ElAmbiente=Ambiente(0,1,1,0)
ElAspirador=IAspirador(ElAmbiente)
sleep(1)
ElAspirador.verifica_estado_aspirador(ElAmbiente)
sleep(1)
ElAspirador.verifica_estado_ambiente(ElAmbiente)
sleep(1)

print(f"la cantidad de pasos fueron: {ElAspirador.contador_pasos}")
print("\nDespues de la accion del  aspirador, el ambiente esta:  ", ElAmbiente.localizacion)

# variable encargada de medir el desempeño en tiempo al terminar 
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos\n")

turtle.done()