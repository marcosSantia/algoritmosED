from lista import search, by_name, by_house, remove


super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]
#! criterios de orden
def by_name(item):
    return item['nombre']

def by_temp(item):
    return item['temp']

def by_hegiht(item):
    return item['altura']

def by_house(item):
    return item['casa_comic']+item['nombre']

super_heroes.sort(key=by_name)

# #! busqueda elementos simples
def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

buscado = 'None'
criterio = 'None'


        
def mostrar_informacion(superheroe, campo=None):
    # Si se especifica un campo, solo mostrar ese campo
    if campo:
        return f"{campo.capitalize()}: {superheroe[campo]}"
    # Si no se especifica, mostrar toda la información
    return (
        f"Información de {superheroe['nombre']}:\n"
        f"- Nombre: {superheroe['nombre']}\n"
        f"- Año de aparición: {superheroe['año_aparicion']}\n"
        f"- Casa de cómic: {superheroe['casa_comic']}\n"
        f"- Biografía: {superheroe['biografia']}\n"
    )

# PARA MOSTRAR LA INFO DE TODOS LOS SUPERHEROES
# for superheroe in super_heroes:
#     print(mostrar_informacion(superheroe))
#     print()


# # Definir la función search si no la tienes
# def search(lista, criterio, valor):
#     for idx, item in enumerate(lista):
#         if item[criterio] == valor:
#             return idx
#     return -1

# Mostrar información de Flash y Star-Lord
# print("La información de Flash es:")
# flash_info = super_heroes[search(super_heroes, 'nombre', 'Flash')]
# print(mostrar_informacion(flash_info, campo='año_aparicion'))

# print("La información de Star-Lord es:")
# starlord_info = super_heroes[search(super_heroes, 'nombre', 'Star-Lord')]
# print(mostrar_informacion(starlord_info))
 


# print(f'la info de {nombre} es: ')

# personaje_info = super_heroes[search(super_heroes, 'nombre', nombre)]

# print(mostrar_informacion(personaje_info))

# personaje_info = super_heroes[search(super_heroes, 'nombre', nombre)]
# return mostrar_informacion(personaje_info)


def info_nombre(nombre):
    print(f'la info de {nombre} es: ')
    info_nombre = super_heroes[search(super_heroes, 'nombre', nombre)]
    print(mostrar_informacion(info_nombre))
    return info_nombre
  
nombre = 'La Cosa'  
info_nombre(nombre)


# print("La informacion de Flash es:")
# print(super_heroes[search(super_heroes, criterio, "Flash")])
# print("La informacion de Star-Lord es:")
# print(super_heroes[search(super_heroes, criterio, "Star-Lord")])
# print()



# #! ordenar elementos simples
# personajes_star_wars.sort(key=by_name)



# print(f'el personaje esta en la posicion {search(personajes_star_wars, criterio, buscado)}')

# def remove(list_values, criterio, value):
#     index = search(list_values, criterio, value)
#     if index is not None:
#         return list_values.pop(index)
    
# eliminar = 'R2-D2'
# result_delete = remove(personajes_star_wars, criterio, eliminar)
# print(f'Eliminar {eliminar} resultado: {result_delete}')

# def show_list(title, list_values):
#     print()
#     print(f"{title}")
#     for index, elemento in enumerate(list_values):
#         print(index, elemento)
#     print()

# show_list('Personajes Star Wars', personajes_star_wars)

##################################################
# infoLinternaVerde = super_heroes[search(super_heroes, criterio, valor)]

# print(mostrar_informacion(infoLinternaVerde))
########################################