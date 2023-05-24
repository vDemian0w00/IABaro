import random
import openpyxl

# Banco de palabras para generar nombres de gastos_variables_pre
palabras_variables_pre = ['tinte de cabello', 'tinte cabello', 'corte de cabello', 'corte de pelo', 'corte de cabello','comida fuera', 'café de tienda', 'cenas elegantes', 'peluquería', 'estetica', 'cuidado personal','viajes innecesarios', 'cine', 'entrada six flags', 'cumpleaños', 'pastel', 'entrada de cine', 'entrada a parque de diversiones', 'comida cumpleaños', 'antro', 'juguete mascota', 'decoracion', 'fiesta', 'reunion', 'fiesta de cumpleaños', 'instrumento musical', 'boleto de avion', 'boleto para concierto', 'boleto para evento', 'ropa deportiva', 'cosmético', 'perfumes', 'perfume','maquillaje', 'accesorio', 'revistas', 'libros', 'compra de música', 'clases particulares', 'electrónicos', 'decoración de interiores', 'plantas', 'flores', 'regalo', 'joya', 'visita a museo', 'visitas a galerías de arte', 'plancha de pelo', 'maquina de palomitas', 'articulos de papeleria', 'folder', 'cuaderno', 'lapiz', 'lapicero', 'borrador', 'goma de borrar', 'regla', 'calculadora', 'tijeras', 'papel', 'cartulina', 'papel bond', 'papel de regalo', 'papel de envolver', 'papel de cocina', 'papel higienico', 'papel de baño', 'papel de aluminio', 'cojin', 'crema para la cara', 'teatro', 'boleto de teatro', 'boletos de cine', 'boletos teatro', 'nutriologo', 'peluqueria', 'estética', 'cena con amigos', 'cumpleaños', 'festejo', 'concierto', 'festival', 'evento', 'eventos', '']

# Meses
dias=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

nombres=['ana', 'maria', 'sofia', 'isabella', 'valeria', 'lucia', 'paola', 'carolina', 'andrea', 'juliana', 'valentina', 'daniela', 'natalia', 'adriana', 'angela', 'laura', 'claudia', 'monica', 'camila', 'catalina', 'liliana', 'veronica', 'diana', 'silvia', 'patricia', 'viviana', 'johana', 'ximena', 'ana maria', 'mariana', 'paulina', 'karina', 'jessica', 'alejandra', 'cristina', 'rosa', 'jennifer', 'mary', 'jenny', 'doris', 'gabriela', 'cecilia', 'veronica', 'jimena', 'tania', 'fernanda', 'margarita', 'fabiola', 'luz',  'juan', 'carlos', 'jose', 'luis', 'miguel', 'fernando', 'pablo', 'ricardo', 'daniel', 'cesar', 'eduardo', 'david', 'oscar', 'andres', 'jorge', 'antonio', 'manuel', 'augusto', 'rafael', 'gabriel', 'alejandro', 'lucas', 'alonso', 'sergio', 'marco', 'alberto', 'roberto', 'ramon', 'leonardo', 'mauricio', 'rodrigo', 'maximiliano', 'benjamin', 'francisco', 'pedro', 'guillermo', 'ignacio', 'omar', 'javier', 'edgar', 'juan carlos', 'victor', 'felipe', 'adrian', 'hector', 'mario', 'julio', 'hugo', 'hijo', 'hija', 'hijos', 'marido', 'esposa', 'novia', 'novio', 'tio', 'tia', 'niños', 'niña', 'niña', 'abuelita', 'abuela', 'abuelo', 'suegro', 'suegra', 'yerno', 'nuera', 'hermanastro', 'hermanastra', 'papa', 'mama', 'madre', 'padre', 'padrastro', 'madrastra', 'bisabuela', 'cuñado', 'cuñada','abuelito', 'yerno', 'sobrino', 'sobrina', 'cuñado', 'cuñada', 'Juan', 'José', 'Antonio', 'Jesús', 'Francisco', 'Manuel', 'Miguel', 'David', 'Pedro', 'Carlos', 'Daniel', 'Luis', 'Rafael', 'Alejandro', 'Roberto', 'Jorge', 'Fernando', 'Javier', 'Enrique', 'Alberto', 'Ricardo', 'Guillermo', 'Héctor', 'Mario', 'Ernesto', 'Ignacio', 'Eduardo', 'Gabriel', 'Andrés', 'Arturo', 'Armando', 'Sergio', 'Salvador', 'Oscar', 'Israel', 'Emilio', 'Juan Carlos', 'Adrián', 'Gustavo', 'Víctor', 'Raúl', 'Leonardo', 'César', 'Julio', 'Benjamín', 'José Luis', 'Ismael', 'Samuel', 'Mauricio', 'Mariano', 'Agustín', 'Gerardo', 'Abraham', 'Albert', 'Octavio', 'Alfredo', 'Joel', 'Joaquín', 'Diego', 'Jairo', 'Alonso']

# Banco de palabras para generar nombres de gastos_variables_pre
nombres_variables_pre=[
    'Gasto {palabra}',
    '{palabra}',
    'Pago de {palabra}',
    'Gasto de {palabra}',
    'Pago {palabra}',
    '{palabra} {nombre}',
    '{palabra} {nombre} {dia}',
    '{palabra} {dia}',
]

# Banco de frases para generar descripciones de gastos_variables_pre
descripciones_variables_pre = [
    'Pago de {palabra} {nombre}',
    'Pago de {palabra} {nombre} {dia}',
    'Pago de {palabra} {dia}',
    'Gasto de {palabra} {nombre}',
    'Gasto de {palabra} {nombre} {dia}',
    'Gasto de {palabra} {dia}',
    'Este fue el gasto para el {palabra} de {nombre}',
    'Devolver {palabra} porque salió defectuoso',
    'Este dinero correponde a la compra de {palabra} para {nombre}',
    'Este dinero correponde a la compra de {palabra} para {nombre} el {dia}',
    'Compra de {palabra}',
    'Gasto destinado para {palabra}',
    'Compra de {palabra} del dia {dia}',
    'Compra de {palabra} para {nombre}',
]

# abrir el archivo xlsx
libro = openpyxl.load_workbook('data_synthetic_baro.xlsx')

# crear hoja de trabajo
hoja4 = libro.create_sheet("variables_pre")

# escribir datos en las hojas
hoja4['A1'] = "name"
hoja4['B1'] = "description"
hoja4['C1'] = "amount"

for i in range(10000):
    name=random.choice(nombres_variables_pre)
    palabra = random.choice(palabras_variables_pre)
    name=name.replace('{palabra}', palabra)
    name=name.replace('{nombre}', random.choice(nombres))
    name=name.replace('{dia}', random.choice(dias))
    # establecer el contenido de la celda
    celda = 'A{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja4[celda] = name
    
    # generar la descripción
    palabra_encontrada = False
    while not palabra_encontrada:
        description=random.choice(descripciones_variables_pre)
        descripcion_palabra = random.choice(palabras_variables_pre)
        description=description.replace('{palabra}', descripcion_palabra)
        description=description.replace('{nombre}', random.choice(nombres))
        description=description.replace('{dia}', random.choice(dias))
        if palabra in description:
            palabra_encontrada = True
        # establecer el contenido de la celda
        celda = 'B{}'.format(i+2)  # aumentar el índice de fila para cada iteración
        hoja4[celda] = description
    
    amount=random.randint(100, 10000)
    # establecer el contenido de la celda
    celda = 'C{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja4[celda] = amount

# Guardar el archivo xlsx
libro.save('data_synthetic_baro.xlsx')