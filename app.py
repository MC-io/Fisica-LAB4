import numpy as np
import math
from matplotlib import pyplot as plt

GRAVEDAD = 9.8

class SistemaEnergiaMecanica:
   def __init__(self, masa, altura):
      self.masa = masa
      self.altura = altura
      self.velocidad_final = (2 * GRAVEDAD * self.altura) ** 0.5
      self.tiempo_final = self.velocidad_final / GRAVEDAD

   def hallar_altura(self, tiempo):
      return (self.altura - self.hallar_distancia_recorrida(tiempo))

   def hallar_distancia_recorrida(self, tiempo):
      return ((tiempo * GRAVEDAD) ** 2) / (2 * GRAVEDAD)
   
   def hallar_velocidad(self, tiempo):
      distancia = self.hallar_distancia_recorrida(tiempo)
      return (2 * GRAVEDAD * distancia) ** (0.5)

   def energia_potencial(self, tiempo):
      altura_ = self.hallar_altura(tiempo)
      return self.masa * GRAVEDAD * altura_
   
   def energia_cinetica(self, tiempo):
      velocidad = self.hallar_velocidad(tiempo)
      return 0.5 * self.masa * (velocidad ** 2)
   
   def energia_mecanica(self, tiempo):
      return self.energia_potencial(tiempo) + self.energia_cinetica(tiempo)
   
   def graficar(self):
      tiempo = np.linspace(0, self.tiempo_final)
      U = self.energia_potencial(tiempo)
      K = self.energia_cinetica(tiempo)
      M = self.energia_mecanica(tiempo)


      plt.plot(tiempo, U, color='blue', label="Energia Potencial")
      plt.plot(tiempo, K, color='green', label="Energia Cinetica")
      plt.plot(tiempo, M, color='red', label="Energia Mecanica")

      plt.xlabel("Segundos (s)")
      plt.ylabel("Joules (J)")

      plt.legend()


      plt.show()
  

if __name__ == "__main__":
   mi_sistema = SistemaEnergiaMecanica(20.0, 100.0)
   print("La energia mecanica conservada en el sistema es de: {} J".format(mi_sistema.energia_mecanica(0)))

   mi_sistema.graficar()

