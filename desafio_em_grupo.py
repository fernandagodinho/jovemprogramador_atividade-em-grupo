import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.ranking = "ranking.txt"

    def jogar(self, nome, tentativas_totais):
        tentativas = 0
        while tentativas < tentativas_totais:
            tentativas += 1
            try:
                palpite = int(input(f"Tentativa {tentativas} de {tentativas_totais}, {nome}: Digite um número: "))
                if 1 <= palpite <= 100:
                    if palpite == self.numero_secreto:
                        print(f"\nParabéns, {nome}! Você acertou o número em {tentativas} tentativas!")
                        pontuacao = 100 - (tentativas - 1) * 10
                        return pontuacao
                    elif palpite < self.numero_secreto:
                        print("O número secreto é maior.\n")
                    else:
                        print("O número secreto é menor.\n")
                else:
                    print("Por favor, digite um número entre 1 e 100.\n")
                    tentativas -= 1  # Não contar tentativa inválida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.\n")
                tentativas -= 1  # Não contar tentativa inválida
        print(f"\nFim das tentativas, {nome}! O número secreto era {self.numero_secreto}.")
        return 0

    def modo_um_jogador(self):
        nome = input("Digite seu nome: ")
        print(f"\nBem-vindo(a), {nome}!")
        print("Regras do jogo: tente adivinhar o número secreto entre 1 e 100.")
        print("Você tem 7 tentativas.\n")
        pontuacao = self.jogar(nome, 7)
        self.salvar_ranking(nome, pontuacao)

    def modo_dois_jogadores(self):
        nomes = [input(f"Digite o nome do jogador {i+1}: ") for i in range(2)]
        print("\nBem-vindos ao modo para dois jogadores!")
        print("Regras: vocês se alternam nas tentativas para adivinhar o número secreto.\n")
        tentativas_totais = 7
        pontuacoes = {nomes[0]: 0, nomes[1]: 0}

        for tentativas in range(1, tentativas_totais + 1):
            jogador_atual = nomes[tentativas % 2]
            pontuacoes[jogador_atual] += self.jogar(jogador_atual, 1)
            if pontuacoes[jogador_atual] > 0:
                break

        print("\n----- Resultado Final -----")
        for jogador, pontos in pontuacoes.items():
            print(f"{jogador}: {pontos} pontos")
        vencedor = max(pontuacoes, key=pontuacoes.get)
        print(f"O vencedor é {vencedor}!\n")

    def salvar_ranking(self, nome, pontuacao):
        with open(self.ranking, "a") as arquivo:
            arquivo.write(f"{nome}: {pontuacao} pontos\n")
        print("Ranking atualizado com sucesso!\n")

    def mostrar_ranking(self):
        try:
            with open(self.ranking, "r") as arquivo:
                print("\n----- Ranking -----")
                print(arquivo.read())
        except FileNotFoundError:
            print("\nRanking ainda não foi criado.")

    def iniciar_jogo(self):
        while True:
            print("\nEscolha o modo de jogo:")
            print("1. Um jogador")
            print("2. Dois jogadores")
            print("3. Mostrar ranking")
            print("4. Sair")
            opcao = input("Digite sua escolha: ")

            if opcao == "1":
                self.modo_um_jogador()
            elif opcao == "2":
                self.modo_dois_jogadores()
            elif opcao == "3":
                self.mostrar_ranking()
            elif opcao == "4":
                print("Saindo do jogo. Até a próxima!")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    jogo = JogoAdivinhacao()
    jogo.iniciar_jogo()
