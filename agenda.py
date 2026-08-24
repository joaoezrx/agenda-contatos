# agenda.py
# Agenda de Contatos - Estrutura Inicial
# Projeto em Ciência de Dados I - Atividade em Dupla

contatos = []


def cadastrar_contato():
    """Cadastra um novo contato (nome, telefone e email)."""
    # TODO: implementar (Pessoa A)
    pass


def listar_contatos():
    """Lista todos os contatos cadastrados."""
    # TODO: implementar (Pessoa A)
    pass


def buscar_contato():
    """Busca um contato pelo nome."""
    # TODO: implementar (Pessoa B)
    pass


def remover_contato():
    """Remove um contato."""
    # TODO: implementar (Pessoa B)
    pass


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
