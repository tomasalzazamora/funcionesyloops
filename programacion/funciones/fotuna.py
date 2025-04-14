import random

fortuna_opciones= [
    "no persigas la felicidad, creala",
    "todas las cosas son dificiles antes de que sean faciles",
    "el pajaro madrugador consigue el guasano, pero el segundo raton te lleva al queso",
    "alguien en tu vida necesita una carta de tu padre",
    "no solo pienses. actua",
    "tu corazon se acelerara",
    "la fortuna que buscas esta en otra galleta",
    "ayuda, estoy prisionero en una panaderia china"
]


def fortuna():
    fortuna = random.randit(0, len(fortuna_opciones) - 1)
    print(fortuna_opciones[fortuna])

fortuna()
fortuna()
fortuna()