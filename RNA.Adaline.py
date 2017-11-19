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
        return np.tanh(self.PotencialDeAtivacao)

    def PropagaResposta(self, vetorEntradas):
        self.Entradas[1:] = vetorEntradas
        self.CalcularPotenciais()
        self.CalcularSaidas()
        return self.Saidas

    def AjusteDePesos(self, vetorSaidasEsperadas):
        erroAcumulado = 0
        for i in range(0, len(self.Saidas)):
            erro = vetorSaidasEsperadas[i] - self.Saidas[i]
            for j in range(0, len(self.Pesos)):
                self.Pesos[j] += self.TaxaDeAprendizado * erro * self.Entradas[j]
            erroAcumulado += (erro**2)
        return erroAcumulado/len(self.Entradas)

def CalculaLMS(neuronio,entradas,saidas):
    erroAcumulado = 0
    for i in range(1, len(entradas)):
        saida = neuronio.PropagaResposta(entradas[i])
        print("Saída esperada: ", saidas[i]," Saída obtida: ", saida)
        erroAcumulado += ((saidas[i] - saida)**2)
    erroAcumulado -= 
    print(np.abs(erroAcumulado))
    return np.abs(erroAcumulado/len(saidas))

def executeAlgoritmo(neuronio, entradas, saidas):
    epocas = 1
    epsilon = 0.000001
    erroAnterior = CalculaLMS(neuronio, entradas, saidas)
    condicao = True
    while condicao:
        index = r.randint(0, len(entradas)-1)
        neuronio.PropagaResposta(entradas[index])
        neuronio.AjusteDePesos([saidas[index]])


        erroAtual = CalculaLMS(neuronio, entradas, saidas)
        epocas += 1
        if np.abs(erroAtual - erroAnterior) < epsilon:
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
saidas = [0,1,1,1]
executeAlgoritmo(neuronioAdaline, entradas, saidas)

print("Porta AND")
neuronioAdaline.IniciaPesos()
entradas = [[0,0],[1,0],[0,1],[1,1]]
saidas = [0,0,0,1]
executeAlgoritmo(neuronioAdaline, entradas, saidas)