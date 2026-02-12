from enum import Enum

class Cidade(str, Enum):
    MARACANAU = "850256388"
    MARANGUAPE = "850256601"
    EUSEBIO = "850256710"
    CAUCAIA = "850256822"
    FORTALEZA = "850256930"

    @property
    def nome(self):
        nomes = {
            Cidade.MARACANAU: "Maracanaú",
            Cidade.MARANGUAPE: "Maranguape",
            Cidade.EUSEBIO: "Eusébio",
            Cidade.CAUCAIA: "Caucaia",
            Cidade.FORTALEZA: "Fortaleza",
        }
        return nomes[self]
