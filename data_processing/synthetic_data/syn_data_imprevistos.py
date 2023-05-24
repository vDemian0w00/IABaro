import random
import openpyxl

# Banco de palabras para generar nombres de gastos_imprevistos
palabras_imprevistos = ['funeral', 'urgencia médica', 'viaje de trabajo', 'viaje trabajo', 'urgencias', 'accidente', 'accidente de tráfico', 'accidente de coche', 'accidente de moto', 'accidente de bicicleta', 'robo', 'carro robado', 'casa robada', 'daños a la propiedad', 'viaje inesperado', 'muerte', 'gasto legal', 'gastos legales', 'multa', 'llanta ponchada', 'neumatico', 'imprevisto', 'imprevistos', 'reemplazo tuberia', 'reemplazo de bateria de auto', 'pérdida de empleo', 'pérdida trabajo', 'desastre natural', 'temblor', 'terremoto', 'tsunami', 'inundacion', 'huracan', 'incendio', 'incendio forestal', 'tornado', 'calor extremo', 'funeraria', 'falla', 'desalojo', 'desalojo de casa', 'desalojo de local', 'desalojo local', 'reparación eléctrica', 'reparación de plomería', 'reparación de electrodoméstico', 'reparación de computadora', 'reparación de lavadora', 'reparacion de refrigerador', 'reparación del hogar', 'reparación de gotera', 'robo de celular', 'robo de identificaciones', 'robo de cartera', 'multa estacionamiento', 'multa exceso de velocidad', 'reparacion de ventanas', 'reparacion de pared', 'cancer', 'quimioterapias', 'medicina', 'enfermedad', 'operación', 'cirugia', 'robo total', 'robo parcial', 'falla', 'oxigeno', 'tanque de oxigeno', 'hospital', 'cita hospital', 'camilla', 'gastos médicos', 'emergencia', 'multa', 'multas', 'muerte', 'fallecimiento', 'enfermedad', 'enfermo', 'enfermedades', 'funeral', 'velorio', 'embargue', 'embar', 'daño', 'avería', 'accidente', 'accidentes', 'multas', 'hospital', 'gastos médicos', 'emergencia', 'médico', 'medico', 'doctor', 'mudanza inesperada', 'urgencia', 'reparacion', 'reparacion', 'penalizacion', 'penalización', 'viaje de emergencia', 'reemplazo', 'reemplazos', 'legal', 'inesperado', 'problema inesperado', 'carcel', 'fianza', 'fianzas', 'emergencia', 'imprevisto', 'imprevistos', 'daños', 'reemplazo', 'pérdida', 'pérdidas', 'perdida total', 'perdidas', 'perdidas', 'roto', 'rotos', 'rota', 'choque', 'choques', 'asalto', 'asaltos', 'reparacion', 'repentino', 'repentinos', 'arreglo', 'arreglado', 'cambio', 'cambios', 'fuga', 'fugas', 'emergencia', 'tsunami', 'terremoto', 'pastilla del dia siguiente', 'pastilla embarazo', 'post day', 'temblor', 'huracan', 'temblores', 'temblor', 'inundacion', 'inundación', 'inundaciones', 'avalancha', 'deslaves', 'deslave', 'huracán', 'tornado', 'tornados', 'deslizamiento de tierra', 'emergencia perro', 'emergencia mascota', 'lluvia fuerte', 'lluvia', 'inundacion', 'tormenta eléctrica', 'rayo', 'tormenta', 'trueno', 'roto', 'rota', 'granizo', 'granizada', 'erupción volcánica', 'volcán', 'volcan', 'erupcion', 'muerte', 'muertes', 'fallecimiento', 'fallecimientos', 'incendio', 'incendios', 'quemadura', 'quemado', 'quema', 'quemada', 'cargo adicional', 'cargos adicionales', 'defectuoso', 'infracción', 'infracciones', 'infraccion', 'fugas', 'fuga', 'problema', 'problemas', 'agotado', 'agotados','agotadas', 'agotados', 'vandalismo', 'vandálico', 'reemplazos', 'perdida', 'daño', 'perdidos', 'exceso', 'plaga', 'plagas', 'chinches', 'chinche', 'piojos','dañado', 'dañada', 'insectos', 'desgaste', 'desgastes', 'problemas', 'problemas de conexión', 'fractura', 'ataque cardiaco', 'ataque cardíaco', 'accidente', 'accidentes', 'crisis', 'desalojo','desalojado', 'nehumonía', 'gripa', 'médico', 'medicina', 'medicamentos', 'medicamento', 'medicamento', 'consulta', 'consulta médica', 'consulta con el doctor', 'consulta doctor', 'mecánico', 'mecanico', 'arreglo de refri', 'arreglo de lavadora', 'arreglar', 'arreglo', 'arreglado', 'arreglo', 'cambio', 'atención médica', 'atencion medica', 'cita doc', 'cita doctor', 'consulta doctor', 'reparar', 'reparación', 'reparacion', 'desastre natural', 'desastres naturales', 'multa', 'infraccion', 'tratamiento', 'tratamiento medico', 'perder', 'perdida', 'pérdida', 'cancelación', 'cancelado', 'cancelacion', 'legal', 'legales', 'legalidad', 'legal'] 

# Meses
dias=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

nombres=['hijo', 'hija', 'hijos', 'marido', 'esposa', 'novia', 'novio', 'tio', 'tia', 'niños', 'niña', 'niña', 'abuelita', 'abuela', 'abuelo', 'suegro', 'suegra', 'yerno', 'nuera', 'hermanastro', 'hermanastra', 'papa', 'mama', 'madre', 'padre', 'padrastro', 'madrastra', 'bisabuela', 'cuñado', 'cuñada','abuelito', 'yerno', 'sobrino', 'sobrina', 'cuñado', 'cuñada', 'Juan', 'José', 'Antonio', 'Jesús', 'Francisco', 'Manuel', 'Miguel', 'David', 'Pedro', 'Carlos', 'Daniel', 'Luis', 'Rafael', 'Alejandro', 'Roberto', 'Jorge', 'Fernando', 'Javier', 'Enrique', 'Alberto', 'Ricardo', 'Guillermo', 'Héctor', 'Mario', 'Ernesto', 'Ignacio', 'Eduardo', 'Gabriel', 'Andrés', 'Arturo', 'Armando', 'Sergio', 'Salvador', 'Oscar', 'Israel', 'Emilio', 'Juan Carlos', 'Adrián', 'Gustavo', 'Víctor', 'Raúl', 'Leonardo', 'César', 'Julio', 'Benjamín', 'José Luis', 'Ismael', 'Samuel', 'Mauricio', 'Mariano', 'Agustín', 'Gerardo', 'Abraham', 'Albert', 'Octavio', 'Alfredo', 'Joel', 'Joaquín', 'Diego', 'Jairo', 'Alonso', 'Susana', 'Claudia', 'Adriana', 'Alejandra', 'Mónica', 'Esther', 'Paulina', 'Gisela', 'Beatriz', 'Irma', 'Rosario', 'Emma', 'Miriam', 'Angélica', 'Norma', 'Diana', 'Gabriela', 'Pilar', 'Carolina', 'Alicia', 'Olga', 'Julia', 'Cristina', 'Teresa', 'Cecilia', 'Aurora', 'Rafaela', 'Lucía', 'Raquel', 'Marta', 'Magdalena', 'Edith', 'Estela', 'Montserrat', 'Elvira', 'Catalina', 'Mirna', 'Nancy', 'Rosa María']

# Banco de palabras para generar nombres de gastos_imprevistos
nombres_imprevistos=[
    'Gasto {palabra}',
    '{palabra}',
    'Pago de {palabra}',
    'Gasto de {palabra}',
    'Pago {palabra}',
    '{palabra} {nombre}',
    '{palabra} {nombre} {dia}',
    '{palabra} {dia}',
]

# Banco de frases para generar descripciones de gastos imprevistos
descripciones_imprevistos = [
    'Gasto de {palabra} {nombre}',
    'Gasto de {palabra} {nombre} {dia}',
    'Gasto {dia}',
    'Pago de {palabra} {nombre}',
    'Pago de {palabra} {nombre} {dia}',
    'Pago {palabra} correspondiente al dia {dia}',
    'El dia {dia} se pago {palabra}',
    'Se hizo el pago de {palabra} el dia {dia}',
    'Cobro de {palabra} el dia {dia}',
    'Imprevisto de {palabra} el dia {dia}',
    'Emergencia de {palabra} el dia {dia}',
    'Emergencia {nombre}',
    'Se tuvo que pagar {palabra} el dia {dia}',
]

# abrir el archivo xlsx
libro = openpyxl.load_workbook('data_synthetic_baro.xlsx')

# crear hoja de trabajo
hoja6 = libro.create_sheet("imprevistos")

# escribir datos en las hojas
hoja6['A1'] = "name"
hoja6['B1'] = "description"
hoja6['C1'] = "amount"

for i in range(10000):
    name=random.choice(nombres_imprevistos)
    palabra = random.choice(palabras_imprevistos)
    name=name.replace('{palabra}', palabra)
    name=name.replace('{nombre}', random.choice(nombres))
    name=name.replace('{dia}', random.choice(dias))
    # establecer el contenido de la celda
    celda = 'A{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja6[celda] = name
    
    # generar la descripción
    palabra_encontrada = False
    while not palabra_encontrada:
        description=random.choice(descripciones_imprevistos)
        descripcion_palabra = random.choice(palabras_imprevistos)
        description=description.replace('{palabra}', descripcion_palabra)
        description=description.replace('{nombre}', random.choice(nombres))
        description=description.replace('{dia}', random.choice(dias))
        if palabra in description:
            palabra_encontrada = True
        # establecer el contenido de la celda
        celda = 'B{}'.format(i+2)  # aumentar el índice de fila para cada iteración
        hoja6[celda] = description
    
    amount=random.randint(100, 10000)
    # establecer el contenido de la celda
    celda = 'C{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja6[celda] = amount

# Guardar el archivo xlsx
libro.save('data_synthetic_baro.xlsx')