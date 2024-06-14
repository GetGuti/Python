def menu(agenda):
    while True:
        print("\n### Menu ###")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif opcao == '3':
            nome = input("Digite o nome do contato a ser pesquisado: ")
            agenda.pesquisar_contato(nome)
        elif opcao == '4':
            agenda.listar_contatos()
        elif opcao == '5':
            print("Programa encerrado. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"O contato {nome} já existe na agenda.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato {nome} adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"O contato {nome} não foi encontrado na agenda.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}")
            print(f"Telefone: {self.contatos[nome]}")
        else:
            print(f"O contato {nome} não foi encontrado na agenda.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}")
                print(f"Telefone: {telefone}")
                print()            

agenda = AgendaTelefonica()

menu(agenda)