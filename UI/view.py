import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):
        # title
        self._title = ft.Text("simulazione esame 04/09/2020", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1
        self.txtRank = ft.TextField(label="Rank")
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([ft.Container(self.txtRank, width=300),
                       ft.Container(self.btnCreaGrafo, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        #row 2
        self.btnFilmGradoMassimo = ft.ElevatedButton(text="Film di grado massimo", on_click=self._controller.handleGradoMassimo, disabled=True)
        row2 = ft.Row([
                       ft.Container(self.btnFilmGradoMassimo, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        #row3
        self.ddFilm = ft.Dropdown(label="Film")
        self.btnCammino = ft.ElevatedButton(text="Cammino incrementale", on_click=self._controller.handleCalcolaCammino)
        row3 = ft.Row([ft.Container(self.ddFilm, width=300),
                       ft.Container(self.btnCammino, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

        self.txtGrafo = ft.ListView(expand=1)
        self.txtGradoMax = ft.ListView(expand=1)
        self.txtRicorsione = ft.ListView(expand=1)

        self._page.add(self.txtGrafo)
        self._page.add(self.txtGradoMax)
        self._page.add(self.txtRicorsione)
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
