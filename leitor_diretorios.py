import os

class LeitorDiretorio:

    def __init__(self):
        pass

    def le_arquivos_recursivo(self, diretorio, extensao):
        listing = os.listdir(diretorio)
        arquivos = []
        for infile in listing:
            caminho_arquivo = diretorio + '/' + infile
            try:
                a = self.le_arquivos_recursivo(caminho_arquivo, extensao)
                for arq in a:
                    arquivos.append(arq)
            except:
                if (infile.split('.')[-1] == extensao):
                    arquivos.append(caminho_arquivo)
        return arquivos

    def le_arquivos_java(self, diretorio):
        return self.le_arquivos_recursivo(diretorio, 'java')
	    
