from database.corsoDAO import CorsoDao
class Model:

    def __init__(self):
        self.corsi = CorsoDao.get_all_corsi()

    def get_corsi_periodo(self, pd):
        # soluzione con filtro periodo fatto nella query
        #return CorsoDao.get_corsi_periodo(pd)

        # soluzione con filtro periodo fatto da python (prendi tutti i corsi salvati e seleziono solo quelli del periodo selezionato)
        corsi_periodo = []
        for corso in self.corsi:
            if corso.pd == pd:
                corsi_periodo.append(corso)
        return corsi_periodo

    def get_numero_studenti_periodo(self, pd):
        # soluzione con filtro fatto nella query (con join tabelle)
        #return CorsoDao.get_studenti_periodo(pd)

        # soluzione con filtro periodo fatto da python
        matricole_iscritti = set()
        for corso in self.corsi:
            if corso.pd == pd:
                if corso.matricole is None:
                    corso.matricole = CorsoDao.get_matricole_corso(corso.codins)
                matricole_iscritti = matricole_iscritti.union(corso.matricole)
        return len(matricole_iscritti)

    def get_studenti_corso(self, codins):
        return CorsoDao.get_studenti_corso(codins)
