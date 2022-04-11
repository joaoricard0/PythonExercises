import random
print(f"{' Jogo Pedra/Papel/Tesoura ':*^40}")
print("""[1] Jogar
[2] Sair""")
opcao = int(input("escolhe uma opcao:"))

if opcao == 1:
    
    while True:
        jogador = input("Vamos jogar Pedra/Papel/Tesoura, joga!: ")
        computador = random.choice(["pedra", "papel","tesoura"])
        if computador == "pedra" and jogador == "pedra" or computador == "papel" and jogador == "papel" or computador == "tesoura" and jogador == "tesoura":
            print(f"O resultado entre {computador} e {jogador} é empate")
        elif computador == "tesoura" and jogador == "pedra" or computador == "papel" and jogador == "tesoura" or computador == "pedra" and jogador == "papel":
            print(f"O resultado entre {computador} e {jogador} é vitória para o jogador")
        elif computador == "pedra" and jogador == "tesoura" or computador == "tesoura" and jogador == "papel" or computador == "papel" and jogador == "pedra":
            print(f"O resultado entre {computador} e {jogador} é vitória para o computador")
        else:
            print("Jogada inválida")
        if input("Deseja sair (Y/N) ? ").lower() == "y":
            False
            print("Jogo Terminado")
elif opcao == 2:
    print("Jogo Terminado")
    quit()
else:
    print("opcao errada")