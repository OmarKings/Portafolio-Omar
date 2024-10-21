# Código del Perceptrón 

import numpy as np

class Perceptron:
    def __init__(self, tasa_aprendizaje=0.01, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = None
        self.sesgo = None

    def activacion(self, x):
        return 1 if x >= 0 else 0

    def entrenar(self, X, y):
        n_caracteristicas = X.shape[1]
        self.pesos = np.zeros(n_caracteristicas)
        self.sesgo = 0

        for _ in range(self.epocas):
            for idx, x_i in enumerate(X):
                salida_lineal = np.dot(x_i, self.pesos) + self.sesgo
                y_predicho = self.activacion(salida_lineal)

                ajuste = self.tasa_aprendizaje * (y[idx] - y_predicho)
                self.pesos += ajuste * x_i
                self.sesgo += ajuste

    def predecir(self, X):
        salida_lineal = np.dot(X, self.pesos) + self.sesgo
        return np.array([self.activacion(x) for x in salida_lineal])

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # Compuerta AND
modelo = Perceptron(tasa_aprendizaje=0.1, epocas=10)
modelo.entrenar(X, y)
print(modelo.predecir(X))


# Código del algoritmo de Backpropagation 

import numpy as np

class RedNeuronal:
    def __init__(self, tasa_aprendizaje=0.1):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.pesos1 = np.random.rand(2, 2)  # Pesos capa 1
        self.pesos2 = np.random.rand(2, 1)  # Pesos capa 2

    def sigmoide(self, x):
        return 1 / (1 + np.exp(-x))

    def derivada_sigmoide(self, x):
        return x * (1 - x)

    def hacia_adelante(self, X):
        self.capa1 = self.sigmoide(np.dot(X, self.pesos1))
        self.salida = self.sigmoide(np.dot(self.capa1, self.pesos2))
        return self.salida

    def hacia_atras(self, X, y):
        error_salida = y - self.salida
        delta_salida = error_salida * self.derivada_sigmoide(self.salida)

        error_capa1 = delta_salida.dot(self.pesos2.T)
        delta_capa1 = error_capa1 * self.derivada_sigmoide(self.capa1)

        # Actualización de pesos
        self.pesos2 += self.capa1.T.dot(delta_salida) * self.tasa_aprendizaje
        self.pesos1 += X.T.dot(delta_capa1) * self.tasa_aprendizaje

    def entrenar(self, X, y, epocas=1000):
        for _ in range(epocas):
            self.hacia_adelante(X)
            self.hacia_atras(X, y)

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])  # Compuerta XOR
red = RedNeuronal(tasa_aprendizaje=0.1)
red.entrenar(X, y)
print(red.hacia_adelante(X))
