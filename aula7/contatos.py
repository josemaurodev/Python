contatos = {"José", "João", "Gustavo", "Thales"}

print("Qual contato deseja excluir?")
for p in contatos:
    print(p)

contatoExcluir = input("Digite o nome do contato para excluir: ")

if contatoExcluir in contatos:
    contatos = contatos - {contatoExcluir}
    #+ -> |
    #- -> - 
    #= -> &
    #contatos.remove(contatoExcluir)
    print(f"Contato '{contatoExcluir}' excluído com sucesso.")
else:
    print(f"Contato '{contatoExcluir}' não encontrado.")

print("Contatos restantes:", contatos)
