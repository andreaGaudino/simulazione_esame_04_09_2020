import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.film = None


    def handleCreaGrafo(self, e):
        rank = self._view.txtRank.value
        if rank == "":
            self._view.create_alert("Rank non inserito")
            return
        try:
            rankFloat = float(rank)
        except ValueError:
            self._view.create_alert("Rank inserito non numerico")
            return
        self._model.buildGraph(rankFloat)
        n,e = self._model.graphDetails()
        self._view.txtGrafo.clean()
        self._view.txtGrafo.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self._view.btnFilmGradoMassimo.disabled = False
        self.fillDD(list(self._model.graph.nodes))
        self._view.update_page()
        print()

    def handleGradoMassimo(self, e):
        film, count = self._model.calcolaGradoMassimo()
        self._view.txtGradoMax.clean()
        self._view.txtGradoMax.controls.append(ft.Text(f"Il film con grado maggiore è {film} con grado {count}"))
        self._view.update_page()

    def handleCalcolaCammino(self, e):
        if self.film is None:
            self._view.create_alert("Film non inserito")
            return

        solBest = self._model.calcolaCammino(self.film)
        self._view.txtRicorsione.clean()
        self._view.txtRicorsione.controls.append(ft.Text(f"Cammino con lunghezza {len(solBest)-1}"))
        for i in range(len(solBest)-1):
            self._view.txtRicorsione.controls.append(ft.Text(f"{solBest[i]} --> {solBest[i+1]} peso {self._model.graph[solBest[i]][solBest[i+1]]["weight"]}"))
        self._view.update_page()

    def fillDD(self, nodi):
        nodiDD = list(map(lambda x: ft.dropdown.Option(key=x, on_click=self.getFilm), nodi))
        self._view.ddFilm.options = nodiDD
        self._view.update_page()


    def getFilm(self, e):
        if e.control.key is None:
            pass
        else:
            self.film = e.control.key


           