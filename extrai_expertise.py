import os
import sys
from leitor_diretorios import LeitorDiretorio
from autoria import *
from autoria_commit import *


def gera_csv(mapa_expertise, nome_arquivo):
    linhas = ''
    for (classe, contrib) in sorted(mapa_expertise.items()):
        for desenvolvedor in sorted(contrib, key=contrib.get, reverse=True):
            linhas += "{0}, {1}, {2}\n".format(classe, desenvolvedor, mapa_expertise[classe][desenvolvedor])
    arquivo_saida = open(nome_arquivo, 'w')
    arquivo_saida.writelines(linhas)
    arquivo_saida.close()

def salva_arquivo(nome_arquivo, conteudo):
	arquivo_saida = open(nome_arquivo, 'w')
	arquivo_saida.writelines(conteudo)
	arquivo_saida.close()

def prepara_ambiente():
    try:
        os.mkdir('csv')
    except:
        pass


if __name__ == "__main__":
    prepara_ambiente()
    leitor = LeitorDiretorio()
    classes = leitor.le_arquivos_java('../.')

    cvs_suportados = ["hg"]
    controle_versao = sys.argv[1]

    if (controle_versao not in cvs_suportados):
        print "Informe o controle de versao corretamente!"
        print "Os seguintes controles de versoes sao suportados: " + ", ".join(cvs_suportados)
        sys.exit(0)

    autoria = AutoriaPorLoc(classes, controle_versao)
    mapa_expertise = autoria.calcula_autoria()
    gera_csv(mapa_expertise, 'csv/contribuicao_linha.csv')

    autoria = AutoriaPorCommit(classes, controle_versao)
    mapa_expertise = autoria.calcula_autoria()
    gera_csv(mapa_expertise, 'csv/contribuicao_commit.csv')


	
