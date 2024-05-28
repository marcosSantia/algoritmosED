""" Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos
episodios. """


from pila import Stack

pila_episode_v = Stack()
pila_episode_vii = Stack()
pila_ambos_episodios = Stack()

pila_episode_v = ["Luke Skywalker", "Darth Vader", "Yoda", "Han Solo"]
pila_episode_vii = ["Rey", "Kylo Ren", "Finn", "Poe Dameron"]


pila_ambos_episodios = pila_episode_v + pila_episode_vii
print("Contenido de pila_ambos_episodios:")
print(pila_ambos_episodios)


""" En Python dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G. """


pila_personajes = Stack()
personajes = [
    ("Iron Man", 10),
    ("Captain America", 9),
    ("Black Widow", 7),
    ("Thor", 8),
    ("Hulk", 6),
    ("Hawkeye", 5),
    ("Rocket Raccoon", 5),
    ("Groot", 4),
    ("Doctor Strange", 3),
    ("Spider-Man", 5),
    ("Star-Lord", 4),
    ("Gamora", 4),
    ("Drax", 4),
    ("Mantis", 3),
    ("Nebula", 4),
    ("Ant-Man", 4),
    ("Wasp", 2),
]

def ver_items(self):
        return self.items[:]

for personaje in personajes:
    pila_personajes.push(personaje)
    

def posicion_personaje(pila, nombre_personaje):
    items = pila.ver_items()
    for i, (nombre, _) in enumerate(reversed(items), 1):
        if nombre == nombre_personaje:
            return i
    return -1  # Si no se encuentra


def personajes_mas_de_5_peliculas(pila):
    items = pila.ver_items()
    resultado = [(nombre, cantidad) for nombre, cantidad in items if cantidad > 5]
    return resultado

def cantidad_peliculas_personaje(pila, nombre_personaje):
    items = pila.ver_items()
    for nombre, cantidad in items:
        if nombre == nombre_personaje:
            return cantidad
    return 0  # Si no se encuentra

def personajes_con_iniciales(pila, iniciales):
    items = pila.ver_items()
    resultado = [nombre for nombre, _ in items if nombre[0] in iniciales]
    return resultado

# a. Posición de Rocket Raccoon y Groot
posicion_rocket = posicion_personaje(pila_personajes, "Rocket Raccoon")
posicion_groot = posicion_personaje(pila_personajes, "Groot")

# b. Personajes con más de 5 películas
personajes_5_peliculas = personajes_mas_de_5_peliculas(pila_personajes)

# c. Cantidad de películas de Black Widow
peliculas_black_widow = cantidad_peliculas_personaje(pila_personajes, "Black Widow")

# d. Personajes cuyos nombres empiezan con C, D y G
personajes_iniciales = personajes_con_iniciales(pila_personajes, "CDG")

print(f"Posicion de Rocket Raccoon: {posicion_rocket}")
print(f"Posicion de Groot: {posicion_groot}")
print("Personajes con mas de 5 peliculas:", personajes_5_peliculas)
print(f"Cantidad de peliculas de Black Widow: {peliculas_black_widow}")
print("Personajes cuyos nombres empiezan con C, D y G:", personajes_iniciales)