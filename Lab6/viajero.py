from random import random
from random import randint
import numpy 
#es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos

# clase ciudad 
class ciudad():
    def __init__(self, cantidad):
        self.cantidad = cantidad


    def generarDistancias(self):
      NumCantidad = self.cantidad
      # zeros Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos ceros.
      ciudad = numpy.zeros((NumCantidad,NumCantidad))
      #self.ciudades = ciudad
      for i in range(0,NumCantidad):
        for j in range(0,NumCantidad):
          if(i==j):
            #Si los índices son iguales, establezca la distancia en 0
            #Entre la ciudad ej: la ciudad 1 está a 0 de la ciudad 1
            ciudad[i][j] = 0
          else:
            #Genera un valor entero aleatorio mayor que 0 para distancia entre ciudades
            valor = round(random() * 100)+1
            #Asigna el valor al índice
            ciudad[i][j] = valor
            x = j
            y = i
            #Asigna el mismo valor al índice invertido
            ciudad[x][y] = valor
        #Esto asegura que genera una matriz simétrica para no mantener diferentes distancias entre las mismas ciudades
        i += 1 
      self.ciudades = ciudad
      return self.ciudades


# Clase de poblacion 
class Individuos():
  def __init__(self, tamañoPoblacion, cantidad):
    self.tamañoPoblacion = tamañoPoblacion
    self.cantidad = cantidad


  def generaCromosoma(self):
    cromosoma = []
    poblacion = []
    cantidad = self.cantidad
    tamañoPoblacion = self.tamañoPoblacion
    x = 1
    for x in range(tamañoPoblacion):
      #Crear cromosoma con números aleatorios, cromosoma siempre del mismo tamaño que el número de ciudades
      while len(cromosoma) != cantidad:
        #Dibujar números al azar
        r = randint(1, cantidad)
        if r not in cromosoma:
          # Garantiza de que no habrá repetición
          cromosoma.append(r)
      #Reproducir el ciudadano generado en la lista de población
      poblacion.append(cromosoma)
      cromosoma = []
    self.poblacion = poblacion
    return self.poblacion 


  def GenerarFitness(self, poblacion, ciudades):
    fitness = []
    cantidad = self.cantidad
    tamañoPoblacion = self.tamañoPoblacion
    for i in range(tamañoPoblacion):
      #variables temporales
      temp = []
      nota = 0
      x = 0
      y = 0
      temp = poblacion[i]
      #Si está dentro del alcance, contará las distancias y sumará
      for j in range(cantidad-1):
        x = temp[j]
        if(j < cantidad):
          y = temp[j+1]
        else:
          y = -1
        if(y > 0):
          nota += ciudades[x-1][y-1]
      #Graba el Fitness
      fitness.append(nota)
    self.fitness = fitness
    return self.fitness


  def ordenaPoblacion(self, poblacion, ciudades):
    #ordenar la población por fitness
    #Pasar el cromosoma de la población y el fitness para una lista temporal
    temp = []
    if (len(poblacion) == 0):
      poblacion = self.generaCromosoma()
    fitness = self.GenerarFitness(poblacion, ciudades)
    temp = list(zip(fitness, poblacion))
    #Vaya a la lista temporal para ver una nueva lista que ya está ordenada según Fitness
    lista_tupla_ordenada = []
    lista_tupla_ordenada = sorted(temp, reverse=False) #ordenar
    #lista_tupla_ordenada = temp
    self.litsta_ordanada = lista_tupla_ordenada
    return self.litsta_ordanada


  def reproduccion(self, poblacion, ciudades):
    nuevaPoblacion = []
    if (len(poblacion) == 0):
      poblacion = self.generaCromosoma()
    cantidad = self.cantidad
    tamañoPoblacion = self.tamañoPoblacion
    lista_tupla_ordenada = self.ordenaPoblacion(poblacion, ciudades)
    for i in range(0,tamañoPoblacion,2):
      #Distribuye la población con mejor aptitud para generar nuevos hijos
      padre1 = []
      padre2 = []
      hijoCromosoma = []
      hijo1 = []
      hijo2 = []
      padre1 = lista_tupla_ordenada[i][1]
      #condición para la reproducción
      if(i < tamañoPoblacion-1):
        padre2 = lista_tupla_ordenada[i+1][1]
      else:
        padre2 = lista_tupla_ordenada[-1][1]
      for x in range(cantidad):
        #sortea para determinar si heredar del padre1 o del padre2
        if random() < 0.7:
          hijoCromosoma.append("0")
        else:
          hijoCromosoma.append("1")

      #hijo1
      for j in range(cantidad):
        #El error del padre 1
        if hijoCromosoma[j] == "1":
          hijo1.append(padre1[j])
        #El error del padre 2
        else:
          hijo1.append(0)
      for j in range(cantidad):
        z = 0
        #En el caso de heredar del padre2 los cromosomas
        if hijo1[j] == 0:
          while (z != cantidad):
            #Garantiza de no haya repetición de cromosoma
            if padre2[z] not in hijo1:
              #Seguirá ejecutándose hasta que encuentre un cromosoma del padre 2 que aún no está en el hijo 1
              hijo1[j] = padre2[z]
              z = cantidad
            else:
              z = z + 1
      hijo1 = self.mutacion(hijo1)

      #hijo2
      for j in range(cantidad):
        if hijoCromosoma[j] == "1":
          #El error de padre1
          hijo2.append(padre2[j])
        else:
          #El error de padre2
          hijo2.append(0)
      for j in range(cantidad):
        z = 0
        #En el caso de heredar del padre 2 los cromosomas
        if hijo2[j] == 0:
          while (z != cantidad):
            #Garantiza de no repetición cromosómica
            if padre1[z] not in hijo2:
              #Seguirá ejecutándose hasta que encuentre un cromosoma del padre 2 que aún no está en el hijo 2
              hijo2[j] = padre1[z]
              z = cantidad
            else:
              z = z + 1
      hijo2 = self.mutacion(hijo2)

      nuevaPoblacion.append(hijo1)
      nuevaPoblacion.append(hijo2)

    litsta_ordanada = self.ordenaPoblacion(nuevaPoblacion, ciudades)
    self.litsta_ordanada = litsta_ordanada
    return self.litsta_ordanada


  def mutacion(self, hijo):
    penalizar = random()
    cantidad = self.cantidad
    if penalizar < 0.01:
      #Crear un aleatorio para la penalizacion
      indice1 = randint(0, (cantidad-1))
      indice2 = randint(0, (cantidad-1))
      temp = hijo[indice1]
      temp2 = hijo[indice2]
      hijo[indice1] = temp2
      hijo[indice2] = temp
    return hijo


# clase de Algoritimo Genetico 
class AlgoritimoGenetico():
  def __init__(self, tamañoPoblacion, cantidad, generaciones):
    self.tamañoPoblacion = tamañoPoblacion
    self.cantidad = cantidad
    self.generaciones = generaciones
    self.mejores = []


  def resolver(self):
    tamañoPoblacion = self.tamañoPoblacion
    cantidad = self.cantidad
    generaciones = self.generaciones
    lugarCiudad = ciudad(cantidad)
    ciudades = lugarCiudad.generarDistancias()
    individuo = Individuos(tamañoPoblacion, cantidad)
    poblacion = individuo.generaCromosoma()
    retirar = individuo.reproduccion(poblacion, ciudades)
    for i in range(generaciones):
      poblacion = []
      for j in range(tamañoPoblacion):
        poblacion.append(retirar[j][1])
      resultado = individuo.reproduccion(poblacion, ciudades)
      mejor = resultado[0][0]
      self.mejores.append(mejor)
      retirar = resultado
    return resultado

if __name__ == '__main__':
  cantidad = int(input("Ingrese el número de ciudades: "))
  while cantidad < 2:
    print("cantidad invalida!!!")
    cantidad = int(input("Ingrese el número de ciudades: "))


  tamañoPoblacion = int(input("Introduzca el tamaño de la población:  "))
  while tamañoPoblacion < 1:
    print("cantidad invalida!!!")
    tamañoPoblacion = int(input("Introduzca el tamaño de la población: "))


  generaciones = int(input("Ingrese el número de generaciones: "))
  while generaciones < 1:
    print("cantidad invalida!!!")
    generaciones = int(input("Ingrese el número de generaciones: "))


  resultado = AlgoritimoGenetico(tamañoPoblacion, cantidad, generaciones)
  prueba = resultado.resolver()
  i=0;
  for poblacion in prueba:
      i=i+1
      print(i," ",poblacion)
  print("\nEl camino mas corto es: ", prueba[0])