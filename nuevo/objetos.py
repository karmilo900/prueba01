'''
class carros:
    def __init__(self, marca, modelo,color):
        self.marca= marca
        self.modelo= modelo
        self.color=color


carro1= carros('toyota',2020,'azul')
print(f'Carros 1:{carro1.marca} {carro1.modelo} {carro1.color}')


class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

cantidad=int(input("ingresa la cantidad de nombres que deseas ingresar a la lista"))
lista=[]
numero=0

while numero <= cantidad:
    nombre= input(f"por favor escribe el nombre de la persona: ")
    apellido= input(f"ingresa el apellido de la persona: ")
    edad= input(f"ingresa la edad de la persona: ")
    numero += 1

    lista+=[nombre,apellido,edad]

print(lista)
'''


class operaciones():

    def __init__(self,operandoA,operandoB):
        self.operandoA=operandoA
        self.operandoB=operandoB

    def sumar(self):
        return self.operandoA+self.operandoB
    
    def restar(self):
        return self.operandoA-self.operandoB
    
    def multiplicar(self):
        return self.operandoA*self.operandoB
    
    def dividir(self):
        return self.operandoA/self.operandoB



numero1=int(input('ingresa por favor el primer numero: '))
numero2=int(input('ingresa por favor el segundo numero: '))
numeros=operaciones(numero1,numero2)

operacion=int(input('presiona 1 para sumar tus numeros\nPresiona 2 para restar tus numeros'))



if operacion==1:
    print(numeros.sumar())

elif operacion==2:
    print(numeros.restar())
elif operacion==3:
    print(numeros.multiplicar())
elif operacion==4:
    print(numeros.dividir())

else:
    print('opcion icorrrsta')





    

    

    
    

'''persona1= persona(nombre,apellido,edad)
print(f"el nombre de la persona es: {persona1.nombre}\n el apellido de la persona es: {persona1.apellido} \n su edad es de: {persona1.edad}")
'''