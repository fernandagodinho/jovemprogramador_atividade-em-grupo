"""Parte 1 Algoritmo (Escreva em forma de texto) 
Antes de começar a programar, escreva o passo a passo do funcionamento do jogo, como 
se estivesse explicando para outra pessoa. Use frases curtas, claras e em ordem lógica. 
Exemplo de começo: 
1. Iniciar o programa. 
2. Mostrar uma mensagem de boas-vindas. 
3. ... 
Parte 2  Codificação em Python 
Após revisar o algoritmo com seu grupo, programem o jogo conforme as regras: 
Regras do Jogo: 
• O programa solicita o nome do usuário 
• O exibe o nome do jogo 
• O sistema mostra as regras 
• O programa sorteia um número entre 1 e 100. 
• O jogador tem 7 tentativas. 
• A cada tentativa, o jogo diz se o número digitado é maior ou menor que o número 
mágico. 
• Se acertar, mostra mensagem de vitória e quantas tentativas foram usadas. 
• Se errar todas, mostra mensagem de derrota com o número correto. 
• O jogador ganha pontos conforme a tentativa em que acertar. 
• Ao final, mostrar um ranking com os nomes e pontuações dos jogadores/grupos. 
Pontuação: 
• Acertar na 1ª tentativa: 100 pontos 
• Na 2ª: 90 pontos 
• Na 3ª: 80 pontos 
• ... 
• Na 7ª: 40 pontos 
• Se errar todas: 0 pontos 
Desafio Extra (opcional): 
• Criar um modo com 2 jogadores que se alternam nas tentativas. 
• Criar um placar final com o vencedor da rodada. 
• Salvar o ranking em um arquivo .txt (pesquisar uso de arquivos em Python). 
Entrega: 
• Parte 1: Algoritmo em texto  
• Parte 2: Código Python funcional do grupo."""

import random

# Função para exibir o cabeçalho do jogo
def jogar():
    nome = input("Digite seu nome: ")
    print("\nBem-vindo(a) ao Jogo de Adivinhação, {}!".format(nome))
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print("Você tem 7 tentativas.\n")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    pontuacao = 0

    while tentativas < 7:
        tentativas += 1
        try:
            palpite = int(input("Tentativa {}: Digite um número: ".format(tentativas)))
            if 1 <= palpite <= 100:
                if palpite == numero_secreto:
                    print("\nParabéns, {}! Você acertou o número em {} tentativas!".format(nome, tentativas))
                    if tentativas == 1:
                        pontuacao = 100
                    elif tentativas == 2:
                        pontuacao = 90
                    elif tentativas == 3:
                        pontuacao = 80
                    elif tentativas == 4:
                        pontuacao = 70
                    elif tentativas == 5:
                        pontuacao = 60
                    elif tentativas == 6:
                        pontuacao = 50
                    elif tentativas == 7:
                        pontuacao = 40
                    print("Sua pontuação é: {} pontos.\n".format(pontuacao))
                    return nome, pontuacao
                elif palpite < numero_secreto:
                    print("O número secreto é maior.\n")
                else:
                    print("O número secreto é menor.\n")
            else:
                print("Por favor, digite um número entre 1 e 100.\n")
                tentativas -= 1 # Não contar tentativa inválida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            tentativas -= 1 # Não contar tentativa inválida

    print("\nFim das tentativas, {}! Você não conseguiu adivinhar.".format(nome))
    print("O número secreto era {}.\n".format(numero_secreto))
    return nome, 0

def mostrar_ranking(ranking):
    if ranking:
        print("\n----- Ranking dos Jogadores -----")
        ranking_ordenado = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
        for jogador, pontos in ranking_ordenado:
            print("{}: {} pontos".format(jogador, pontos))
        print("-------------------------------\n")
    else:
        print("\nAinda não há jogadores no ranking.\n")

def main():
    ranking = {}
    while True:
        nome_jogador, pontuacao_jogador = jogar()
        ranking[nome_jogador] = ranking.get(nome_jogador, 0) + pontuacao_jogador
        mostrar_ranking(ranking)

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    main()

"""O código acima implementa um jogo de adivinhação onde o jogador tenta adivinhar um número secreto entre 1 e 100.
O jogador tem 7 tentativas e ganha pontos conforme a tentativa em que acerta.
O ranking dos jogadores é exibido ao final de cada partida.
O jogo continua até que o jogador decida sair.
O código também trata entradas inválidas e garante que o jogador só insira números dentro do intervalo permitido.
O ranking é salvo em um dicionário, onde o nome do jogador é a chave e a pontuação é o valor.
O ranking é exibido em ordem decrescente de pontuação.
O jogo é encerrado quando o jogador decide não jogar mais.
O código é modularizado em funções para facilitar a leitura e manutenção.
O jogo é interativo e fornece feedback ao jogador a cada tentativa.
O código é escrito em Python e utiliza a biblioteca random para gerar o número secreto.
O código é funcional e atende aos requisitos propostos na atividade.  
O código é claro e bem estruturado, facilitando a compreensão e a manutenção."""