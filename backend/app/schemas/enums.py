from enum import Enum

class Sexo(str, Enum):
    FEMININO = "FEMININO"
    MASCULINO = "MASCULINO"
    OUTRO = "OUTRO"

class Especie(str, Enum):
    CAO = "CÃO"
    FELINO = "FELINO"
    AVE = "AVE"
    ROEDOR = "ROEDOR"

class Intervalo(str, Enum):
    DIAS = "DIAS"
    MESES = "MESES"
    ANOS = "ANOS"
