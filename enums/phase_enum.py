from enum import Enum

class Phase(str, Enum):
    CAIXA_DE_ENTRADA = "323403002"
    FAZENDO = "323403003"
    CONCLUIDO = "323403004"

    @property
    def nome(self):
        nomes = {
            Phase.CAIXA_DE_ENTRADA: "Caixa de entrada",
            Phase.FAZENDO: "Fazendo",
            Phase.CONCLUIDO: "Concluído",
        }
        return nomes[self]