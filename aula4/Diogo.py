#caracteres UTF-8 ç ã

opçaoum = "tomar banho"
opçaodois = "escovar os dentes"
opçaotres = "passar café"
opçaoquatro = "comer miojo"
opçaocinco = "ir a escola"
opçaoseis = "jogar lol"
opçaosete = "chamar ajuda"

print(f"Acordo pela manhã, devo {opçaoum} ou {opçaodois}?")

chooseum = input("O que devo fazer?: ").lower
if (chooseum == opçaoum):
   print(f"Após tomar banho, me sinto revigorado")

elif (chooseum  == opçaodois):
   print("Após escovar os dentes, sinto um frescor na boca")

choosedois = input(f"Agora, devo {opçaotres}, ou {opçaoquatro}?: ").lower

if (choosedois == opçaotres):
   print ("cAIU AQUi")
   print(f"Me sinto energético.")

   choosetres = input(f"Agora, devo {opçaocinco}, ou {opçaoseis}?: ").lower

   if (choosetres == opçaocinco):
      print("Hora de aprender!")

   elif (choosetres == opçaoseis):
      print("A raiva domina meu coração e eu crio um mundo de ódio e destruição")

elif (choosedois == opçaoquatro):
      print("Sinto uma pontada no peito.")

      choosetres = input(f"Agora, devo {opçaosete}, ou {opçaoseis}?: ").lower

      if (choosetres == opçaoseis):
        print("Eu morri de miojo")

      elif (choosetres == opçaosete):
        print("Acordo na maca da ambulância.")

print("Fim...")