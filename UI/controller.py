import flet as ft
from UI import view


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None

    def leggi_tendina(self, e):
        self._pd = int(self._view.dd_periodo.value) # oppure e.control.value


    def get_corsi_periodo(self, e):

        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico!")
            return

        corsi = self._model.get_corsi_periodo(self._pd)

        self._view.lst_result.controls.clear()
        for corso in corsi:
            self._view.lst_result.controls.append(ft.Text(corso))

        self._view.update_page()


    def get_numero_studenti_periodo(self, e):

        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico!")
            return

        numero_studenti = self._model.get_numero_studenti_periodo(self._pd)

        self._view.lst_result.controls.clear()

        self._view.lst_result.controls.append(ft.Text(f"Gli studenti iscritti a corsi del periodo didattico {self._pd} sono: {numero_studenti}"))

        self._view.update_page()

    def get_studenti_corso(self, e):

        if self._view.txt_codice_corso.value is None:
            self._view.create_alert("Inserire il codice di un corso!")
            return

        studenti_corso = self._model.get_studenti_corso(self._view.txt_codice_corso.value)

        self._view.lst_result.controls.clear()

        self._view.lst_result.controls.append(
            ft.Text(f"Elenco degli studenti iscritti al corso selezionato:"))

        for studente in studenti_corso:
            self._view.lst_result.controls.append(ft.Text(studente))

        self._view.update_page()


    def get_dettaglio_corso(self, e):
        pass

