from random import randint

class PacoteWifi(object):
    header = 38
    areaDados = 0
    trailer = 16

    def __init__(self):
        self.areaDados = randint(46, 2312)

    def setAreaDados(self, tamanho):
        self.areaDados = tamanho

    def tamanhoTotal(self):
        return self.header + self.areaDados + self.trailer
