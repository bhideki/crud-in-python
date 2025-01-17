
AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print("----------------------")
    else:
        print("Agenda vazia.")


def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["tel"])
        print("Email:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
    except KeyError:
        print("Contato Inexistente!")
    except Exception as error:
        print("Um erro inesperado ocorreu")
        print(error)

def ler_detalhes_contato():
    tel = int(input("Digite o telefone do contato: "))
    email = str(input("Digite o email do contato: "))
    endereco = str(input("Digite o endereço do contato: "))
    return tel, email, endereco


def incluir_editar_contato(contato,tel, email,endereco):


    AGENDA[contato] = {
        "tel": tel,
        "email": email,
        "endereco": endereco,
    }
    salvar()
    print("Contato {} adicionado/editado com sucesso!".format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print("Contato {} removido com sucesso!".format(contato))
        print()
    except KeyError:
        print("Contato Inexistente!")
    except Exception as error:
        print("Um erro inesperado ocorreu")
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                tel = AGENDA[contato]["tel"]
                email = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]
                arquivo.write("{},{},{},{}\n".format(contato,tel,email,endereco))
        print("Contato exportado com sucesso!")
    except Exception as error:
        print("algum erro ocorreu ao exportar")
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome,tel,email,endereco)

    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print("Um erro inesperado ocorreu")
        print(error)

def salvar():
    exportar_contatos("database.csv")

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    "tel": tel,
                    "email": email,
                    "endereco": endereco,
                }
        print('database exportada com sucesso!')
        print('{} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print("Um erro inesperado ocorreu")
        print(error)



def imprimir_menu():
    print("1 - Mostrar contatos da agenda")
    print("2 - Buscar contatos da agenda")
    print("3 - Incluir contato da agenda")
    print("4 - Editar contato da agenda")
    print("5 - Excluir contato da agenda")
    print("6 - Exportar contatos para CSV")
    print("7 - Importar contatos CSV")
    print("0 - Fechar agenda")


#INICIO DO PROGRAMA

carregar()
while True:
    imprimir_menu()

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        mostrar_contatos()
    elif opcao == 2:
        contato = str(input("Digite o nome do contato: "))
        buscar_contato(contato)
    elif opcao == 3:
        contato = str(input("Digite o nome do contato: "))

        try:
            AGENDA[contato]
            print("Contato já existente:", contato)
        except KeyError:
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)
    elif opcao == 4:
        contato = str(input("Digite o nome do contato: "))

        try:
            AGENDA[contato]
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato,tel, email,endereco)
        except KeyError:
            print("Contato Inexistente!")
    elif opcao == 5:
        contato = str(input("Digite o nome do contato: "))
        excluir_contato(contato)
    elif opcao == 6:
        nome_do_arquivo = input("Digite o nome do arquivo: ")
        exportar_contatos()
    elif opcao == 7:
        nome_do_arquivo = input("Digite o nome do arquivo: ")
        importar_contatos(nome_do_arquivo)
    elif opcao == 0:
        print("Fechando agenda")
        break
    else:
        print("Opção invalida!")