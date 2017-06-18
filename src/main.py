#coding: utf-8
from classes.packEthernet import PacoteEthernet
from classes.packWifi import PacoteWifi

from random import randint

bandaNominal = 0.0
bandaReal = 54.0
transmissao = 10000
taxaErro = 20
listaPacotes = []

bytesInfo = 0.0
bytesTotal = 0.0
pacotesRecebidos = 0
erroEnvio = 0

print

#1 == Ethernet, 2 == Wifi
def selecionarTipoRede():
	while(True):
		print "Insira o tipo de pacote a ser utilizado [1 - Ethernet / 2 - Wifi]: "
		opcao = input()

		if(opcao == 1):
			print "Ethernet selecionado! "
			print
			break
		elif(opcao == 2):
			print "Wifi selecionado!"
			print
			break
		else:
			print "Opção inválida! Tente novamente."

		print

	return opcao

def erroPacote(taxaErro):
	num = randint(0, 100)

	if num < taxaErro:
		return True
	else:
		return False

def criarPacote(quant, lista, tipo):
	for i in range(quant):
		if(tipo == 1):
			pacote = PacoteEthernet()
		else:
			pacote = PacoteWifi()

		lista.append(pacote)

	return lista

tipo = selecionarTipoRede()

if(tipo == 1):
	bandaNominal = 100.0
else:
	bandaNominal = 54.0

criarPacote(transmissao, listaPacotes, tipo)

for i in range(transmissao):
	erro = erroPacote(taxaErro)

	while(erro == True):
		bytesTotal += listaPacotes[i].tamanhoTotal()
		erro = erroPacote(taxaErro)

		if(erro == False):
			erroEnvio += 1

	bytesTotal += listaPacotes[i].tamanhoTotal()
	bytesInfo += listaPacotes[i].areaDados

pacotesRecebidos = transmissao - erroEnvio

print "Banda Real: ", str(bandaReal)
print "Banda Nominal: ", str(bandaNominal)
print "Pacotes Recebidos: ", str(pacotesRecebidos)
print "Pacotes Enviados: ", str(transmissao)
print "Bytes de Informação: ", str(bytesInfo)
print "Bytes Totais: ", str(bytesTotal)

vazao = round(((bandaReal/bandaNominal) * (float(pacotesRecebidos)/float(transmissao)) * (bytesInfo/bytesTotal)), 4)

print
print "Vazão: ", str(vazao * 100), "%"
