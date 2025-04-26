# Definir la secuencia de referencia
referencia = "ATGCTAGCTAAT"

# Función para detectar mutaciones
def detectar_mutaciones(ref, muestra):
    mutaciones = []
    for i, (r, m) in enumerate(zip(ref, muestra)):
        if r != m:
            mutaciones.append(i)
    return mutaciones

# Leer las secuencias desde el archivo
ruta_archivo = "datos_sensor.txt"  # Cambia aquí si usas el archivo de 20 secuencias

with open(ruta_archivo, "r") as archivo:
    secuencias_sensor = archivo.read().splitlines()

# Inicializar variables para guardar la secuencia con más mutaciones
max_mutaciones = -1
indice_max = -1

# Comparar cada secuencia con la referencia
for idx, secuencia in enumerate(secuencias_sensor):
    mutaciones = detectar_mutaciones(referencia, secuencia)
    print(f"Secuencia {idx + 1}: {secuencia}")
    if mutaciones:
        print(f"  → Mutaciones detectadas en posiciones: {mutaciones}")
    else:
        print("  → No se detectaron mutaciones.")
    
    # Verificar si esta secuencia tiene más mutaciones que las anteriores
    if len(mutaciones) > max_mutaciones:
        max_mutaciones = len(mutaciones)
        indice_max = idx + 1  # +1 para que sea humano (empezando desde 1)

# Mostrar la secuencia que tuvo más mutaciones
print("\n🔎 La secuencia con más mutaciones fue la línea {} con {} mutaciones.".format(indice_max, max_mutaciones))
