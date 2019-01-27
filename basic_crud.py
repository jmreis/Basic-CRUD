import sqlite3
import os
import time


# import winsound

class Manager:
    """Classe que vai gerenciar a aplicação"""

    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""

    def add(self):
        """Função com a finalidade de adicionar novo contato no db"""

        # Variavel que vai guardar condição do while
        running = True

        # Repetição para introduzir contatos
        while running:

            # Comando para limpar a tela
            os.system("clear")
            # Mensagem de cabeçalho
            print("-----------------------ADICIONE UM NOVO CONTATO-----------------------\n")
            # Mensagem para cancelar função
            print("PRECIONE A TECLA SHIRFT + Q PARA CANCELAR")

            # Criação de uma variavel temporaria para verificar o db
            temp_name = input("Name: ")
            # Condiçao de erro para preenchimento vazio
            if len(temp_name) != 0 and  temp_name != "Q".upper():

                # Conecção com o db para verificar se o ctt ja existe
                db = sqlite3.connect("connection")
                cursor = db.cursor()


                # Verificação de dados no db
                cursor.execute("SELECT Name FROM contacts")
                # Variavel que guardará o resultado
                result = cursor.fetchall()
                # Impressão do resultado
                for i in result:
                    # Condição de o dado existir
                    if temp_name in i:
                        # Mensagem de existencia de dados
                        print("ESTE CONTATO JA EXISTE")
                        # Tempo de execução
                        time.sleep(2)
                        # Executa função add
                        self.add()
                        # Atribuição da variavel temp_name
                        self.name = temp_name
                        # Excluido dados de temp_name
                        temp_name = ""

                """# Entrada de dados para o atributo name
                self.name = input("Name:")
                # Tempo de Execução
                time.sleep(0.20)"""

                # Entrada de dados para o atributo phone
                self.phone = input("Phone:")
                # Tempo de Execução
                time.sleep(0.20)

                # Entrada de dados para o atributo address
                self.address = input("Address:")
                # Tempo de Execução
                time.sleep(0.20)

                # Conexão para o db
                db = sqlite3.connect("connection")

                # Criação de objeto para db
                cursor = db.cursor()

                # Inserindo dados na tabela
                cursor.execute("""INSERT INTO contacts\
                                (Name, Phone, Address)VALUES(?, ?, ?)""", (self.name, self.phone, self.address))

                # Confirmação da entrada de dados
                db.commit()

                # Variavel para adicionar mais contatos
                add_more = input("DESEJA ADICIONAR MAIS CONTATOS? (Y/N): ")

                # Condição para escolhado usuario
                if add_more in ["y", "Y"]:
                    continue
                else:
                    # Encerrando db
                    db.close()
                    # Break para variavel running
                    running = False
                    # Mensagem de encerramento para o usuário
                    print("SAINDO DO MENU")
                    # Tempo de execução
                    time.sleep(2)

            # Condição se o usuario teclar Q
            elif temp_name  == "Q".upper():
                # Mensagem de encerramento
                print("SAINDO DO MENU PRINCIPAL")
                # Tempo de execução
                time.sleep(2)
                # Executa função menu
                self.menu()

            # Condição se o campo for vazio
            else:
                # Mensagem de erro ao usuário
                print("FAVOR PREENCHER O MENU PRINCIPAL")
                # Tempo de execução
                time.sleep(2)
                # Executa a função
                self.add()

    def update(self):
        pass

    def remove(self):
        """Função para remover dados cadastrados"""

        # Mensagem de cabeçalho
        print("-----------------------REMOVER UM CONTATO-----------------------\n")
        # Variavel que recebe name para deletar
        name = input("DIGITE O NOME PARA DELETAR: ")
        # Variavel para confirmar a ação
        confirm = input("CONFIRMAR(Y/N): ")
        # Condição para ação confirmada
        if confirm in ["Y", "y"]:
            # Conecção com o db
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            # Deleta o dado em db
            cursor.execute("DELETE FROM contacts WHERE Name = ?", (name,))
            # Atualiza o db
            db.commit()
            # Mensagem de ação realizada
            print("-----------------------CADASTRO DELETADO COM SUCESSO-----------------------\n")
            # Tempo de execução
            time.sleep(2)
            # Executa função menu
            self.menu()
        # Condição para ação não confirmada
        else:
            # Mensagem de saida da função
            print("-----------------------SAINDO DO MENU PRINCIPAL-----------------------\n")
            # Tempo de execução
            time.sleep(3)
            # Executa função menu
            self.menu()


    def get_list(self):
        """Função que tem a finalidade de imprimir buscas em db"""

        count = 0
        count_2 = 0
        # Estabelecendo conexão com db
        db = sqlite3.connect("connection")
        # Variavel de dados de db
        cursor = db.cursor()
        # Comando para limpar a tela
        os.system("clear")
        # Cabeçalho para exibição de dados
        print("*********************CONTATOS*********************")
        # Tempo de execução
        time.sleep(0.50)
        # Busca de dados na tabela contacts
        cursor.execute("SELECT Name, Phone, Address FROM contacts")
        # Variavel que vai guardar os dados da busca
        result = cursor.fetchall()
        # Impressao dos resultados para o usuário.
        for row in result:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2, row)
            # Condição para encerrar a repetição.
            if count == 5:
                # Instrução para teclar para encerramento
                input("PRECIONE QUALQUER TECLA PARA CONTINUAR")
                count = 0
            # Espaça de uma linha
            print()

        print() # Espaço de uma linha
        # Mensagem de encerramento
        print("Final dos Resultados")
        # Espaço de uma linha
        print()
        # Mensagens de opções para o usuário
        print("ESCOLHA UMA OPÇÃO PARA CONTINUAR")
        # Variavel que guardara o valor da opção do usuário
        option = input(
                "DIGITE (A) PARA ATUALIZAR\n"
                "DIGITE (R) PARA REMOVER\n"
                "DIGITE (M) PARA RETORNAR AO MENU:\n"
                ""
            )

        # Condições para continuar com o programa
        if option in ["A", "a"]:
            # Executa função update
            self.update()
        elif option in ["R", "r"]:
            # Executa funcão remove
            self.remove()
        elif option in ["M", "m"]:
            # Executa função menu
            self.menu()

        # Tempo de execução
        time.sleep(0.20)

    def terminate(self):
        pass

    def menu(self):
        """Função que tem por objetivo mostrar opções ao usuário"""

        # Comando clear usando o lib os
        os.system("clear")
        # Impressão do menu na tela
        print(
            "-------------------Menu----------------------\n"
            "1 :) Add\n"
            "2 :) Remove\n"
            "3 :) Update\n"
            "4 :) List\n"
            "5 :) Terminate\n"
        )

        # Variavel que vai guardar o opção do usuário
        opcao = input("DIGITE UMA OPÇÃO:")

        # Lista que vai guardar as opções do usuário
        # opcoes = ["1", "2", "3", "4", "5"]

        # Condições para execução das opções
        if opcao == "1":
            # Execução da função add
            self.add()
        elif opcao == "2":
            # Execução da função remove
            self.remove()
        elif opcao == "3":
            # Execução da função update
            self.update()
        elif opcao == "4":
            # Execução da função get_list
            self.get_list()
        elif opcao == "5":
            # Execução da função terminate
            self.terminate()
        else:
            # Mensagem de erro para o usuario
            print("ERRRO!, Insira uma opção valida (1-5)")
            # Tempo de execução para chamar a função menu
            time.sleep(2)
            # Reexecução da função menu
            self.menu()

    def main(self):
        """Função principal para execução do programa"""

        # Comando clear para o so
        os.system("clear")

        # Condição de existencia para o arquivo de conecção com db
        if os.path.isfile("connection"):
            # Variavel que vai guardar a conecção com db
            db = sqlite3.connect("connection")
            # Tempo para conecção com db
            time.sleep(3)
            # Mensagem conecção do db para o usuário
            print("BANCO DE DADOS CONECTADO")
            # Tempo de execução
            time.sleep(3)
            # Execução da função menu
            self.menu()
        else:
            # Mensagem de erro na conecção do db
            print("ERROR! ESTA CONEXÃO NÃO EXISTE")
            # Tempo de execução
            time.sleep(3)
            # Mensagem de orientação para o usuário
            print("CRIE UM NOVO ARQUIVO DE CONEXÃO")
            # Tempo de exucução
            time.sleep(3)
            # Variavel que vai guardar a conecção com db
            db = sqlite3.connect("connection")

            # Criação de objeto para db
            cursor = db.cursor()

            # Criação da tabela
            cursor.execute(
                """CREATE TABLE contacts(Name TEXT, Phone TEXT, Address TEXT)"""
            )

            # Mensagem de retorno para o usuário
            print(
                "Conexão criada com sucesso!\n"
                "Banco de dados conectado\n"
            )

            # Tempo de execução
            time.sleep(3)
            # Execução da função menu
            self.menu()

        # Execução da função menu
        self.menu()


# Variavel que vai guardar a classe principal
contacts_manager = Manager()

# Executando a classe função main
contacts_manager.main()
