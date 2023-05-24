# type Periodo = 'Semanal' | 'Quincenal' | 'Mensual' | 'Bimestral' | 'Trimestral'

# type Frecuente = {
#   freId: number
#   freName: string
#   freDescription: string
#   freAmount: number
#   freLapse: Periodo
#   freIsStatic: boolean
#   day: Day
# }

# type Day = {
#   dayId: number
#   dayDate: string

# }

# type Diario = {
#   diaId: number
#   diaName: string
#   diaDescription: string
#   diaAmount: number
#   diaIcon: number
#   diaCategory: null
#   day: Day
# }
# `
# type Main = {
#   frecuentes: Frecuente[]
#   diarios: Diario[]
# }

# CONVERT INTO CLASSES

class Periodo(enumerate):
    SEMANAL = 1
    QUINCENAL = 2
    MENSUAL = 3
    BIMESTRAL = 4
    TRIMESTRAL = 5

class Day:
    def __init__(self, dayId: int, dayDate: str):
        self.dayId = dayId
        self.dayDate = dayDate

class Frecuente:
    def __init__(self, freId: int, freName: str, freDescription: str, freAmount: float, freLapse: Periodo, freIsStatic: bool, day: Day):
        self.freId = freId
        self.freName = freName
        self.freDescription = freDescription
        self.freAmount = freAmount
        self.freLapse = freLapse
        self.freIsStatic = freIsStatic
        self.day = day