from dataclasses import dataclass


@dataclass
class Corso:
    codins : str = ""
    crediti : int = 0
    nome : str = ""
    pd: int = 0

    matricole : set = None
    studenti : set = None

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def get_matricole_corso(self):
        return self.matricole

    def get_studenti_corso(self):
        return self.studenti

