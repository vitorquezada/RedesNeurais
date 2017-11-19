import numpy as np
import random as r

class Perceptron:
    Bias = r.random()
    TaxaDeAprendizado = 1
    def __init__(self, numEntradas, numSaidas):
        self.Entradas = np.ones(numEntradas + 1)
        self.Saidas = np.zeros(numSaidas)
        self.Pesos = np.zeros(numEntradas + 1)
        self.IniciaPesos()

    def IniciaPesos(self):
        for i in range(len(self.Pesos)):
            self.Pesos[i] = r.random()

    def CalcularPotenciais(self):
        self.PotencialDeAtivacao = 0
        for i in range(0, len(self.Entradas)):
            self.PotencialDeAtivacao += self.Entradas[i] * self.Pesos[i]
    
    def CalcularSaidas(self):
        for i in range(0, len(self.Saidas)):
            self.Saidas[i] = self.FuncaoDeAtivacao()

    def FuncaoDeAtivacao(self):
        if self.PotencialDeAtivacao >= 0:
            return 1
        else:
            return 0

    def PropagaResposta(self, vetorEntradas):
        self.Entradas[1:] = vetorEntradas
        self.CalcularPotenciais()
        self.CalcularSaidas()
        return self.Saidas

    def AjusteDePesos(self, vetorSaidasEsperadas):
        for i in range(0, len(self.Saidas)):
            erro = vetorSaidasEsperadas[i] - self.Saidas[i]
            for j in range(0, len(self.Pesos)):
                self.Pesos[j] += self.TaxaDeAprendizado * erro * self.Entradas[j]

def executeAlgoritmo(neuronio, entradas, saidas):
    for i in range(0, 100):
        index = r.randint(0, len(entradas)-1)
        neuronio.PropagaResposta(entradas[index])
        neuronio.AjusteDePesos([saidas[index]])
    for i in range(0, len(entradas)):
        saida = neuronio.PropagaResposta(entradas[i])
        print ("Entrada ",(i+1),":",entradas[i]," Saída ",(i+1),":",saida," Saída esperada:",saidas[i])


neuronioPerceptron = Perceptron(2,1)

print("Porta OR")
neuronioPerceptron.IniciaPesos()
entradas = [[0,0],[1,0],[0,1],[1,1]]
saidas = [0,1,1,1]
executeAlgoritmo(neuronioPerceptron, entradas, saidas)

print("Porta AND")
neuronioPerceptron.IniciaPesos()
entradas = [[0,0],[1,0],[0,1],[1,1]]
saidas = [0,0,0,1]
executeAlgoritmo(neuronioPerceptron, entradas, saidas)