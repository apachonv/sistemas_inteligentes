#%% Dependences
import random
import turtle
from time import sleep

#%% Variables
global t1,t2,t3,t4
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()

#%%main
t1.penup()
t1.begin_fill()
t1.setpos(-140,60)
t1.write("Lado A", align="center",font=("Arial",15,"normal"))
t1.end_fill()
t1.penup()

t2.penup()
t2.begin_fill()
t2.setpos(140,60)
t2.write("Lado B", align="center",font=("Arial",15,"normal"))
t2.end_fill()
t2.penup()

class Ambiente(object):
    def __init__(self, estadoA, estadoB):
        # Estado limpio: 0   Estado Sucio: 1
        self.localizacion={"A":None,"B":None}
        self.localizacion["A"]=estadoA 
        self.localizacion["B"]=estadoB 
        print(40*"---")
        print('estado inicial ',self.localizacion)

        self.A=turtle.Turtle()
        self.A.penup()
        self.A.setpos(-120,0)
        self.A.begin_fill()
        self.A.shape("square")
        self.A.turtlesize(5)
        if self.localizacion["A"]==0:
            self.A.color("green")
        else:
            self.A.color("gray")
        self.A.end_fill()
        self.A.penup()

        self.B=turtle.Turtle()
        self.B.penup()
        self.B.setpos(120,0)
        self.B.begin_fill()
        self.B.shape("square")
        self.B.turtlesize(5)
        if self.localizacion["B"]==0:
            self.B.color("green")
        else:
            self.B.color("gray")
        self.B.end_fill()
        self.B.penup()


class IAspirador(Ambiente):
    def __init__(self,Ambiente):
        # Localización del aspirador, si el salon es A o B
        global localizacionAspirador

        localizacionAspirador=random.choice(["A","B"])
        print(40*"*")
        print("El ambiente esta: ",Ambiente.localizacion)
        
        global Asp
        Asp=turtle.Turtle()
        Asp.penup()
        Asp.setpos(0,0)
        Asp.begin_fill()
        Asp.shape("circle")
        Asp.color("red")
        Asp.end_fill()
        Asp.penup()

        self.contador_pasos = 0


    def verifica_estado_aspirador(self, Ambiente):
        if localizacionAspirador=="A":
            result1="El aspirador es colocado aleatoriamente en el local A \n"
            Asp.speed(10)
            Asp.setpos(-120,0)
            return print(result1)
        elif localizacionAspirador=="B":
            result2="El aspirador es colocado aleatoriamente en el local B \n"
            Asp.speed(10)
            Asp.setpos(120,0)
            return print(result2)
    
    def verifica_estado_ambiente(self,Ambiente):
        # Si el lado A estuviese sucio
        if Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==0:
            if localizacionAspirador=="B":
                print("El lado B ya esta limpio")
                IAspirador.moverse(self,Ambiente)
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                sleep(2)
                IAspirador.finalizarAspiradora(self)
            else:
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                print("El lado B ya esta limpio")
                sleep(2)
                IAspirador.finalizarAspiradora(self)
        elif Ambiente.localizacion["A"]==0 and Ambiente.localizacion["B"]==1:
            if localizacionAspirador=="A":
                print("El lado A ya esta limpio")
                IAspirador.moverse(self,Ambiente)
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                sleep(2)
                IAspirador.finalizarAspiradora(self)
            else:
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                print("El lado A ya esta limpio")
                sleep(2)
                IAspirador.finalizarAspiradora(self)
        elif Ambiente.localizacion["A"]==1 and Ambiente.localizacion["B"]==1:
            if localizacionAspirador=="A":
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                IAspirador.moverse(self,Ambiente)
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                sleep(2)
                IAspirador.finalizarAspiradora(self)
            else:
                print("El lado B esta sucio...")
                IAspirador.aspiraB(self,Ambiente)
                IAspirador.moverse(self, Ambiente)
                print("El lado A esta sucio...")
                IAspirador.aspiraA(self,Ambiente)
                sleep(2)
                IAspirador.finalizarAspiradora(self)
        else:
            if localizacionAspirador=="A":
                print("El lado A ya esta limpio")
                print("El lado B ya esta limpio...")
                sleep(2)
                IAspirador.finalizarAspiradora(self)
            else:
                print("El lado B ya esta limpio.")
                print("El lado A ya esta limpio")
                sleep(2)
                IAspirador.finalizarAspiradora(self)
            print("\n --- Los dos lados estan limpios ---")
    
    def aspiraA(self, Ambiente):
        self.contador_pasos += 1
        Ambiente.A.color("green")
        Ambiente.localizacion["A"]=0
        print("El lado A fue limpiado")
    
    def aspiraB(self,Ambiente):
        self.contador_pasos += 1
        Ambiente.B.color("green")
        Ambiente.localizacion["B"]=0
        print("El lado B fue limpiado")

    def moverse(self,Ambiente):
        self.contador_pasos += 1
        if localizacionAspirador=="A":
            print("\nSe mueve para el lado B")
            IAspirador.localizacionAspirador="B"
            sleep(2.25)
            Asp.forward(240)
        else:
            print("\nSe mueve para el lado A")
            IAspirador.localizacionAspirador="A"
            sleep(2.25)
            Asp.back(240)

    def finalizarAspiradora(self):
        Asp=turtle.Turtle()
        Asp.penup()
        Asp.setpos(0,0)
        Asp.begin_fill()
        Asp.shape("circle")
        Asp.color("red")
        Asp.end_fill()
        Asp.penup()
        return print("La aspiradora termino")



#####   LIMPIAR
ElAmbiente=Ambiente(1,1)
ElAspirador=IAspirador(ElAmbiente)
sleep(1)
ElAspirador.verifica_estado_aspirador(ElAmbiente)
sleep(1)
ElAspirador.verifica_estado_ambiente(ElAmbiente)
sleep(1)
#ElAspirador.finalizarAspiradora()
print(f"la cantidad de pasos fueron: {ElAspirador.contador_pasos}")


#### Al terminar muestra los dos lados limpios
print("\nDespues de la accion del  aspirador, el ambiente esta:  ", ElAmbiente.localizacion)
turtle.done()
#quit()