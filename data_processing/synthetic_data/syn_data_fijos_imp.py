import random
import openpyxl

# Banco de palabras para generar nombres de gastos_fijos_imp
palabras_fijos_imp = ['agua', 'suministro de agua', 'consumo de agua', 'agua potable', 'agua para baño', 'consumo de agua', 'recibo del agua', 'CFE', 'recibo agua', 'consumo de luz', 'luz', 'recibo de luz', 'recibo luz', 'electricidad', 'energia electrica', 'Luz CFE', 'gas lp', 'gas natural', 'lp', 'recibo del gas', 'recibo gas', 'recarga de gas', 'recibo telefono', 'servicio telefonico', 'linea de telefono', 'linea telefonica', 'telefonia', 'conexion a internet', 'recibo de internet', 'wifi', 'red', 'poliza del auto', 'renta departamento', 'departamento', 'gas', 'internet', 'teléfono', 'celular', 'seguro', 'colegio', 'universidad', 'transporte', 'alquiler', 'hipoteca', 'tarjeta', 'crédito', 'préstamo', 'casa', 'carro', 'moto', 'servicios', 'impuesto', 'coche', 'colegiatura', 'hogar', 'televisión', 'despensa', 'gasolina', 'motocicleta', 'seguro médico', 'seguro de vida', 'seguro de gastos médicos', 'seguro de auto', 'seguro de casa', 'seguro de moto', 'comision', 'comisión', 'comisiones', 'servicio del carro', 'guarderia', 'prepa', 'secundaria', 'preparatoria', 'kinder', 'seguro', 'compra de alimentos', 'canasta básica', 'comisiones', 'alimentos', 'renta', 'ropa', 'prendas para vestir', 'curso', 'cursos', 'vestimenta', 'ropa', 'impuesto sobre la renta', 'irs', 'IRS','impuesto al valor agregado', 'iva', 'IVA', 'ieps', 'IEPS', 'impuesto especial sobre producción y servicios', 'IETU', 'ietu', 'impuesto empresarial a la tasa única', 'IDE', 'ide', 'impuesto a los depósitos en efectivo', 'ISAN', 'isan', 'impuesto a los autos nuevos', 'impuesto de mi auto nuevo', 'aduana', 'Aduana', 'aduana', 'impuesto por la importación y exportación de mercancias', 'mercancia', 'mercancia', 'cedular', 'dap', 'DAP', 'derecho al alumbrado público', 'IEDU', 'iedu', 'impuesto aplicable a bebidas alcohilas', 'tenencia', 'Tenencias', 'verificacion carro', 'verificacion auto', 'IMSS', 'impuesto nómina', 'infonavit', 'INFONAVIT', 'mantenimiento del edificio', 'mantenimiento de la casa', 'mantenimiento', 'seguro de la casa', 'seguro del hogar', 'préstamo', 'préstamo para la casa', 'préstamo del carro', 'pension', 'pensiones', 'préstamo del banco', 'préstamo banco', 'recarga tarjeta del metro', 'tarjeta metro', 'recarga metro', 'boletos metros', 'boletos para metro', 'tarjeta de debito', 'tarjeta de credito', 'impuesto sobre la propiedad', 'alimento mascota', 'alimento para perro', 'alimento para gato', 'alimento para pez', 'croquetas', 'alimentos casa', 'alimentos para la casa', 'costal croquetas', 'whiskas', 'sobre comida perro', 'sobre comida gato', 'sobre comida mascota', 'fecha de corte', 'fecha limite de pago', 'deuda', 'banco', 'credito', 'debito', 'nomina', 'suministros', 'servicios publicos', 'terapia', 'psicologo', 'meses sin intereses', 'intereses', 'meses con intereses', 'limpieza de la casa', 'limpieza casa', 'señora limpieza', 'agua caliente', 'condominio', 'depa', 'receta medicamento', 'medicamento', 'deudas', 'legal', 'legales', 'transporte público', 'recarga tarjeta', 'tarjeta recarga', 'manutencion', 'plan de pensiones', 'local', 'changarro', 'tienda', 'local comercial', 'renta de un almacén', 'renta de bodega', 'bodega', 'depa', 'edificio', 'hogar', 'renta oficina', 'renta', 'renta trabajo', 'red de agua', 'internet de alta velocidad', 'seguro de salud', 'hipoteca de la casa', 'hipoteca del banco', 'banco', 'recarga de la gas', 'recarga del celular', 'saldo telefono', 'saldo', 'gas', 'combustible del carro', 'combustible', 'mantenimientos', 'seguro de invalidez', 'plan de jubilacion', 'plan', 'planes', 'seguro contra robos', 'seguro vital', 'agua caliente', 'limpieza del edificio', 'limpieza de la casa', 'servicio de limpieza', 'servicio', 'servicios', 'vivienda', 'ropa', 'calzado', 'electricidad', 'servicio de electricidad', 'coches', 'recarga', 'alojamiento', 'alojamiento', 'negocio', 'negocios', 'impuestos del negocio', 'cosas del negocio', 'abastecimiento del negocio', 'abastecimiento', 'reabastecimiento', 'reabastecimientos', 'abastecimientos', 'insumos', 'servicios basicos', 'tanque de oxígeno', 'escuela de paga', 'colegios', 'escuelas', 'bachillerato', 'secu', 'preescolar', 'clases', 'clase', 'curso', 'cursos', 'curso educacion', 'educacion', 'verificacion del carro', 'verificacion coche', 'dentista'] 

# Meses
meses=['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

nombres=['María', 'Guadalupe', 'Juana', 'Ana', 'Carmen', 'Francisca', 'Rosa', 'Elena', 'Leticia', 'Isabel', 'Sara', 'Laura', 'Margarita', 'Patricia', 'Verónica', 'Gloria', 'Victoria', 'Natalia', 'Silvia', 'Susana', 'Claudia', 'Adriana', 'Alejandra', 'Mónica', 'Esther', 'Paulina', 'Gisela', 'Beatriz', 'Irma', 'Rosario', 'Emma', 'Miriam', 'Angélica', 'Norma', 'Diana', 'Gabriela', 'Pilar', 'Carolina', 'Alicia', 'Olga', 'Julia', 'Cristina', 'Teresa', 'Cecilia', 'Aurora', 'Rafaela', 'Lucía', 'Raquel', 'Marta', 'Magdalena', 'Edith', 'Estela', 'Montserrat', 'Elvira', 'Catalina', 'Mirna', 'Nancy', 'Rosa María', 'Mariana', 'Inés', 'Leonora', 'Berta', 'Renata', 'Esmeralda', 'Mayra', 'Jazmín', 'Rebeca', 'Gloria María', 'Constanza', 'Julieta', 'Irene', 'Lorena', 'Emilia', 'Jovita', 'Marisol', 'Alma', 'Maricela', 'Yolanda', 'Grecia', 'Fabiola', 'Ana Karen', 'Luz', 'Ana Isabel', 'Yesenia', 'Karla', 'Lidia', 'Rita', 'Fernanda', 'Adela', 'Nadia', 'Dolores', 'Rocio', 'Lilia', 'Ana Laura', 'Marina', 'Daniela', 'Viviana', 'Angelina', 'Bianca', 'Eugenia', 'hijo', 'hija', 'hijos', 'marido', 'esposa', 'novia', 'novio', 'tio', 'tia', 'niños', 'niña', 'niña', 'abuelita', 'abuela', 'abuelo', 'suegro', 'suegra', 'yerno', 'nuera', 'hermanastro', 'hermanastra', 'papa', 'mama', 'madre', 'padre', 'padrastro', 'madrastra', 'bisabuela', 'cuñado', 'cuñada','abuelito', 'yerno', 'sobrino', 'sobrina', 'cuñado', 'cuñada', 'Juan', 'José', 'Antonio', 'Jesús', 'Francisco', 'Manuel', 'Miguel', 'David', 'Pedro', 'Carlos', 'Daniel', 'Luis', 'Rafael', 'Alejandro', 'Roberto', 'Jorge', 'Fernando', 'Javier', 'Enrique', 'Alberto', 'Ricardo', 'Guillermo', 'Héctor', 'Mario', 'Ernesto', 'Ignacio', 'Eduardo', 'Gabriel', 'Andrés', 'Arturo', 'Armando', 'Sergio', 'Salvador', 'Oscar', 'Israel', 'Emilio', 'Juan Carlos', 'Adrián', 'Gustavo', 'Víctor', 'Raúl', 'Leonardo', 'César', 'Julio', 'Benjamín', 'José Luis', 'Ismael', 'Samuel', 'Mauricio', 'Mariano', 'Agustín', 'Gerardo', 'Abraham', 'Albert', 'Octavio', 'Alfredo', 'Joel', 'Joaquín', 'Diego', 'Jairo', 'Alonso', 'Edgar', 'Felipe', 'Lorenzo', 'José Manuel', 'Máximo', 'Milton', 'Rodrigo', 'Cristóbal', 'Camilo', 'Humberto', 'Pablo', 'Santiago', 'Marcos', 'Rubén', 'Cándido', 'René', 'Nicolás', 'Josué', 'Isidro', 'Federico', 'Ángel', 'José Antonio', 'Renato', 'Efraín', 'Jaime', 'Luis Carlos', 'Ulises', 'Moses', 'Óscar', 'Rogelio', 'Xavier', 'Adán', 'Julián', 'Fabián', 'Jesús', 'Evelyn', 'Yolanda']

# Banco de palabras para generar nombres de gastos_fijos_imp
nombres_fijos_imp=[
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
    '{palabra}',
    'Pago de {palabra}',
    'Gasto fijo de {palabra}',
    'Pago {palabra}',
    '{palabra} {nombre}',
    '{palabra} {nombre} {mes}',
    '{palabra} de {nombre}',
    'Gasto de {palabra} de {nombre}',
    'Pago de {palabra} de {nombre}',
    'Gasto {palabra} {nombre}',
    'Pago {palabra} {nombre}',
    '{nombre} {mes}',
    '{palabra}, {mes}',
    '{palabra}, {nombre}',
    'Factura de {palabra}',
    'Factura de {palabra} {mes}',
]

# Banco de frases para generar descripciones de gastos_fijos_imp
descripciones_fijos_imp = [
    'Pago de {palabra} del mes de {mes}',
    'Pago de {palabra} del mes',
    'Gasto de {palabra}',
    'Gasto de {palabra} del mes de {mes}',
    'Gasto de {palabra} del mes',
    'Gasto de {palabra} de {nombre} {mes}',
    'Gasto de {palabra} de {nombre} {mes}',
    'Pago mensual de {palabra}',
    'Pago quincenal de {palabra}',
    'Pago semanal de {palabra}',
    'Pago trimestral de {palabra}',
    'Pago bimestral de {palabra}',
    'Pago semestral de {palabra}',
    'Pago anual de {palabra}',
    'Gasto mensual de {palabra}',
    'Gasto quincenal de {palabra}',
    'Gasto semanal de {palabra}',
    'Gasto trimestral de {palabra}',
    'Gasto semestral de {palabra}',
    'Gasto bimestral de {palabra}',
    'Gasto anual de {palabra}',
    'Mensualidad de {palabra}',
    'Anualidad de {palabra}',
    'Semestralidad de {palabra}',
    'Tarifa de {palabra}',
    'Factura de {palabra} de {nombre}',
    'Cuota de {palabra}',
    'Pago de {palabra} de {nombre}',
    'Gasto de {palabra} de {nombre}',
    'Pago {nombre}',
    'Gasto {nombre}',
    'Pago {mes}',
    'Gasto {mes}',
    'Este es el pago de {palabra} correspondiente al mes de {mes}',
    'Este es el pago de {palabra} correspondiente al mes',
    'Este es el pago de {palabra} correspondiente al mes de {mes} de {nombre}',
    'Este gasto corresponde a {palabra} del mes de {mes}',
    'Este gasto corresponde a {palabra} del mes, {nombre}',
    'Cuota mensual de {palabra}',
    'Cuota quincenal de {palabra}',
    'Cuota semanal de {palabra}',
    'Cuota trimestral de {palabra}',
    'Cuota bimestral de {palabra}',
    'Cuota semestral de {palabra}',
    'Cuota {palabra}',
    'Factura de {palabra} de {nombre} {mes}',
    'Cuota anual de {palabra}',
    'Dinero para {palabra}',
    'Dinero para el pago de {palabra}',
    'Dinero para el pago de {palabra} del mes de {mes}',
]

# crear libro y hoja de trabajo
libro = openpyxl.Workbook()
hoja = libro.active

# establecer nombre de la hoja
hoja.title = "fijos_imp"

# escribir datos en las hojas
hoja['A1'] = "name"
hoja['B1'] = "description"
hoja['C1'] = "amount"

for i in range(10000):
    name=random.choice(nombres_fijos_imp)
    palabra = random.choice(palabras_fijos_imp)
    name=name.replace('{palabra}', palabra)
    name=name.replace('{nombre}', random.choice(nombres))
    name=name.replace('{mes}', random.choice(meses))
    # establecer el contenido de la celda
    celda = 'A{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja[celda] = name
    
    # generar la descripción
    palabra_encontrada = False
    while not palabra_encontrada:
        description=random.choice(descripciones_fijos_imp)
        descripcion_palabra = random.choice(palabras_fijos_imp)
        description=description.replace('{palabra}', descripcion_palabra)
        description=description.replace('{nombre}', random.choice(nombres))
        description=description.replace('{mes}', random.choice(meses))
        if palabra in description:
            palabra_encontrada = True
        # establecer el contenido de la celda
        celda = 'B{}'.format(i+2)  # aumentar el índice de fila para cada iteración
        hoja[celda] = description
    
    amount=random.randint(100, 10000)
    # establecer el contenido de la celda
    celda = 'C{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja[celda] = amount

# Guardar el archivo xlsx
libro.save('data_synthetic_baro.xlsx')

