from random import randint

class PacoteEthernet(object):
	header = 14
	areaDados = 0
	trailer = 4

	def __init__(self):
		self.areaDados = randint(46, 1500)

	def setAreaDados(self, tamanho):
		self.areaDados = tamanho

	def tamanhoTotal(self):
		return self.header + self.areaDados + self.trailer
