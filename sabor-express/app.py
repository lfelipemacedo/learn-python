import os

restaurantes = []

def iniciar_app():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def menu_principal():
    input("\nDigite qualquer tecla para voltar ao menu principal")
    main()


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar/Desativar Restaurante")
    print("4. Sair\n")
    
def opcao_invalida():
    print("Opção Inválida")
    menu_principal()

def cadastrar_restaurante():
    '''
        Essa função é responsável para o cadastro de um novo restaurante
        
        Inputs:
        - Nome do Restaurante
        - Categoria do Restaurante
        
        Output:
        - Adiciona um novo restaurante na lista de restaurantes
    '''
    
    exibir_subtitulo('Cadastro de Restaurantes')
    
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    
    restaurantes.append({'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False})
    
    print(f'Restaurante {nome_restaurante} foi cadastrado com sucesso!')
    menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados:')
    
    for restaurante in restaurantes:
        print(f"- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativado' if restaurante['ativo'] else 'Desativado'}")
    menu_principal()

def ativar_restaurante():
    exibir_subtitulo("Ativar/Desativar Restaurante")
    
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    
    for restaurante in restaurantes:
        restaurante_encontrado = False
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso')
            break
        if not restaurante_encontrado:
            print('Restaurante não encontrado')
    menu_principal()    
        

def escolher_opcao():
    try:
        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            cadastrar_restaurante()
        elif choice == 2:
            listar_restaurantes()
        elif choice == 3:
            ativar_restaurante()
        elif choice == 4:
            os.system("clear")
            print("Encerrando programa")
        else:
            opcao_invalida()

        # match choice:
        #     case 1:
        #         print("Cadastrando restaurante")
        #     case 2:
        #         print("Listando restaurantes")
        #     case 3:
        #         print("Ativando restaurantes")
        #     case 4:
        #         print("Encerrando programa")
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    limpar_tela()
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def limpar_tela():
    os.system('clear')
    
def main():
    limpar_tela()
    iniciar_app()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
