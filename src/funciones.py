##############        Funciones del ejercicio 1        ##############

def procesar_text (text):
    lineas = text.split("\n")  # Separa en líneas
    cant_lineas = len(lineas)
    total_palabras = 0

    # Calcula la cantidad total de palabras
    for linea in lineas:
        palabras = linea.split()
        total_palabras += len(palabras)

    promedio = total_palabras / cant_lineas    # Promedio de palabras por línea
    lineas_mayores = []    

    # Lineas por encima del promedio
    for linea in lineas:
        palabras = linea.split()
        if len(palabras) > promedio:
            lineas_mayores.append(linea)

    return {
        "lineas": cant_lineas,
        "palabras": total_palabras,
        "promedio": promedio,
        "mayores": lineas_mayores
    }    

##############        Funciones del ejercicio 2         ###############

def procesar_playlist (playlist):
    total_segundos = 0
    max_duracion = 0
    min_duracion = float("inf") # Inicializo en un valor infinito

    cancion_larga = None
    cancion_corta = None

    for song in playlist:
        minutos, segundos = song["duration"].split(":")
        duracion = int(minutos) * 60 + int(segundos)
        total_segundos += duracion   # Suma el total de segundos

        if duracion > max_duracion:    # Canción más larga
            max_duracion = duracion
            cancion_larga = song

        if duracion < min_duracion:    # Canción más corta
            min_duracion = duracion
            cancion_corta = song

    # Convertir total a minutos y segundos
    total_min = total_segundos // 60  
    total_seg = total_segundos % 60

    return {
        "total": (total_min, total_seg),
        "larga": cancion_larga,
        "corta": cancion_corta
    }

##############        Funciones del ejercicio 3         ##############

def limpiar_palabra(palabra):
    return palabra.lower().strip(".,!¿?")

def censurar_palabra(palabra):
    return "*" * len(palabra)

def filtrar_spoilers(review, spoilers_input):
    spoilers = [palabra.strip().lower() for palabra in spoilers_input.split(",")]

    palabras = review.split()
    resultado = []

    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra)

        if palabra_limpia in spoilers:
            resultado.append(censurar_palabra(palabra))
        else:
            resultado.append(palabra)

    return " ".join(resultado)

##############        Funciones del ejercicio 10        ##############  

def calcular_puntaje (scores):
    resultados = {}
    for participante, jueces in scores.items():
        total = sum(jueces.values())
        resultados[participante] = total
    return resultados

def inicializar_participantes (nombres):
    data = {}
    for nombre in nombres:
        data[nombre] = {
            "total": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "rondas": []
        }
    return data

def procesar_competencia(rounds):
    nombres = list(rounds[0]['scores'].keys())
    data = inicializar_participantes(nombres)

    for i, ronda in enumerate(rounds, 1):
        print(f"\nRonda {i} - {ronda['theme']}:")

        resultados = calcular_puntaje(ronda['scores'])

        ganador = max(resultados, key=resultados.get)
        print(f"Ganador: {ganador} ({resultados[ganador]} pts)")

        data[ganador]["rondas_ganadas"] += 1

        for nombre, puntaje in resultados.items():
            data[nombre]["total"] += puntaje
            data[nombre]["rondas"].append(puntaje)

            if puntaje > data[nombre]["mejor_ronda"]:
                data[nombre]["mejor_ronda"] = puntaje

        # Imprime tabla parcial
        imprimir_tabla(data)

    return data

def imprimir_tabla(data):
    print("\nTabla de posiciones:")

    ordenados = sorted(data.items(), key=lambda x: x[1]["total"], reverse=True)

    for nombre, stats in ordenados:
        print(f"{nombre}: {stats['total']} pts")

def imprimir_tabla_final(data):
    
    print("\nTabla final:\n")

    ordenados = sorted(data.items(), key=lambda x: x[1]["total"], reverse=True)

    print(f"{'Participante':<12} {'Puntaje':<10} {'Ganadas':<10} {'Mejor':<10} {'Promedio'}")
    print("-" * 55)

    for nombre, stats in ordenados:
        promedio = sum(stats["rondas"]) / len(stats["rondas"])

        print(f"{nombre:<12} {stats['total']:<10} {stats['rondas_ganadas']:<10} {stats['mejor_ronda']:<10} {round(promedio,1)}")
