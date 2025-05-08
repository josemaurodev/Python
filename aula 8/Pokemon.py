import random

# Pokémons e seus níveis de evolução como dano
pokemon = {
    "Bulbasaur", "Ivysaur", "Venasaur",
    "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise"
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

# Lista com os Pokémons do jogador
meusPoke = [escolhido]
print("Seu Pokémon é:", escolhido)

# Loop do jogo
while len(meusPoke) > 0 and len(meusPoke) < len(pokemon):
    print("\nSeus Pokémons:", meusPoke)

    # Sorteia oponente que ainda não foi capturado
    resto = [p for p in pokemon if p not in meusPoke]
    inimigo = random.choice(resto)

    print("Você encontrou um", inimigo)
    resposta = input("Quer batalhar? (s/n): ")

    if resposta != "s":
        continue

    # Tenta batalhar com cada Pokémon que o jogador tem
    venceu = False
    for i in range(len(meusPoke)):
        chance = random.randint(1, 3)
        if chance != 3:
            print(f"{meusPoke[i]} venceu a batalha contra {inimigo}!")
            meusPoke.append(inimigo)
            venceu = True
            break
        else:
            print(f"{meusPoke[i]} perdeu a batalha...")
    
            # Marca o Pokémon como derrotado
            meusPoke[i] = None

    # Remove todos os Pokémons que foram derrotados (None)
    pokes_vivos = []
    for p in meusPoke:
        if p is not None:
            pokes_vivos.append(p)
    meusPoke = pokes_vivos

# Fim do jogo
if len(meusPoke) == 0:
    print("\nVocê perdeu todos os seus Pokémons. Fim de jogo!")
else:
    print("\nParabéns! Você capturou todos os Pokémons!")
