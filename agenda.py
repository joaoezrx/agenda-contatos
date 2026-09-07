# agenda.py
# Agenda de Contatos - Estrutura Inicial
# Projeto em Ciência de Dados I - Atividade em Dupla

contatos = []


def cadastrar_contato():
    """Cadastra um novo contato (nome, telefone e email)."""
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)

    print(f"Contato '{nome}' cadastrado com sucesso!")


def listar_contatos():
    """Lista todos os contatos cadastrados."""
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    print("\n--- Contatos cadastrados ---")
    for i, contato in enumerate(contatos, start=1):
        print(f"{i}. {contato['nome']} | {contato['telefone']} | {contato['email']}")


def buscar_contato():
    """Busca um contato pelo nome."""
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    nome_busca = input("Digite o nome a buscar: ")
    encontrados = [c for c in contatos if nome_busca.lower() in c["nome"].lower()]

    if not encontrados:
        print(f"Nenhum contato encontrado com o nome '{nome_busca}'.")
        return

    print("\n--- Resultado da busca ---")
    for contato in encontrados:
        print(f"{contato['nome']} | {contato['telefone']} | {contato['email']}")


def remover_contato():
    """Remove um contato."""
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    nome_remover = input("Digite o nome do contato a remover: ")
    for contato in contatos:
        if contato["nome"].lower() == nome_remover.lower():
            contatos.remove(contato)
            print(f"Contato '{nome_remover}' removido com sucesso!")
            return

    print(f"Nenhum contato encontrado com o nome '{nome_remover}'.")


def exibir_menu():
    print("\n===== AGENDA DE CONTATOS =====")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            remover_contato()
        elif opcao == "0":
            print("Encerrando a agenda...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()