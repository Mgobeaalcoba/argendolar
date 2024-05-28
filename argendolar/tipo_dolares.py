# Enum class for the type of dollars
from enum import Enum


class TipoDivisas(Enum):
    OFICIAL = 'oficial'
    BLUE = 'blue'
    MEP = 'bolsa'
    MAYORISTA = 'mayorista'
    SOLIDARIO = 'solidario'
    TURISTA = 'turista'