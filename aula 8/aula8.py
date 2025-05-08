# def adventure_game():
#   print("Sejam bem vindos a Dungeon! Seu objetivo é encontrar o tesouro.")
#   print("Escolha as suas ações com cuidado para evitar armadilhas e erros.")

#   try:
#     print("Você está em frente a 3 portas: [1, 2 e 3]")
#     porta = int(input("Qual porta você escolhe:"))

#     if porta == 1:
#       print("Você encontrou um monstro! Ele atacou você, porém você escapou.")
#     elif porta == 2:
#       print("Parabéns você encontrou o tesouro.")
#       return
#     elif porta == 3:
#       print("Infelizmente um monstro te atacou e você morreu.")
#   except ValueError:
#     print("Essa porta não existe!")
#   finally:
#     print("Fim do turno")

# adventure_game()

# life = 100
# pokemon = {"Bulbasaur": 15, "Ivysaur": 20, "Venasaur": 30,
#            "Charmander": 15, "Charmeleon": 20, "Charizard": 30,
#            "Squirtle": 15, "Wartortle": 20, "Blastoise": 30 
#            }

# #Escolher um pokemon inicial
# #Batalhar com um pokemon
# #A vitoria é randomica 2/3 de chance
# #Caso perca, diminui a vida
# #Caso vença, pegou o pokemon
# #Meta, pegar todos

# import random
# meuPokemon = []
# meuPokemon = ["Bulbasaur"]
# meuPokemon = ["Bulbasaur"] + ["Ivysaur"]
# print(meuPokemon)
# print("Minha vida é:" . life)


# while(life > 0):
#   sorteia pot: recuperar vida
#   luta:
#     sorteia numero entre 1 e 3, caso seja 3 perdeu a vida do pokemon selecionado
#     caso vença, adiciona o pokemon ao vetor de pokemons
#     caso perca, diminui a vida 
  

# vetor = [1, 2, 3]
# vetorB = vetor + [4]
# print(vetorB)

import random

# Vida do jogador
life = 100

# Pokémons disponíveis e seus "valores de dano"
pokemon = {
    "Bulbasaur": 15, "Ivysaur": 20, "Venasaur": 30,
    "Charmander": 15, "Charmeleon": 20, "Charizard": 30,
    "Squirtle": 15, "Wartortle": 20, "Blastoise": 30
}

# Pokémons já capturados
meuPokemon = ["Bulbasaur"]

print("Meus Pokémons:", meuPokemon)
print("Minha vida é:", life)

# Loop do jogo enquanto o jogador estiver vivo e não tiver todos os pokémons
while life > 0 and len(meuPokemon) < len(pokemon):
    print("Meus Pokémons:", meuPokemon)
    print("Minha vida é:", life)
    # Sorteia um Pokémon que o jogador ainda não tem
    pokemons_restantes = [p for p in pokemon if p not in meuPokemon]
    pokemon_inimigo = random.choice(pokemons_restantes)

    print(f"\nVocê encontrou um {pokemon_inimigo}! Deseja batalhar? (s/n)")
    resposta = input().lower()

    if resposta != "s":
        continue
    # Sorteia chance de vitória (1 em 3 perde, 2 em 3 vence)
    resultado = random.randint(1, 3)

    if resultado == 3:
        dano = pokemon[pokemon_inimigo]
        life -= dano
        print(f"Você perdeu a batalha! Perdeu {dano} de vida. Vida atual: {life}")
    else:
        meuPokemon.append(pokemon_inimigo)
        print(f"Você venceu e capturou o {pokemon_inimigo}!")

# Resultado final
if life <= 0:
    print("\nVocê perdeu todas as vidas! Fim de jogo.")
else:
    print("\nParabéns! Você capturou todos os Pokémons!")
