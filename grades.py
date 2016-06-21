print "Grades"
candela = {
    "name": "Candela",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "test": [88.0, 40.0, 94.0],
    "exam": [75.0, 90.0]
}
milagros = {
    "name": "Milagros",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "test": [82.0, 83.0, 91.0],
    "exam": [89.0, 97.0]
}
ramiro = {
    "name": "Ramiro",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "test": [0.0, 75.0, 78.0],
    "exam": [100.0, 100.0]
}

def promedio(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total
    
def sacar_promedio(pupil):
    homework = promedio(pupil["homework"])
    test = promedio(pupil["test"])
    exam = promedio(pupil["exam"])
    return 0.1 * homework + 0.3 * test + 0.6 * exam

def calificaciones_con_letras(result):
    if result >= 90:
        return "A"
    elif result >= 80:
        return "B"
    elif result >= 70:
        return "C"
    elif result >= 60:
        return "D"
    else:
        return "F"


print calificaciones_con_letras(sacar_promedio(candela))
    