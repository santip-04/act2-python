# Funciones del ejercicio 10

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