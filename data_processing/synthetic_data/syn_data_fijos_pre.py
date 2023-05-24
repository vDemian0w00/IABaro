import random
import openpyxl

# Banco de palabras para generar nombres de gastos_fijos_pre
palabras_fijos_pre = ['entrenamiento', 'natacion', 'football', 'futbol', 'basketball', 'beisbol', 'gimnasia', 'voleibol', 'hockey', 'atletismo', 'deporte', 'rugby', 'gimnasio', 'GYM', 'gym', 'netflix', 'disney Plus', 'Disney +',  'hbo max', 'HBO', 'hbo','amazon prime', 'prime', 'amazon', 'spotify Premium', 'premium', 'spotify', 'apple Music', 'apple', 'icloud', 'Apple Music', 'tidal', 'youtube', 'YouTube', 'youtube Premium', 'kindle Unlimited', 'kindle', 'clases de yoga', 'yoga', 'pilates', 'zumba','clases de pilates', 'baile', 'clases de baile', 'entrenador personal', 'masajes', 'salon', 'salón de belleza', 'manicura', 'pedicura', 'depilación láser', 'ropa de marca', 'membresía de club social', 'xbox game pass', 'game pass', 'play plus', 'playstation plus', 'membresia six flags', 'six flags', 'suscripción revista', 'suscripcion periodico', 'hulu', 'apple tv', 'paramount', 'crunchyroll', 'sport city', 'ymca', 'noticias', 'cinepolis fan', 'club de cocina', 'club de escritura', 'club de esgrima', 'servicio de correo', 'socio', 'membresia', 'servicio', 'vacaciones', 'salida por vacaciones', 'cable', 'tv', 'servicio de tv', 'taller', 'servicio de streaming', 'servicio de peliculas', 'membresia gym', 'suscripcion revista', 'suscripcion', 'suscripciones', 'suscripcion web', 'clases de cocina', 'club', 'clubes', 'clubs', 'suscripcion a tienda en linea', 'suscripcion servicio', 'membresía', 'membresías', 'membresia', 'premium', 'membresia', 'crunchyroll', 'crunchy', 'prime', 'amazon prime', '']

# Meses
meses=['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

nombres=['abril', 'adriel', 'aisha', 'alberto', 'alejandra', 'alejandro', 'alicia', 'alondra', 'amanda', 'ambar', 'ana', 'anahi', 'andrea', 'angel', 'angela', 'antonio', 'ariadna', 'ariana', 'armando', 'arturo', 'astrid', 'axel', 'beatriz', 'benjamin', 'bernardo', 'josue', 'juan', 'julieta', 'karina', 'karla', 'kassandra', 'katherine', 'kevin', 'laura', 'liliana', 'lizbeth', 'lucia', 'luis', 'luisa', 'magdalena', 'manuel', 'marcela', 'margarita', 'maria', 'mariana', 'mario', 'marisol', 'martin', 'mateo', 'mauricio', 'maximiliano', 'melanie', 'melissa', 'miguel', 'miriam', 'monica', 'nadia', 'Natalia', 'Nayeli', 'Nicolás', 'Nidia', 'Noelia', 'Norma', 'Octavio', 'Oliver', 'Olivia', 'Omar', 'Orlando', 'Oscar', 'Pablo', 'Paola', 'Patricia', 'Paula', 'Pedro', 'Perla', 'Pilar', 'Priscila', 'Rafael', 'Ramiro', 'Raúl', 'Raymundo', 'Rebeca', 'Regina', 'Renata', 'René', 'Ricardo', 'Roberto', 'Rodrigo', 'Rogelio', 'Rolando', 'Román', 'Romina', 'Rosario', 'Rubén', 'Ruth', 'Sabrina', 'hijo', 'hija', 'hijos', 'marido', 'esposa', 'novia', 'novio', 'tio', 'tia', 'niños', 'niña', 'niña', 'abuelita', 'abuela', 'abuelo', 'suegro', 'suegra', 'yerno', 'nuera', 'hermanastro', 'hermanastra', 'papa', 'mama', 'madre', 'padre', 'padrastro', 'madrastra', 'bisabuela', 'cuñado', 'cuñada','abuelito', 'yerno', 'sobrino', 'sobrina', 'cuñado', 'cuñada', 'Juan', 'José', 'Antonio', 'Jesús', 'Francisco', 'Manuel', 'Miguel', 'David', 'Pedro', 'Carlos', 'Daniel', 'Luis', 'Rafael', 'Alejandro', 'Roberto', 'Jorge', 'Fernando', 'Javier', 'Enrique', 'Alberto',]

# Banco de palabras para generar nombres de gastos_fijos_pre
nombres_fijos_pre=[
    'Gasto {palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    'Pago de {palabra}',
    'Gasto de {palabra}',
    'Pago {palabra}',
    '{palabra} {nombre}',
    '{palabra} {nombre} {mes}',
    '{palabra} de {nombre}',
    'Gasto de {palabra} de {nombre}',
    'Pago de {palabra} de {nombre}',
    'Gasto de {palabra} de {nombre} {mes}',
    'Gasto de {palabra} de {nombre} {mes}',
    '{nombre} {mes}',
    '{palabra}, {mes}',
    '{palabra}, {nombre}'
]

# Banco de frases para generar descripciones de gastos_fijos_pre
descripciones_fijos_pre = [
    'Dinero para {palabra}',
    'Dinero para el pago de {palabra}',
    'Dinero para el pago de {palabra} del mes de {mes}',
    'Pago de {palabra} del mes de {mes}',
    'Pago de {palabra} del mes',
    'Gasto de {palabra}',
    'Gasto de {palabra} del mes de {mes}',
    'Gasto de {palabra} del mes',
    'Pago mensual de {palabra}',
    'Pago quincenal de {palabra}',
    'Pago semanal de {palabra}',
    'Pago anual de {palabra}',
    'Gasto mensual de {palabra}',
    'Gasto quincenal de {palabra}',
    'Gasto semanal de {palabra}',
    'Gasto anual de {palabra}',
    'Mensualidad de {palabra}',
    'Anualidad de {palabra}',
    'Semestralidad de {palabra}',
    '{palabra} {nombre}',
    '{palabra} {nombre} {mes}',
    'Gasto de {palabra} de {nombre}',
    'Pago de {palabra} de {nombre}',
    'Este es el pago de {palabra} correspondiente al mes de {mes}',
    'Este es el pago de {palabra} correspondiente al mes',
    'Este es el pago de {palabra} correspondiente al mes de {mes} de {nombre}',
]

# abrir el archivo xlsx
libro = openpyxl.load_workbook('data_synthetic_baro.xlsx')

# crear hoja de trabajo
hoja2 = libro.create_sheet("fijos_pre")

# escribir datos en las hojas
hoja2['A1'] = "name"
hoja2['B1'] = "description"
hoja2['C1'] = "amount"

for i in range(10000):
    name=random.choice(nombres_fijos_pre)
    palabra = random.choice(palabras_fijos_pre)
    name=name.replace('{palabra}', palabra)
    name=name.replace('{nombre}', random.choice(nombres))
    name=name.replace('{mes}', random.choice(meses))
    # establecer el contenido de la celda
    celda = 'A{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja2[celda] = name
    
    # generar la descripción
    palabra_encontrada = False
    while not palabra_encontrada:
        description=random.choice(descripciones_fijos_pre)
        descripcion_palabra = random.choice(palabras_fijos_pre)
        description=description.replace('{palabra}', descripcion_palabra)
        description=description.replace('{nombre}', random.choice(nombres))
        description=description.replace('{mes}', random.choice(meses))
        if palabra in description:
            palabra_encontrada = True
        # establecer el contenido de la celda
        celda = 'B{}'.format(i+2)  # aumentar el índice de fila para cada iteración
        hoja2[celda] = description
    
    amount=random.randint(100, 10000)
    # establecer el contenido de la celda
    celda = 'C{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja2[celda] = amount

# Guardar el archivo xlsx
libro.save('data_synthetic_baro.xlsx')