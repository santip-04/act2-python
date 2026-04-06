######        Funciones del ejercicio 1        ######

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

######        Funciones del ejercicio 10        ######  

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
