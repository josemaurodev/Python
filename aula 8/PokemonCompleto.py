import random

# Pokémons e seus níveis de evolução como "vida"
pokemon = {
    "Bulbasaur": 1, "Ivysaur": 16, "Venasaur": 32,
    "Charmander": 1, "Charmeleon": 16, "Charizard": 36,
    "Squirtle": 1, "Wartortle": 16, "Blastoise": 36
}

# Escolher Pokémon inicial
print("Escolha seu Pokémon:")
print("1 - Charmander")
print("2 - Squirtle")
print("3 - Bulbasaur")

num = int(input("Digite o número: "))

if num == 1:
    escolhido = "Charmander"
elif num == 2:
    escolhido = "Squirtle"
else:
    escolhido = "Bulbasaur"

meusPoke = [escolhido]
print("Seu Pokémon é:", escolhido)

# Loop do jogo
while len(meusPoke) > 0 and len(meusPoke) < len(pokemon):
    print("\nSeus Pokémons:", meusPoke)

    resto = [p for p in pokemon if p not in meusPoke]
    inimigo = random.choice(resto)

    print("Você encontrou um", inimigo)
    resposta = input("Quer batalhar? (s/n): ")

    if resposta == "n":
        continue

    venceu = False
    for i in range(len(meusPoke)):
        meu_poke = meusPoke[i]
        nivel_jogador = pokemon[meu_poke]
        nivel_inimigo = pokemon[inimigo]
        chance = random.randint(1, 20)

        if nivel_jogador >= nivel_inimigo:
            if chance <= 15:
                print(f"{meu_poke} venceu a batalha contra {inimigo}!")
                meusPoke.append(inimigo)
                venceu = True
                break
        else:
            if chance <= 5:
                print(f"{meu_poke} venceu a batalha contra {inimigo}!")
                meusPoke.append(inimigo)
                venceu = True
                break
            else:
                print(f"{meu_poke} perdeu a batalha contra {inimigo}...")
                meusPoke[i] = None

    meusPoke = [p for p in meusPoke if p is not None]

if len(meusPoke) == 0:
    print("\nVocê perdeu todos os seus Pokémons. Fim de jogo!")
else:
    print("\nParabéns! Você capturou todos os Pokémons!")
