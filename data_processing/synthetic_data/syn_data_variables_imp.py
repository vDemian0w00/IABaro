import random
import openpyxl

# comida
palabras_producto_vi = ['comida', 'aguacate', 'ajo', 'albahaca', 'arándanos', 'atún', 'avena', 'brócoli', 'calabaza', 'camarones', 'carne de res', 'cebolla', 'cereales', 'champiñones', 'chía', 'ciruelas', 'coco', 'espinacas', 'frijoles', 'galletas', 'garbanzos', 'granola', 'huevo', 'kiwi', 'lechuga', 'limones', 'lentejas', 'mandarina', 'mango', 'manzanas', 'manzana', 'naranja', 'nueces', 'palta', 'papaya', 'pepinos', 'pepino', 'pepitas', 'pescado', 'piña', 'pimiento', 'plátanos', 'queso', 'quinoa', 'sandía', 'semillas de girasol', 'tomates', 'uvas', 'zanahorias', 'caja de huevos', 'carne', 'mayonesa', 'mermelada', 'crema', 'alimentos enlatados', 'frijoles bayos', 'frijoles', 'arroz', 'pasta', 'salsa', 'salsa de tomate', 'salsa de soya', 'té', 'pollo', 'cerdo', 'carne de cerdo', 'carne de pollo', 'yogurt', 'harina para hot cakes', 'papel de baño', 'jabon', 'shampoo', 'toallas', 'toalla', 'toalla de papel', 'toallas sanitarias', 'kotex', 'leche', 'suavitel', 'cloro', 'cloralex', 'escoba', 'trapeador', 'detergente', 'computadora', 'pc', 'productos de limpieza', 'compra del super', 'cepillo de dientes', 'fruta', 'verdura', 'frutas', 'verduras', 'comida escuela', 'desayuno', 'cena', 'lunch', 'almuerzo', 'pollo rostizado', 'pizza', 'hamburguesa', 'helado', 'tacos', 'tortillas', 'tortillas de maiz', 'garrafones', 'garragon de agua', 'agua embotellada', 'botella de agua', 'mueble', 'cama', 'muebles','silla', 'mesa', 'refrigerador', 'television', 'secadora', 'lavaplatos', 'ventilador', 'estufa', 'horno', 'microondas', 'platos', 'cubiertos', 'cocina', 'comedor', 'purificador de agua', 'palomitas', 'almohada']

#servicios
palabras_servicio_vi=['mudanza', 'cambio de casa',]

# ropa
palabras_ropa_vi=['camisa', 'playera', 'blusa', 'tennis', 'zapatos', 'abrigo', 'pantalon', 'tenis', 'gorra', 'jeans', 'traje', 'sudadera', 'chamarra', 'calzones', 'trusa', 'ropa interior', 'brassier', 'brasier', 'zapatillas', 'pijama', 'falda', 'vestido']

# transporte
palabras_transporte_vi=['metro', 'metrobus', 'combi', 'trolebus', 'mexibus', 'tren', 'camion', 'cablebus', 'bicitaxi', 'taxi', 'suburbano', 'microbus', 'micro', 'tren ligero', 'colectivo', 'uber', 'didi', 'taxi', 'renta de bici', 'bici', 'Lyft', 'lyft', 'trolebús','mexibús', 'bus', 'microbús', 'grab', 'cabify', '']

# dias
dias=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

nombres=['hijo', 'hija', 'hijos', 'marido', 'esposa', 'novia', 'novio', 'tio', 'tia', 'niños', 'niña', 'niña', 'abuelita', 'abuela', 'abuelo', 'suegro', 'suegra', 'yerno', 'nuera', 'hermanastro', 'hermanastra', 'papa', 'mama', 'madre', 'padre', 'padrastro', 'madrastra', 'bisabuela', 'cuñado', 'cuñada','abuelito', 'yerno', 'sobrino', 'sobrina', 'cuñado', 'cuñada', 'alma', 'bruno', 'carla', 'dante', 'elena', 'fernando', 'gabriela', 'hugo', 'ignacio', 'jazmín', 'karla', 'luis', 'mariana', 'nadia', 'oscar', 'paola', 'quetzal', 'ricardo', 'sofía', 'tania', 'ulises', 'valentina', 'ximena', 'yael', 'zoe',  'andrea', 'benjamin', 'camila', 'david', 'elisa', 'felipe', 'gabriel', 'hector', 'isabella', 'juan', 'karen', 'laura', 'marcela', 'natalia', 'orlando', 'pablo', 'quevedo', 'rosa', 'samuel', 'tomas', 'ursula', 'victoria', 'wilder', 'ximena', 'yahir', 'zara', 'adriana', 'bernardo', 'claudia', 'diana', 'emilio', 'francisco', 'graciela', 'isaac', 'javier', 'karen', 'luisa', 'manuel', 'nataly', 'omar', 'paulette', 'quintín', 'rosalía', 'sergio', 'tadeo', 'ursula', 'viviana', 'wenceslao', 'xóchitl', 'yahir', 'zenón', 'ana', 'bernarda', 'carlos', 'diego', 'esteban', 'fanny', 'gimena', 'hernando', 'isidora', 'jimena', 'karina', 'leonor', 'mauricio', 'nicolás', 'oswaldo', 'pilar', 'quintín', 'rafael', 'santiago', 'tadeo', 'ursula', 'vicente', 'wanda', 'xavier', 'yuliana', 'zulma']

# Banco de palabras para generar nombres de gastos_variables_imp
nombres_variables_imp = [
    'Gasto {producto}',
    '{producto}',
    'Pago de {producto}',
    'Gasto de {producto}',
    'Pago {producto}',
    'Compra de {producto}',
    'Dinero para {producto}',
    'Compra {producto}',
    'Compra de {producto}',
    '{producto} {dia}',
    '{producto} {nombre}',
    '{producto} {nombre} {dia}',
    'Compra de {producto} {dia}',
    'Gasto de {producto} del {dia}',
    'Pago de {producto} del {dia}',
    'Gasto {ropa}',
    '{ropa}',
    'Pago de {ropa}',
    'Gasto de {ropa}',
    'Pago {ropa}',
    'Compra de {ropa}',
    'Dinero para {ropa}',
    'Regalo {ropa}',
    'Regalo {ropa} para {nombre}',
    '{ropa} {dia}',
    'Gasto {transporte}',
    '{transporte}',
    'Pago de {transporte}',
    'Gasto de {transporte}',
    'Pago {transporte}',
    'Compra de {transporte}',
    'Dinero para {transporte}',
    '{transporte} {dia}',
    'Gasto {servicio}',
    '{servicio}',
    'Pago de {servicio}',
    'Gasto de {servicio}',
    'Pago {servicio}',
    'Dinero para {servicio}',
    '{servicio} {dia}',
    '{servicio} {nombre}',
]

# Banco de frases para generar descripciones de gastos_variables_imp
descripciones_variables_imp = [
    'Pago de {producto} del {dia}',
    'Pago de {producto} del {dia} para {nombre}',
    'Pago de {producto} {dia}, {nombre}',
    'Gasto de {producto} del {dia}',
    'Gasto de {producto} del {dia} para {nombre}',
    'Gasto {producto} para el dia {dia}',
    'Llevar {producto} a {nombre}',
    'Llevar {producto} a {nombre} el {dia}',
    'Levar {producto} el {dia}',
    'Devolver {producto}',
    'Pago de {ropa}',
    'Pago de {ropa} para {nombre}',
    'Regalo de {ropa} para {nombre} el {dia}',
    'Regalo de {ropa} para {nombre}',
    'Gasto de {ropa}',
    'Gasto de {ropa} para {nombre}',
    'Pago de {transporte} del {dia}',
    'Gasto de {transporte} del {dia}',
    'Gasto de {servicio} del dia {dia}',
    'Pago de {servicio} del dia {dia}',
    'La actividad {servicio} fue realizada el dia {dia}',
]

# abrir el archivo xlsx
libro = openpyxl.load_workbook('data_synthetic_baro.xlsx')

# crear hoja de trabajo
hoja3 = libro.create_sheet("variables_imp")

# escribir datos en las hojas
hoja3['A1'] = "name"
hoja3['B1'] = "description"
hoja3['C1'] = "amount"

for i in range(10000):
    palabra_encontrada = False
    while not palabra_encontrada:
        name = random.choice(nombres_variables_imp)
        producto = random.choice(palabras_producto_vi)
        ropa = random.choice(palabras_ropa_vi)
        transporte = random.choice(palabras_transporte_vi)
        servicio=random.choice(palabras_servicio_vi)
        name = name.replace('{producto}', producto)
        name = name.replace('{ropa}', ropa)
        name = name.replace('{transporte}', transporte)
        name = name.replace('{servicio}', servicio)
        name = name.replace('{nombre}', random.choice(nombres))
        name = name.replace('{dia}', random.choice(dias))

        descripcion_producto = random.choice(palabras_producto_vi)
        descripcion_ropa = random.choice(palabras_ropa_vi)
        descripcion_transporte = random.choice(palabras_transporte_vi)
        descripcion_servicio=random.choice(palabras_servicio_vi)
        descripcion_palabras = [
            descripcion_producto,
            descripcion_ropa,
            descripcion_transporte,
            descripcion_servicio,
        ]
        random.shuffle(descripcion_palabras)
        for descripcion_palabra in descripcion_palabras:
            description = random.choice(descripciones_variables_imp)
            description = description.replace('{producto}', descripcion_producto)
            description = description.replace('{ropa}', descripcion_ropa)
            description = description.replace('{transporte}', descripcion_transporte)
            description = description.replace('{servicio}',descripcion_servicio)
            description = description.replace('{nombre}', random.choice(nombres))
            description = description.replace('{dia}', random.choice(dias))

            if descripcion_palabra in name and descripcion_palabra in description:
                palabra_encontrada = True
                break

    # establecer el contenido de las celdas
    celda_name = 'A{}'.format(i+2)
    hoja3[celda_name] = name
    celda_description = 'B{}'.format(i+2)
    hoja3[celda_description] = description
    
    amount = random.randint(100, 10000)
    # establecer el contenido de la celda
    celda = 'C{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja3[celda] = amount

# Guardar el archivo xlsx
libro.save('data_synthetic_baro.xlsx')