import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esercizio gestore corso"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_periodo = None
        self.btn_corsi_periodo = None
        self.btn_studenti_periodo = None
        self.txt_codice_corso = None
        self.btn_studenti_corso = None
        self.btn_dettaglio_corso = None
        self.lst_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Gestore corsi", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls

        self.dd_periodo = ft.Dropdown(label="Periodo didattico", options=[ft.dropdown.Option(key="1"), ft.dropdown.Option(key="2")], width=130, hint_text="Selezionare il periodo didattico", on_change=self._controller.leggi_tendina)
        self.btn_corsi_periodo = ft.ElevatedButton(text="Corsi periodo", tooltip="Metodo per stampare i corsi del periodo didattico selezionato", width=200, on_click=self._controller.get_corsi_periodo)
        self.btn_studenti_periodo = ft.ElevatedButton(text="Studenti periodo", tooltip="Metodo per stampare tutti gli studenti iscritti ai corsi del periodo didattico", width=200, on_click=self._controller.get_numero_studenti_periodo)

        row1 = ft.Row(controls=[self.dd_periodo, self.btn_corsi_periodo, self.btn_studenti_periodo], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.txt_codice_corso = ft.TextField(label="Codice corso", width=170, hint_text="Inserire il codice di un corso" )
        self.btn_studenti_corso = ft.ElevatedButton(text="Studenti corso", tooltip="Metodo per stampare tutti gli studenti iscritti al corso selezionato", width=200, on_click=self._controller.get_studenti_corso)
        self.btn_dettaglio_corso = ft.ElevatedButton(text="Dettagli studenti corso", tooltip="Metodo per stampare il dettaglio degli studenti iscritti al corso selezionato", width=200, on_click=self._controller.get_dettaglio_corso)

        row2 = ft.Row(controls=[self.txt_codice_corso, self.btn_studenti_corso, self.btn_dettaglio_corso], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lst_result)


        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
