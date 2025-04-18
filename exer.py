import random

def jogar(nome, numero_secreto, tentativas_totais):
    tentativas = 0
    while tentativas < tentativas_totais:
        tentativas += 1
        try:
            palpite = int(input(f"Tentativa {tentativas} de {tentativas_totais}, {nome}: Digite um número: "))
            if 1 <= palpite <= 100:
                if palpite == numero_secreto:
                    print(f"\nParabéns, {nome}! Você acertou o número em {tentativas} tentativas!")
                    pontuacao = 100 - (tentativas - 1) * 10
                    return pontuacao
                elif palpite < numero_secreto:
                    print("O número secreto é maior.\n")
                else:
                    print("O número secreto é menor.\n")
            else:
                print("Por favor, digite um número entre 1 e 100.\n")
                tentativas -= 1  # Não contar tentativa inválida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            tentativas -= 1  # Não contar tentativa inválida
    print(f"\nFim das tentativas, {nome}! O número secreto era {numero_secreto}.")
    return 0

def modo_um_jogador():
    nome = input("Digite seu nome: ")
    print(f"\nBem-vindo(a), {nome}!")
    print("Regras do jogo: tente adivinhar o número secreto entre 1 e 100.")
    print("Você tem 7 tentativas.\n")
    numero_secreto = random.randint(1, 100)
    pontuacao = jogar(nome, numero_secreto, 7)
    return nome, pontuacao

def modo_dois_jogadores():
    nomes = [input(f"Digite o nome do jogador {i+1}: ") for i in range(2)]
    print("\nBem-vindos ao modo para dois jogadores!")
    print("Regras: vocês se alternam nas tentativas para adivinhar o número secreto.")
    print("O jogador que acertar primeiro ou fizer mais pontos vence!\n")
    numero_secreto = random.randint(1, 100)
    tentativas_totais = 14
    pontuacoes = {nomes[0]: 0, nomes[1]: 0}

    for tentativas in range(1, tentativas_totais + 1):
        jogador_atual = nomes[tentativas % 2]
        pontuacoes[jogador_atual] += jogar(jogador_atual, numero_secreto, 1)
        if pontuacoes[jogador_atual] > 0:
            break

    print("\n----- Resultado Final -----")
    for jogador, pontos in pontuacoes.items():
        print(f"{jogador}: {pontos} pontos")
    vencedor = max(pontuacoes, key=pontuacoes.get)
    print(f"O vencedor é {vencedor}!\n")

def salvar_ranking(nome, pontuacao):
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome}: {pontuacao} pontos\n")
    print("Ranking atualizado com sucesso!\n")

def mostrar_ranking():
    try:
        with open("ranking.txt", "r") as arquivo:
            print("\n----- Ranking -----")
            print(arquivo.read())
    except FileNotFoundError:
        print("\nRanking ainda não foi criado.")

def main():
    while True:
        print("\nEscolha o modo de jogo:")
        print("1. Um jogador")
        print("2. Dois jogadores")
        print("3. Mostrar ranking")
        print("4. Sair")
        opcao = input("Digite sua escolha: ")

        if opcao == "1":
            nome, pontuacao = modo_um_jogador()
            salvar_ranking(nome, pontuacao)
        elif opcao == "2":
            modo_dois_jogadores()
        elif opcao == "3":
            mostrar_ranking()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
