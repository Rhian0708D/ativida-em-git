import random

def player_choice():
    print("\nEscolha sua opção: \n1 - Pedra \n2 - Papel \n3 - Tesoura")
    choice = input("Digite o número da sua escolha: ")
    return choice

def computer_choice():
    computer_choice = random.randint(1, 3)
    return computer_choice

def game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Empate!"
    elif (player_choice == '1' and computer_choice == '3') or \
         (player_choice == '2' and computer_choice == '1') or \
         (player_choice == '3' and computer_choice == '2'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

while True:
    print("\n*** Pedra, Papel ou Tesoura ***")
    player_choice = player_choice()
    computer_choice = computer_choice()

    print("\nJogador:", player_choice)
    print("Computador:", computer_choice)

    result = game_result(player_choice, computer_choice)
    print("\nResultado:", result)

    next_game = input("\nDeseja jogar novamente? (Digite 'sim' ou 'não')")
    if next_game.lower() != 'sim':
        break