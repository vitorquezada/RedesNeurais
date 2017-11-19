import numpy as np
import random as r

class Adaline:
    Bias = r.random()
    def __init__(self, numEntradas, numSaidas, TaxaDeAprendizado = 1):
        self.Entradas = np.ones(numEntradas + 1)
        self.Saidas = np.zeros(numSaidas)
        self.TaxaDeAprendizado = TaxaDeAprendizado
        self.Pesos = np.zeros(numEntradas + 1)
        self.IniciaPesos()

    def IniciaPesos(self):
        for i in range(0, len(self.Pesos)):
            self.Pesos[i] = r.random()

    def CalcularPotenciais(self):
        self.PotencialDeAtivacao = 0
        for i in range(0, len(self.Entradas)):
            self.PotencialDeAtivacao += self.Entradas[i] * self.Pesos[i]
    
    def FuncaoDeAtivacao(self):
        return np.tanh(self.PotencialDeAtivacao)

    def CalcularSaidas(self):
        for i in range(0, len(self.Saidas)):
            self.Saidas[i] = self.FuncaoDeAtivacao()

    def PropagaResposta(self, vetorEntradas):
        self.Entradas[1:] = vetorEntradas
        self.CalcularPotenciais()
        self.CalcularSaidas()
        return self.Saidas

    def AjusteDePesos(self, vetorSaidasEsperadas):
        for i in range(0, len(self.Saidas)):
            for j in range(0, len(self.Pesos)):
                self.Pesos[j] += self.TaxaDeAprendizado * (vetorSaidasEsperadas[i] - self.Saidas[i]) * self.Entradas[j]





def CalculaLMS(neuronio,entradas,saidasEsperadas):
    erroAcumulado = 0
    for i in range(0, len(saidasEsperadas)):
        saida = neuronio.PropagaResposta(entradas[i])
        saida -= neuronio.Pesos[0]
        erroAcumulado += ((saidasEsperadas[i] - saida)**2)
    return erroAcumulado / len(saidasEsperadas)

def executeAlgoritmo(neuronio, entradas, saidas):
    epocas = 1
    epsilon = 0.0000001
    
    while True:
        erroAnterior = CalculaLMS(neuronio, entradas, saidas)
        
        index = r.randint(0, len(entradas)-1)
        neuronio.PropagaResposta(entradas[index])
        neuronio.AjusteDePesos([saidas[index]])
        
        erroAtual = CalculaLMS(neuronio, entradas, saidas)

        epocas += 1
        if np.abs(erroAtual - erroAnterior) < epsilon:
            print("Épocas percorridas: ",epocas)
            print("Bias: ",neuronio.Pesos[0])
            print("Pesos: ",neuronio.Pesos[1:])
            break;
        else:
            erroAnterior = erroAtual        
    
    for i in range(0, len(entradas)):
        saida = neuronio.PropagaResposta(entradas[i])
        print ("Entrada ",(i+1),":",entradas[i]," Saída ",(i+1),":",saida," Saída esperada:",saidas[i])


neuronioAdaline = Adaline(2,1)

print("Porta OR")
neuronioAdaline.IniciaPesos()
entradas = [[0,0],[1,0],[0,1],[1,1]]
saidas = [-1,1,1,1]
executeAlgoritmo(neuronioAdaline, entradas, saidas)

print("Porta AND")
neuronioAdaline.IniciaPesos()
entradas = [[0,0],[1,0],[0,1],[1,1]]
saidas = [-1,-1,-1,1]
executeAlgoritmo(neuronioAdaline, entradas, saidas)