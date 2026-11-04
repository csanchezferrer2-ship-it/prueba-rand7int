import random

# Asumimos que esta función ya existe
def rand5():
    return random.randint(1, 5)

def rand7():
    """
    Genera un número entero aleatorio entre 1 y 7 con distribución uniforme.
    Implementación basada en muestreo de rechazo (rejection sampling) para 
    garantizar que la probabilidad de cada número sea exactamente 1/7 .
    """
    while True:
        # 1. Expandimos el espacio muestral a 25 combinaciones equiprobables (5x5).
        # (rand5() - 1) * 5 genera saltos: 0, 5, 10, 15, 20.
        # Al sumar un segundo rand5() (1-5), cubrimos todos los enteros del 1 al 25 (uniformemente).
        num = (rand5() - 1) * 5 + rand5()
        
        # 2. Tomamos el rango 1-21 porque 21 es el múltiplo de 7 más cercano a 25.
        # De este modo, asignamos exactamente 3 casos (21/7) a cada resultado posible.
        if num <= 21:
            # Devolvemos ahora restos del 0 al 6. Y sumamos 1, para desplazamos ese resultado al rango 1 a 7
            return (num % 7) + 1
            
        # 3. Los valores 22, 23, 24 y 25 se rechazan y fuerzan una nueva iteración (con el bucle while).




# PRUEBA
if __name__ == "__main__":
    # Prueba 1: Generar 10 números sueltos para ver qué sale
    print("Ejemplo de 10 tiradas:")
    resultados_simples = [rand7() for _ in range(10)]
    print(resultados_simples)
    print("-" * 30)

    # Prueba 2: Prueba de estrés (100,000 tiradas) para ver si la probabilidad es del ~14.28% para cada número
    print("Lanzando 100,000 veces para comprobar la distribución uniforme...")
    contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    
    for _ in range(100000):
        resultado = rand7()
        contadores[resultado] += 1
        
    for numero, cantidad in contadores.items():
        porcentaje = (cantidad / 100000) * 100
        print(f"Número {numero}: {porcentaje:.2f}%")