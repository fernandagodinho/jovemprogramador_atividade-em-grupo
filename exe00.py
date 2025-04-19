import random

def jogo_adivinhe_o_numero():
    # Bem-vindo ao jogo
    print("Bem-vindo ao 'Adivinhe o Número Mágico'!")
    nome_jogador = input("Por favor, insira seu nome: ")
    print(f"Olá, {nome_jogador}! Vamos começar.")
    
    # Regras do Jogo
    print("\nRegras do Jogo:")
    print("1. O programa escolherá um número mágico entre 1 e 100.")
    print("2. Você terá 7 tentativas para adivinhar o número.")
    print("3. A cada tentativa, o programa informará se o número é maior ou menor.")
    print("4. Pontuações serão baseadas na tentativa em que acertar.")
    print("Boa sorte!\n")

    # Sorteando o número mágico
    numero_magico = random.randint(1, 100)
    tentativas = 7
    pontuacao = 0

    # Jogo começa
    for tentativa in range(1, tentativas + 1):
        try:
            chute = int(input(f"Tentativa {tentativa}: Digite seu número entre 1 e 100: "))
            if chute < 1 or chute > 100:
                print("Por favor, digite um número válido entre 1 e 100.")
                continue

            if chute == numero_magico:
                pontuacao = 100 - (tentativa - 1) * 10
                print(f"Parabéns, {nome_jogador}! Você acertou o número mágico {numero_magico} na tentativa {tentativa}.")
                print(f"Sua pontuação: {pontuacao}")
                break
            elif chute > numero_magico:
                print("O número mágico é menor.")
            else:
                print("O número mágico é maior.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Mensagem de derrota
    if pontuacao == 0:
        print(f"Que pena, você usou todas as tentativas! O número mágico era: {numero_magico}.")
        print("Sua pontuação: 0")
    
    # Salvar ranking (exemplo básico)
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome_jogador}: {pontuacao} pontos\n")
    print("Ranking atualizado no arquivo 'ranking.txt'.")
    
    print("Fim do jogo!")

# Execução do jogo
jogo_adivinhe_o_numero()
