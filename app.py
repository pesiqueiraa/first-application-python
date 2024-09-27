import os 

restaurantes = [{"nome":"Pizza", "categoria": "Pizzaria", "ativo": False},
                {"nome":"Japa", "categoria": "Japonesa", "ativo": True}]

def exibir_nome():
    print('''
          
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
          ''')

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("App finalizado")

def voltar_ao_menu():
    input("Digite uma tecla para ele voltar para o menu principal\n")
    main()

def opcao_invalida():
    print("Opcao Invalida")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
def cadastrar_restaunte():
        exibir_subtitulo("Cadastro de novos restaurantes")
        nome_do_restaurante = input("Qual nome do restaurante que deseja cadastrar? ")
        categoria_restaunte = input(f"Digite a categoria do restaurante {nome_do_restaurante}? ")
        dados_do_restaurante = {"nome": nome_do_restaurante, 'categoria': categoria_restaunte, 'ativo': False}
        restaurantes.append(dados_do_restaurante)
        print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n")
        voltar_ao_menu()   
        
    
def listar_restauntes():
    exibir_subtitulo("Listando os restaurantes..\n")
    
    print(f"{"  Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status")
    
    for i in restaurantes:
        nome_restaurante = i["nome"]
        categoria_restaurante = i["categoria"]
        ativo_restautante = 'ativado' if i["ativo"] else 'desativado'
        print(f".{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restautante}")
    
    voltar_ao_menu()
    
def alterar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if(restaurante["nome"] == nome_restaurante):
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            print(f"Estado do restaurante {restaurante["nome"]} alterado com sucesso")
    if not restaurante_encontrado:
        print("Restaurante não encontrado")
    
    voltar_ao_menu()


def escolher_opcao():
    try:
        decisao = int(input("Escolha uma opcao: "))
        if (decisao == 1):
            cadastrar_restaunte()
        elif (decisao == 2):
            listar_restauntes()
        elif (decisao == 3):
            alterar_estado_restaurante()
        elif (decisao == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()