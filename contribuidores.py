class Contribuidores:
    def __init__(self):
        self.contribuidores = {}

        arquivo = open('contribuidores.csv')
        linhas = arquivo.readlines()

        for linha in linhas:
            linha = linha.replace(', ', ',').strip().split(',')
            identificador = linha.pop()
            if len(linha) == 0:
                if identificador.strip() == '':
                    continue
                self.contribuidores[identificador] = identificador
            else:
                outros_identificadores = ("('" + "','".join(linha) + "')")
                outros_identificadores = eval(outros_identificadores)
                self.contribuidores[outros_identificadores] = identificador

    def get_identificador(self, usuario):
        for nomes in self.contribuidores.keys():
            if usuario in nomes:
                return self.contribuidores[nomes]
        return usuario
