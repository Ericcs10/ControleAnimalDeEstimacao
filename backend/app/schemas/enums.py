from enum import Enum


class Intervalo(str, Enum):
    """Intervalo de tempo para revacinação."""
    DIAS = "Dias"
    MESES = "Meses"
    ANOS = "Anos"


class Sexo(str, Enum):
    """Sexo do animal."""
    FEMININO = "Feminino"
    MASCULINO = "Masculino"
    OUTRO = "Outro"


class Especie(str, Enum):
    """Espécie do animal."""
    CANINO = "Canino"
    FELINO = "Felino"
    AVE = "Ave"
    ROEDOR = "Roedor"
