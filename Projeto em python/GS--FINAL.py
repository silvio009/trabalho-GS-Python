'''     Função responsável por validar o CPF do usuário e autorizar seu login como usuário no sistema!
A validaçao acontece caso o usuário insira de forma correta seu cpf e os 11 dígitos.
'''


def validar_cpf(cpf_usuario):

    if len(cpf_usuario) != 11:
        return False

    if cpf_usuario == cpf_usuario[0] * 11:
        return False

    soma = sum(int(cpf_usuario[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10 or resto == int(cpf_usuario[9]):
        pass
    else:
        return False

    soma = sum(int(cpf_usuario[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10 or resto == int(cpf_usuario[10]):
        return True
    else:
        return False


'''     Função responsável por armazenar o Menu inicial, por ser uma função, ela permite mudanças de forma simples e práticas os itens aplicados pela IA.

'''


def menu_inicia():
    print("=========================== Menu de Opções ===========================")
    print("Selecione qual Estado ou Região você está:  ")
    print(70 * "=")
    print("1. Caso você esteja na Região Sul (Digite 1)")
    print("2. Caso você esteja na Região Suldeste (Digite 2)")
    print("3. Caso você esteja na Região Centro-Oeste (Digite 3)")
    print("4. Caso você esteja na Região Norte (Digite 4)")
    print("5. Caso você esteja na Região Nordeste (Digite 5)")
    print("6. Encerrar o atendimento.")


'''
Função responsável pela interação do usuário com o Menu inicial. Através dela, é possível interagir com todas as regiões de interesse do usuário. 
Desta forma, é possível navegar pelas Regiões e acessar os itens adicionais como cultivo do solo de forma facultativa.



'''


def opcao_menu(opcao):
    if opcao == 1:
        estado_usuario = int(
            input("Você selecionou a Região Sul: \n Digite 1 para confirmar \n Digite 2 para retornar ao Menu! \n ---> "))
        if estado_usuario <= 1:
            print(
                "\n A região Sul possui influência de clima subtropical. \n Temperatura média de 12°C a 25°C. \n Recomenda-se plantio de Beterraba, Arroz e Rabanete.")

            tipo_terra = input(
                "Deseja obter informações sobre o tipo de cultivo do solo? (sim/não) \n --->")
            if tipo_terra.lower() == "sim":
                # A variável tipo_terra.lower é reponsável por identificar a forma que o usuário escreve e transcrever para letras minúsculas, oferecendo maior liberdade de escrita para o usuário.
                print("Para o cultivo adequado é necessário observar os seguintes fatores: \n -  Solos arenosos e argilosos, ricos em matéria orgânica e possuir um pH entre 5,5 e 7,5.")
        else:
            menu_inicia()

            escolha_opcao = int(input("Digite o número da opção que deseja: "))

            resultado_opcao = opcao_menu(escolha_opcao)
            # Volta para o Menu
    elif opcao == 2:
        estado_usuario = int(input(
            "Você selecionou a Região Sudeste: \n Digite 1 para confirmar \n Digite 2 para retornar ao Menu! \n ---> "))
        if estado_usuario <= 1:
            print(
                " \n A região Sudeste possui influência de clima tropical. \n Temperatura média entre 18°C a 24°C. \n Recomenda-se plantio de Café, Feijão e Abacaxi.")

            tipo_terra = input(
                "Deseja obter informações sobre o tipo de cultivo do solo? (sim/não) \n ---> ")

            if tipo_terra.lower() == "sim":
                # A variável tipo_terra.lower é reponsável por identificar a forma que o usuário escreve e transcrever para letras minúsculas, oferecendo maior liberdade de escrita para o usuário.
                print("Para o cultivo adequado é necessário observar os seguintes fatores: \n -  Solos férteis, bem drenados e ricos em matéria orgânica. \n - O pH do solo recomendado varia 4,5 e 7,5.")

        else:
            menu_inicia()

            escolha_opcao = int(input("Digite o número da opção que deseja: "))

            resultado_opcao = opcao_menu(escolha_opcao)
            # Volta para o Menu

    elif opcao == 3:
        estado_usuario = int(input(
            "Você selecionou a Região Centro-Oeste: \n Digite 1 para confirmar \n Digite 2 para retornar ao Menu! \n ---> "))
        if estado_usuario <= 1:
            print(
                " \n A região Centro-Oeste possui influência de clima tropical com período chuvoso(Outubro a Março) e uma estação seca. \n Temperatura média entre 22°C a 28°C. \n Recomenda-se plantio de Soja, Milho e Feijão.")

            tipo_terra = input(
                "Deseja obter informações sobre o tipo de cultivo do solo? (sim/não) \n --->")

            if tipo_terra.lower() == "sim":
                # A variável tipo_terra.lower é reponsável por identificar a forma que o usuário escreve e transcrever para letras minúsculas, oferecendo maior liberdade de escrita para o usuário.
                print(" Para o cultivo adequado é necessário observar os seguintes fatores: \n - Solos com boa capacidade de retenção de água e ricos em matéria orgânica. \n - O pH do solo recomendado varia entre 5,8 a 7,5.")
            else:
                return
        else:
            menu_inicia()

            escolha_opcao = int(input("Digite o número da opção que deseja: "))

            resultado_opcao = opcao_menu(escolha_opcao)
            # Volta para o Menu

    elif opcao == 4:
        estado_usuario = int(input(
            "Você selecionou a Região Norte: \n Digite 1 para confirmar \n Digite 2 para retornar ao Menu! \n ---> "))
        if estado_usuario <= 1:
            print(
                " \n A região Norte  possui influência de clima equatorial, temperaturas elevadas e alta umidade. \n Temperatura média entre 24°C a 32°C. \n Recomenda-se plantio de Mandioca, Milho e Arroz.")

            tipo_terra = input(
                "Deseja obter informações sobre o tipo de cultivo do solo? (sim/não) \n --->")

            if tipo_terra.lower() == "sim":
                # A variável tipo_terra.lower é reponsável por identificar a forma que o usuário escreve e transcrever para letras minúsculas, oferecendo maior liberdade de escrita para o usuário.
                print("Para o cultivo adequado é necessário observar os seguintes fatores: \n - Solos profundos de textura média a arenosa. \n - O ph do solo recomendado varia entre 5,5 a 7,0.")
            else:
                return
        else:
            menu_inicia()

            escolha_opcao = int(input("Digite o número da opção que deseja: "))

            resultado_opcao = opcao_menu(escolha_opcao)
            # Volta para o Menu

    elif opcao == 5:
        estado_usuario = int(input(
            "Você selecionou a Região Nordeste: \n Digite 1 para confirmar \n Digite 2 para retornar ao Menu! \n ---> "))
        if estado_usuario <= 1:
            print(
                " \n Região Nordeste  possui influência de clima tropical, com elevadas temperaturas e temporada de secas. \n Temperatura média entre 25°C a 32°C. \n Recomenda-se plantio de Graviola, Cana-de-Açúcar e Milho.")

            tipo_terra = input(
                "Deseja obter informações sobre o tipo de cultivo do solo? (sim/não) \n --->")

            if tipo_terra.lower() == "sim":
                # A variável tipo_terra.lower é reponsável por identificar a forma que o usuário escreve e transcrever para letras minúsculas, oferecendo maior liberdade de escrita para o usuário.
                print("Para o cultivo adequado é necessário observar os seguintes fatores: \n - Solos profundos e bem drenados, evitar o excesso de água. \n - O pH do solo recomendado varia entre 5,5 a 6,5.")
            else:
                return
        else:
            menu_inicia()

            escolha_opcao = int(input("Digite o número da opção que deseja: "))

            resultado_opcao = opcao_menu(escolha_opcao)
            # Volta para o Menu

    if opcao == 6:
        print("Encerrando atendimento! Obrigado!!")
        exit()


''' Função responsável por mostrar os tipos de pragas mais comuns no Brasil, por meio desta, permite-se maior flexibilidade em alterações futuras.
A estrutura de listas permite maior agilidade nas trocas.
'''


def combate_pragas():

    print("============================== PRAGAS ==============================")

    print("Pragas agrícolas são organismos que se alimentam de cultivos agrícolas, reduzindo sua qualidade e produtividade. \n Saiba mais sobre as pragas mais comuns no Brasil! ")

    pragas_agricultura = ["Lagarta-do-cartucho", "Mosca-branca",
                          "Broca-do-colo", "Broca-do-fruto", "Lagarta-da-maçã"]

    print("-- Região Sul ||",
          (pragas_agricultura[0]), "- Biológico: Nesse método, são utilizados inimigos naturais da lagarta-do-cartucho, como parasitoides e predadores. \n -- O uso de insetos benéficos, como algumas espécies de vespas parasitoides, pode ser eficaz.")
    print(120 * "-")
    print("-- Região Sudeste ||",
          (pragas_agricultura[1]), "- Biológico: O uso de inimigos naturais da mosca-branca pode ser uma estratégia eficaz de controle.\n -- Alguns exemplos são as joaninhas e vespas parasitoides. A introdução e conservação desses inimigos naturais pode ajudar a controlar a população da praga.")
    print(120 * "-")
    print("-- Região Centro-Oeste ||",
          (pragas_agricultura[2]), "- Biológico: Existem alguns agentes de controle biológico que podem ser usados no combater. \n-- Algumas espécies de vespas parasitoides, como a Cephalonomia stephanoderis, são conhecidas por parasitar as larvas da praga.")
    print(120 * "-")
    print("-- Região Norte ||", (pragas_agricultura[3]), "- Biológico:  As larvas dessa praga se alimentam das frutas, causando danos significativos e diminuindo a qualidade dos frutos. \n-- Joaninhas ou Vespas, como a Trichogramma spp.(pequenas vespas), depositam seus ovos nos ovos da praga, impedindo seu desenvolvimento.")
    print(120 * "-")
    print("-- Região Nordeste ||",
          (pragas_agricultura[4]), "- Biológico: Algumas espécies de parasitoides, como Trichogramma spp.(pequenas vespas), depositam seus ovos nos ovos da praga, impedindo o seu desenvolvimento. \n-- O uso de insetos predadores, como joaninhas e crisopídeos, também pode ajudar no controle da praga.")
    print(120 * "-")

    print("                                               *ATENÇÃO*                                               ")
    print("Uso de inseticidas: Em casos de infestações severas, pode ser necessário utilizar inseticidas para controle.\n --> É importante escolher inseticidas registrados e recomendados para essa praga específica. \n --> Recomenda-se usar inseticidas seletivos que causem o menor impacto possível!")


# Estrutura de repetição responsável pelo login do cliente junto com a funçao validar_cpf.
while True:
    print("                     ! Seja Bem-vindo ao Menu J.A.R.V.I.S !                       ")
    print("Somos uma empresa que busca o cultivo mais eficiente e sustentável para o amanhã. ")
    nome_user = input("Digite o seu Nome:  ")

    cpf_usuario = input("Digite o CPF para validar o usuário: ")
    if validar_cpf(cpf_usuario):

        valida_usuario = "Seja bem-vindo: " + nome_user
        print(valida_usuario)
        print("CPF válido. Usuário identificado!")
        break
    else:
        print("CPF inválido.Tente novamente.")

#Chamada de função!
menu_inicia()

escolha_opcao = int(input("Digite o número da opção que deseja:  "))

resultado_opcao = opcao_menu(escolha_opcao)


print(70 * "-")
info_praga = int(input(
    "Você gostaria de saber mais sobre controle de pragas? \n \n Digite: 1 para SIM! \n         2 para NÃO!  \n --> "))
if info_praga == 1:

    combate_pragas()
else:

    print("Prossiga!")

'''Estrutura final responável por formatar o número do cpf do usuário e retornar a formatação do CPF de forma clara juntamente com o número de protoco gerado automaticamente, facilitando futuras consultas.
'''
opcao_retorno = 0
while opcao_retorno != 1:
    print(75 * "=")

    import random
    numero_protocolo = random.randint(100, 9999)

    cpf_format = cpf_usuario[:3] + '.' + cpf_usuario[3:6] + \
        '.' + cpf_usuario[6:9] + '-' + cpf_usuario[9:]

    print("|| Usuário: ", nome_user, "| CPF: ", cpf_format,
          " |  Seu protocolo é: ", numero_protocolo, "||")

    print(75 * "=")
    print("1. Finalizar solicitação!")
    print("2. Gostaria de fazer uma nova análise?")

    opcao_retorno = input("Digite o número da opção: ")

    if opcao_retorno == "1":
        print("Descubra o futuro através de seus próprios olhos!   ||J.A.R.V.I.S||  ")
        exit()

    else:
        # Caso o usuário deseje recomeçar a pesquisa, é possível atráves deste laço de condição.
        opcao_retorno == "2"
    menu_inicia()

    escolha_opcao = int(input("Digite o número da opção que deseja: "))

    resultado_opcao = opcao_menu(escolha_opcao)
    combate_pragas()
