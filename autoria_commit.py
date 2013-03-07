# -*- coding: utf-8 -*-
import os
import sys
from contribuidores import Contribuidores
from controle_versao import *

class AutoriaPorCommit:

    def __init__(self, classes, sistema_controle_versao):
        self.contribuidores = Contribuidores()
        self.classes = classes
        self.sistema_controle_versao = sistema_controle_versao
        self.expertise_desenvolvedores_classe = {}
        self.contribuidores_atuais = []

    def calcula_autoria_por_classe(self, classe):
        saida = eval("{0}_commit('{1}')".format(self.sistema_controle_versao, classe))
        autoria = {}
        for usuario in saida:
            usuario = self.contribuidores.get_identificador(usuario)
            if usuario not in self.contribuidores_atuais:
                self.contribuidores_atuais.append(usuario)

            if usuario not in autoria.keys():
                autoria[usuario] = 100./len(saida)
            else:
                autoria[usuario] += 100./len(saida)
        return autoria

    def calcula_autoria(self):
        for classe in self.classes:
            self.expertise_desenvolvedores_classe[classe] = self.calcula_autoria_por_classe(classe)
        return self.expertise_desenvolvedores_classe
