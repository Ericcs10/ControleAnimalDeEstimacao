from enum import Enum


class Intervalo(str, Enum):
    
    DIAS = "Dias"
    MESES = "Meses"
    ANOS = "Anos"


class Sexo(str, Enum):

    FEMININO = "Feminino"
    MASCULINO = "Masculino"
    OUTRO = "Outro"


class Especie(str, Enum):

    CANINO = "Canino"
    FELINO = "Felino"
    AVE = "Ave"
    ROEDOR = "Roedor"
