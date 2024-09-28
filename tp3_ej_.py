from lista import by_name
from collections import Counter

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



# FUNCIONES
#
# ORDENAR POR NOMBRES
super_heroes.sort(key=by_name)

# MOSTRAR INFORMACION
def mostrar_informacion(superheroe, campo=None):
    # Si se especifica un campo, solo mostrar ese campo
    if campo:
        return f"{campo.capitalize()}: {superheroe[campo]}"
    # Si no se especifica, mostrar toda la información
    return (
        f"La información de {superheroe['nombre']} es:\n"
        f"- Nombre: {superheroe['nombre']}\n"
        f"- Año de aparición: {superheroe['año_aparicion']}\n"
        f"- Casa de cómic: {superheroe['casa_comic']}\n"
        f"- Biografía: {superheroe['biografia']}\n"
    )


def search(super_heroes, criterio, value):
    for index, element in enumerate(super_heroes):
        if element[criterio] == value:
            return index
          
# ELIMINAR NODO          
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

          
# LISTAR          
def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()
   
# MOSTRAR INFORMACION DE UN SUPERHEROE

def info_nombre(buscado):
    print(f'la info de {buscado} es: ')
    info_nombre = super_heroes[search(super_heroes, 'nombre', buscado)]
    print(mostrar_informacion(info_nombre))
    return info_nombre
   
   
   
# RESPUESTAS   
  
  
          
"""a. Eliminar el nodo que contiene la informacion de Linterna Verde """   

  # parameotro de busqueda
criterio = 'nombre'
valor = 'Linterna Verde'


result_delete = remove(super_heroes, criterio, valor)
print(f'Eliminar {valor} resultado: {result_delete}')
print()


""" b. mostrar el año de aparecicion de Wolwerine """

print(f'Wolverine aparecio en el año {super_heroes[search(super_heroes, criterio, "Wolverine")]["año_aparicion"]}')
print()

""" c. cambiar la casa de Dr.Strange a Marvel """

super_heroes[search(super_heroes, criterio, "Doctor Strange")]["casa_comic"] = "Marvel"
print(f'La casa de Doctor Strange fue cambiada a: {super_heroes[search(super_heroes, criterio, "Doctor Strange")]["casa_comic"]}')
print()



""" d. mostrar el nombre de aquellos superheroes que en su biografica menciona la palabra "traje" o "armadura" """
print("Los Superheroes que mencionan traje o armadura en su biografia son:")
for super_hero in super_heroes:
    if "traje" in super_hero["biografia"] or "armadura" in super_hero["biografia"]:
        print(super_hero["nombre"])
print()        
        

""" e. mostrar el nombre y la casa de los superheroes cuya fecha de aparicion sea anterior a 1963 """

print("Los Superheroes que aparecieron antes de 1963 son:")
super_heroes.sort(key=by_name)
for super_hero in super_heroes:
    if super_hero["año_aparicion"] < 1963:
        print(super_hero["nombre"], super_hero["casa_comic"])
print()


""" f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla """

print("La casa de Capitana Marvel es:")
print(super_heroes[search(super_heroes, criterio, "Capitana Marvel")]["casa_comic"])
print("La casa de Mujer Maravilla es:")
print(super_heroes[search(super_heroes, criterio, "Mujer Maravilla")]["casa_comic"])
print()

""" g. mostrar toda la informacion de Flash y Star-Lord """

flash_info = super_heroes[search(super_heroes, 'nombre', 'Flash')]
print(mostrar_informacion(flash_info))
print()
starlord_info = super_heroes[search(super_heroes, 'nombre', 'Star-Lord')]
print(mostrar_informacion(starlord_info))
print()

""" h. listar los superhéroes que comienzan con la letra B, M y S  """

print("Los Superheroes que comienzan con las letras B, M o S son:")
for super_hero in super_heroes:
    if super_hero["nombre"][0] in ["B", "M", "S"]:
        print(super_hero["nombre"])
print()


""" i. determinar cuántos superhéroes hay de cada casa de comic """

cantidad_comic = Counter(hero["casa_comic"] for hero in super_heroes)
for comic, count in cantidad_comic.items():
  print(f"{comic}: {count}")


















