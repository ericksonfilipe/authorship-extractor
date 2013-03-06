# -*- coding: utf-8 -*-
import os
import sys
from subprocess import Popen, PIPE
from contributors import Contributors
from controle_versao import *


class AutoriaPorLoc:
    
    def __init__(self, classes, sistema_controle_versao):
        self.contribuidores = Contributors()
        self.classes = classes
        self.sistema_controle_versao = sistema_controle_versao
        self.expertise_desenvolvedores_classe = {}
        self.contribuidores_atuais = []

    def calcula_autoria_por_classe(self, path):
        saida = eval("{0}('{1}')".format(self.sistema_controle_versao, path))
        linhas = saida.read().split('\n')
        loc = 0
        autoria = {}
        for linha in linhas:
            if is_valid(linha):
                usuario = self.contribuidores.get_identificador(linha.split(':')[0].strip())
                if usuario not in self.contribuidores_atuais:
                    self.contribuidores_atuais.append(usuario)

                loc += 1
                if usuario not in autoria.keys():
                    autoria[usuario] = 1
                else:
                    autoria[usuario] += 1

        for (usuario, quantidade) in autoria.items():
            autoria[usuario] = (quantidade / float(loc)) * 100
        return autoria

    def calcula_autoria(self):
        for classe in self.classes:
            self.expertise_desenvolvedores_classe[classe] = self.calcula_autoria_por_classe(classe)
        return self.expertise_desenvolvedores_classe

def is_valid(linha):
    return not (linha == '\n' or
            len(linha.split(':')) < 2 or
            linha.split(':')[1].isspace() or 
            linha.split(':')[1].strip().startswith('//') or 
            linha.split(':')[1].strip().startswith('import') or
            linha.split(':')[1].strip().startswith('package'))


