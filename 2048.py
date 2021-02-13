# Importar bibliotecas necessárias.
import random
import copy

# Definir o a área do jogo e as dimensões.
tamanho = 4
tabuleiro = []


# Classe com as funcionalidades do Jogo.
class Jogo:
    # Função para gerar e imprimir o tabuleiro, ajustando o tamanho
    def matriz(self):
        maior = tabuleiro[0][0]
        for linha in tabuleiro:
            for elemento in linha:
                if elemento > maior:
                    maior = elemento

        espaco = len(str(maior))
        for linha in tabuleiro:
            atual = "|"
            for elemento in linha:
                if elemento == 0:
                    atual += " " * espaco + "|"
                else:
                    atual += str(elemento) + " " * (espaco - len(str(elemento))) + "|"
            # Imprimir linhas
            print(atual)

    # função para gerar os números (2 ou 4)
    def gerarNum(self):
        if random.randint(1, 6) == 4:
            return 4
        else:
            return 2

    # Função para adicionar o número gerado em uma posição aleatória
    def adicionarNum(self):
        num_linha = random.randint(0, tamanho - 1)
        num_coluna = random.randint(0, tamanho - 1)

        while not tabuleiro[num_linha][num_coluna] == 0:
            num_linha = random.randint(0, tamanho - 1)
            num_coluna = random.randint(0, tamanho - 1)

        tabuleiro[num_linha][num_coluna] = self.gerarNum()

    # Função para verificar se o usuário ganhou o jogo
    def vitoria(self):
        for linha in tabuleiro:
            if 2048 in linha:
                return True
        return False

    # Função para verificar se há movimentos disponíveis
    def semMovimentos(self):
        temp_tab1 = copy.deepcopy(tabuleiro)
        temp_tab2 = copy.deepcopy(tabuleiro)

        temp_tab1 = movimento.moverDir(temp_tab1)
        if temp_tab1 == temp_tab2:
            temp_tab1 = movimento.moverBaixo(temp_tab1)
            if temp_tab1 == temp_tab2:
                temp_tab1 = movimento.moverEsq(temp_tab1)
                if temp_tab1 == temp_tab2:
                    temp_tab1 = movimento.moverCima(temp_tab1)
                    if temp_tab1 == temp_tab2:
                        return True
        return False

# Classe para definir as movimentações no jogo
class Movimentacao:
    # Mover as linhas somando(inicialmente esquerda)
    def moverLinhaE(self, linha):
        for j in range(tamanho - 1):
            for i in range(tamanho - 1, 0, -1):
                if linha[i - 1] == 0:
                    linha[i - 1] = linha[i]
                    linha[i] = 0
        for i in range(tamanho - 1):
            if linha[i] == linha[i + 1]:
                linha[i] *= 2
                linha[i + 1] = 0

        for i in range(tamanho - 1, 0, -1):
            if linha[i - 1] == 0:
                linha[i - 1] = linha[i]
                linha[i] = 0
        return linha

    # Mover para esquerda
    def moverEsq(self, novoTabuleiro):
        for i in range(tamanho):
            novoTabuleiro[i] = self.moverLinhaE(novoTabuleiro[i])
        return novoTabuleiro

    # Inverter o tabuleiro
    def inverter(self, linha):
        aux = []
        for i in range(tamanho - 1, -1, -1):
            aux.append(linha[i])
        return aux

    # Transpor o tabuleiro
    def transpor(self, novoTabuleiro):
        for j in range(tamanho):
            for i in range(j, tamanho):
                if not i == j:
                    temp = novoTabuleiro[j][i]
                    novoTabuleiro[j][i] = novoTabuleiro[i][j]
                    novoTabuleiro[i][j] = temp
        return novoTabuleiro

    # Mover para a direita
    def moverDir(self, novoTabuleiro):
        for i in range(tamanho):
            novoTabuleiro[i] = self.inverter(novoTabuleiro[i])
            novoTabuleiro[i] = self.moverLinhaE(novoTabuleiro[i])
            novoTabuleiro[i] = self.inverter(novoTabuleiro[i])
        return novoTabuleiro

    # Mover para Baixo
    def moverBaixo(self, novoTabuleiro):
        novoTabuleiro = self.transpor(novoTabuleiro)
        novoTabuleiro = self.moverDir(novoTabuleiro)
        novoTabuleiro = self.transpor(novoTabuleiro)

        return novoTabuleiro

    # Mover para Cima
    def moverCima(self, novoTabuleiro):
        novoTabuleiro = self.transpor(novoTabuleiro)
        novoTabuleiro = self.moverEsq(novoTabuleiro)
        novoTabuleiro = self.transpor(novoTabuleiro)

        return novoTabuleiro

# Instanciar as classes
jogo = Jogo()
movimento = Movimentacao()

# Método Main - Execução do Programa.
def main(tabuleiro):
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(0)
        tabuleiro.append(linha)

    quant_num = 2
    while quant_num > 0:
        num_linha = random.randint(0, tamanho - 1)
        num_coluna = random.randint(0, tamanho - 1)

        if tabuleiro[num_linha][num_coluna] == 0:
            tabuleiro[num_linha][num_coluna] = jogo.gerarNum()
            quant_num -= 1

    print('----- Bem Vindo(a) ao jogo 2048!')
    print('Comandos: \n a - Mover para Esquerda \n s - Mover para Baixo \n d - Mover para Direita \n w - Mover para Cima \n ')

    jogo.matriz()

    fimDeJogo = False

    while not fimDeJogo:
        mover = input("Para qual lado deseja mover? ")

        entradaValida = True

        tabTemp = copy.deepcopy(tabuleiro)

        if mover == 'd':
            tabuleiro = movimento.moverDir(tabuleiro)
        elif mover == 's':
            tabuleiro = movimento.moverBaixo(tabuleiro)
        elif mover == 'a':
            tabuleiro = movimento.moverEsq(tabuleiro)
        elif mover == 'w':
            tabuleiro = movimento.moverCima(tabuleiro)
        else:
            entradaValida = False

        if not entradaValida:
            print('Insira um valor válido!')
        else:
            if tabuleiro == tabTemp:
                print('Tente outra direção!')
            else:
                if jogo.vitoria():
                    jogo.matriz()
                    print('Parabéns! Você Ganhou!')
                    fimDeJogo = True
                else:
                    jogo.adicionarNum()
                    jogo.matriz()

                    if jogo.semMovimentos():
                        print('Não há mais movimentos possíveis. Voce perdeu!')
                        fimDeJogo = True

# Função para executar o programa.
if __name__ == "__main__":
    main(tabuleiro)
