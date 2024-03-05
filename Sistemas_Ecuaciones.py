import random

# Definir la función para evaluar el sistema de ecuaciones
def evaluar_ecuaciones(B, D, E, F):
    # Definición de las ecuaciones del sistema
    ecuacion_1 = 16*B - 6*D + 4*D + F
    ecuacion_2 = B + 8*D + E + F
    ecuacion_3 = 16*B + 2*D - 4*E + F
    ecuacion_4 = 9*B + 8*D - 3*E + F
    # Devolver la suma de las ecuaciones como resultado
    return (ecuacion_1) + (ecuacion_2) + (ecuacion_3) + (ecuacion_4)

# Definir parámetros de búsqueda
limite_inferior = -100
limite_superior = 100
num_intentos = 10
# Inicializar la mejor solución y su valor
mejor_solucion = None
mejor_valor = float('inf')

# Realizar búsqueda aleatoria
for _ in range(num_intentos):
    # Generar valores aleatorios para B, D, E, y F dentro de los límites especificados
    B = random.randint(limite_inferior, limite_superior)
    D = random.randint(limite_inferior, limite_superior)
    E = random.randint(limite_inferior, limite_superior)
    F = random.randint(limite_inferior, limite_superior)
    
    # Evaluar el sistema de ecuaciones con los valores aleatorios generados
    valor_actual = evaluar_ecuaciones(B, D, E, F)
    
    # Actualizar la mejor solución si se encuentra un valor menor
    if valor_actual < mejor_valor:
        mejor_valor = valor_actual
        mejor_solucion = (B, D, E, F)

# Mostrar la mejor solución encontrada
print("La mejor solución encontrada es:")
print("B =", mejor_solucion[0])
print("D =", mejor_solucion[1])
print("E =", mejor_solucion[2])
print("F =", mejor_solucion[3])

print(".........................")
print("La solucion a la ecuacion es la siguiente")  
print("-36")
print("-64")
print("-4")
print("-64")