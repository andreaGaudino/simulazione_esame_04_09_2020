import copy
import random

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self, rank):
        self.graph.clear()
        nodi = DAO.getNodi()
        for n in nodi:
            self.graph.add_node(n)
            self.idMap[n.id] = n
        archi = DAO.getArchi(rank)
        for a in archi:
            self.graph.add_edge(self.idMap[a[0]], self.idMap[a[1]], weight = a[2])

    def calcolaGradoMassimo(self):
        dizio = {}
        for n in self.graph.nodes:
            somma = 0
            vicini = self.graph.neighbors(n)
            for v in vicini:
                somma += self.graph[n][v]["weight"]
            dizio[n] = somma
        sortato = sorted(dizio, key=lambda x: dizio[x] , reverse=True)
        return sortato[0], dizio[sortato[0]]

    def calcolaCammino(self, film):
        self.solBest = []
        parziale = [film]
        self.ricorsione(parziale)
        print(len(self.solBest))
        return self.solBest

    def ricorsione(self, parziale):
        vicini = list(self.graph.neighbors(parziale[-1]))
        viciniAmmissibili = self.getAmmissibili(parziale, vicini)
        if len(viciniAmmissibili) == 0:
            if len(parziale) == 1:
                return
            if len(self.solBest) < len(parziale):
                self.solBest = copy.deepcopy(parziale)
        else:
            for v in viciniAmmissibili:
                parziale.append(v)
                self.ricorsione(parziale)
                parziale.pop()



    def getAmmissibili(self, parziale, vicini):
        ammissibili = []
        if len(parziale) == 1:
            ammissibili = copy.deepcopy(vicini)
        else:
            for v in vicini:
                if v not in parziale and self.graph[parziale[-2]][parziale[-1]]["weight"] <= self.graph[parziale[-1]][v]["weight"]:
                    ammissibili.append(v)
        return ammissibili


    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)