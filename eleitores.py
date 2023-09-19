#   Gabriel de Angelo Fukuoka - 32329377
#   Mateus Alonso Varjão - 32334001
#   Leonardo Magalhães - 32318359
#MENU
#========================================================================================================================================#
#condição para finalizar menu
finalizar_menu = 0

#listas utilizadas
candidatos_presidente = []
candidatos_governador = []
candidatos_prefeito = []
lista_eleitores = [] 
votos_prefeito = []
votos_governador = []
votos_presidente = []
while finalizar_menu != 1:
    print("[=============== /// SIMULADOR DO SISTEMA DE VOTAÇÃO /// ===============]")
    opcao_menu = int(input("""                  [ 1 ] CADASTRAR CANDIDATOS
                  [ 2 ] CADASTRAR ELEITORES
                  [ 3 ] VOTAR
                  [ 4 ] APURAR RESULTADOS
                  [ 5 ] RELÁTORIO E ESTATÍSTICAS
                  [ 6 ] GRAVAR APURAÇÃO
                  [ 7 ] ENCERRAR

Opção escolhida: """))

    #opção para cadastrar candidatos
    if opcao_menu == 1:
        #CADASTRAR CANDIDATOS
        #lista para cada cargo
        print("[=============== /// CADASTRANDO CANDIDATOS /// ===============]")
        #condição para encerrar o código de forma organica
        finalizar_candidatos= 0 
        while finalizar_candidatos!= 1:

            #definir três funções para adicionar os candidatos, uma para cada cargo disponível
            def adicionar_presidente(nome, idade, partido, cargo, numero):
                candidato = {'Nome': nome, 'Idade': idade, 'Partido': partido, 'Cargo': cargo, 'Numero': numero}
                candidatos_presidente.append(candidato)

            def adicionar_governador(nome, idade, partido, cargo, numero):
                candidato = {'Nome': nome, 'Idade': idade, 'Partido': partido, 'Cargo': cargo, 'Numero': numero}
                candidatos_governador.append(candidato)
                
            def adicionar_prefeito(nome, idade, partido, cargo, numero):
                candidato = {'Nome': nome, 'Idade': idade, 'Partido': partido, 'Cargo': cargo, 'Numero': numero}
                candidatos_prefeito.append(candidato)

            #dados do candidato, juntamente com a opção de cargo
            votos = 0
            print("=============================================================================")
            nome_candidato = input("Nome do candidato: ")
            numero_candidato = int(input("Número do candidato: "))
            idade_candidato = int(input("Idade: "))
            partido_candidato = input("Partido: ")
            cargo_candidato = int(input("""Cargo: 
[ 1 ] Presidente 
[ 2 ] Governador
[ 3 ] Prefeito
= """))
            #condições para adicionar os dados dos candidatos na lista determinada pelo cargo
            if cargo_candidato == 1:
                adicionar_presidente(nome_candidato, idade_candidato, partido_candidato, cargo_candidato, numero_candidato)
            
            elif cargo_candidato == 2:
                adicionar_governador(nome_candidato, idade_candidato, partido_candidato, cargo_candidato, numero_candidato)
            
            elif cargo_candidato == 3:
                adicionar_prefeito(nome_candidato, idade_candidato, partido_candidato, cargo_candidato, numero_candidato)
            
            else:
                print("Opção inválida: ")
            
            #opção de finalizar o código
            print("=============================================================================")
            continuar_cadastro = int(input("""Deseja cadastrar outro candidato: 
[ 1 ] Sim
[ 2 ] Não
= """))
            #condição de saida, caso cliente escolher a opção 2 o while é finalizado
            if continuar_cadastro == 2:
                    finalizar_candidatos = finalizar_candidatos + 1
            elif continuar_cadastro != 1 and continuar_cadastro != 2:
                    print("Opção inválida!")

    #opção para cadastrar eleitores
    elif opcao_menu == 2:
        print("[=============== /// CADASTRANDO ELEITORES /// ===============]")

        #condição de saida para não cadastrar mais eleitores
        finalizar_eleitores = 0
        while finalizar_eleitores != 1:

            #função para adicionar eleitores na lista
            def adicionar_eleitores(nome, cpf):
                eleitor = {'Nome': nome, 'CPF': cpf}
                lista_eleitores.append(eleitor)

            #dados do eleitor
            print("=============================================================================")
            nome_eleitor = input("Nome do eleitor: ")
            cpf_eleitor = int(input("CPF (Apenas números): "))
            adicionar_eleitores(nome_eleitor, cpf_eleitor)
            print("=============================================================================")
            continuar_cadastro = int(input("""Deseja cadastrar outro eleitor: 
[ 1 ] Sim
[ 2 ] Não
= """))
            
            #condição de saida, caso cliente escolher a opção 2 o while é finalizado
            if continuar_cadastro == 2:
                finalizar_eleitores = finalizar_eleitores + 1
            elif continuar_cadastro != 1 and continuar_cadastro != 2:
                    print("Opção inválida!")  

    #opção para realizar votação
    elif opcao_menu == 3:
        #condição para finalizar a votação
        finalizar_votacao = 0
        print("")
        print("[=============== /// REALIZAR VOTAÇÃO /// ===============]")
        
        #função para verificar se o CPF do eleitor já foi cadastrado
        def verificar_cpf(cpf):
            for eleitor in lista_eleitores:
                if eleitor["CPF"] == cpf:
                    return True
            return False
        
        #função para exibir o candidato para o eleitor confirmar na hora da votação
        def exibir_candidato(candidato):
            print("Nome: " + candidato["Nome"])
            print("Partido: " + candidato["Partido"])

        #função para confirmar o voto nulo
        def confirmar_nulo(confirmacao):
            confirmacao = int(input("""Confirmar voto nulo:
[ 1 ] Sim
[ 2 ] Não
= """))     
            if confirmacao == 1:
                print("=============================================================================")
                print("Voto registrado!")
            else:
                print("Voto cancelado! ")
        
        #função para confirmar o voto em branco
        def confirmar_branco(confirmacao):
            confirmacao = int(input("""Confirmar voto em branco:
[ 1 ] Sim
[ 2 ] Não
= """))     
            if confirmacao == 1:
                print("Voto registrado!")
            else:
                print("Voto cancelado! ")

        #função para coletar voto para candidatos a presidencia 
        def votar_presidente(cpf):
            print("""
------------------------- CANDIDATOS A PRESIDENCIA: -------------------------
======================""")
            for candidato in candidatos_presidente:
                print(f"""Número: {candidato['Numero']}
Nome: {candidato['Nome']}
Partido: {candidato['Partido']}
======================""")
            voto = int(input("""
[ NUMERO DO CANDIDATO ] PARA ESCOLHER CANDIDATO
[ -1 ] PARA VOTO EM BRANCO
[ -2 ] PARA VOTO NULO
= """))     
            confirmar_voto = int(input("""Confirmar voto: 
[ 1 ] SIM
[ 2 ] NÃO 
= """))
            if confirmar_voto == 1:
                print("=============================================================================")
                print("Voto confirmado! ")
                print("=============================================================================")
                votos_presidente.append({"CPF": cpf, "Voto": voto})
            else:
                print("voto cancelado!")


        
        #função para coletar votos de candidatos a governador
        def votar_governador(cpf):
            print("""
------------------------- CANDIDATO A GOVERNADOR: ---------------------------
======================""")
            for candidato in candidatos_governador:
                print(f"""Número: {candidato['Numero']}
Nome: {candidato['Nome']}
Partido: {candidato['Partido']}
======================""")
            voto = int(input("""
[ NUMERO DO CANDIDATO ] PARA ESCOLHER CANDIDATO
[ -1 ] PARA VOTO EM BRANCO
[ -2 ] PARA VOTO NULO
= """))     
            print("=============================================================================")
            confirmar_voto = int(input("""Confirmar voto: 
[ 1 ] SIM
[ 2 ] NÃO 
= """))
            if confirmar_voto == 1:
                print("=============================================================================")
                print("Voto confirmado! ")
                print("=============================================================================")
                votos_governador.append({"CPF": cpf, "Voto": voto})
            else:
                print("voto cancelado!")

        #função para coletar votos dos candidatos a prefeito
        def votar_prefeito(cpf):
            print("""
------------------------- CANDIDATO A PREFEITO: -----------------------------
======================""")
            for candidato in candidatos_prefeito:
                print(f"""Número: {candidato['Numero']}
Nome: {candidato['Nome']}
Partido: {candidato['Partido']}
======================""")
            voto = int(input("""
[ NUMERO DO CANDIDATO ] PARA ESCOLHER CANDIDATO
[ -1 ] PARA VOTO EM BRANCO
[ -2 ] PARA VOTO NULO
= """))     
            confirmar_voto = int(input("""Confirmar voto: 
[ 1 ] SIM
[ 2 ] NÃO 
= """))
            if confirmar_voto == 1:
                print("=============================================================================")
                print("Voto confirmado! ")
                print("=============================================================================")
                votos_prefeito.append({"CPF": cpf, "Voto": voto})
            else:
                print("voto cancelado!")            

        #realizar votação
        while finalizar_votacao != 1:
            cpf = int(input("Digite seu CPF (apenas números): "))
            if verificar_cpf(cpf):
                votar_presidente(cpf)
                votar_governador(cpf)
                votar_prefeito(cpf)
                opcao_eleitor = int(input("""Realizar votação de outro eleitor?
[ 1 ] Sim
[ 2 ] Não
= """))
                
                #condição de saida, caso cliente escolher a opção 2 o while é finalizado
                if opcao_eleitor == 2:
                    finalizar_votacao = finalizar_votacao + 1
                elif continuar_cadastro != 1 and continuar_cadastro != 2:
                    print("Opção inválida!")
            else:
                ("CPF não localizado. Tente novamente!")

    #opção para apurar resultados
    elif opcao_menu == 4:
        def apurar_resultados():
            # Apuração dos votos para cada cargo
            resultado_presidente = apurar_votos(candidatos_presidente, votos_presidente)
            resultado_governador = apurar_votos(candidatos_governador, votos_governador)
            resultado_prefeito = apurar_votos(candidatos_prefeito, votos_prefeito)
        
            # Mostrar os candidatos vencedores para cada cargo
            print("\n====================== RESULTADO DA APURAÇÃO ======================")
            print("---------------------------------------------------------------------")
            print("////////////////////// CANDIDATOS VENCEDORES POR CARGO //////////////////////")
            print("Presidente: ", resultado_presidente[0]["Nome"], "- Número: ", resultado_presidente[0]["Numero"])
            print("Governador: ", resultado_governador[0]["Nome"], "- Número: ", resultado_governador[0]["Numero"])
            print("Prefeito: ", resultado_prefeito[0]["Nome"], "- Número: ", resultado_prefeito[0]["Numero"])
            print("---------------------------------------------------------------------")
        
            # Geração do ranking
            print("\n====================== RANKING DOS CANDIDATOS ======================")
            print("////////////////////// Presidente //////////////////////")
            exibir_ranking(resultado_presidente)
            print("\n////////////////////// Governador //////////////////////")
            exibir_ranking(resultado_governador)
            print("\n////////////////////// Prefeito //////////////////////")
            exibir_ranking(resultado_prefeito)

        def apurar_votos(candidatos, votos):
            resultado = []
        
            #Realizar a contagem de voto para cada candidato cadastrado
            for candidato in candidatos:
                quantidade_votos = 0
                for voto in votos:
                    if voto["Voto"] == candidato["Numero"]:
                        quantidade_votos += 1
                resultado.append({"Nome": candidato["Nome"], "Numero": candidato["Numero"], "Votos": quantidade_votos, "Idade": candidato["Idade"]})
        
            #Ordenação do resultado por quantidade de votos e idade (critério de desempate)
            resultado.sort(key=lambda x: (x["Votos"], x["Idade"]), reverse=True)
        
            return resultado
        
        #Função para exibir o ranking da votação, juntamente com uma lista para cada cargo (guardando a quantidade de votos para especificar na apuração)
        resultado_votos_presidente = []
        resultado_votos_governador = []
        resultado_votos_prefeito = []
        def exibir_ranking(resultado):
            for candidato in candidatos_presidente:
                total_votos = votos_prefeito.count(candidato)
                resultado_votos_presidente.append((candidato, total_votos))

            for candidato in candidatos_governador:
                total_votos = votos_governador.count(candidato)
                resultado_votos_governador.append((candidato, total_votos))

            for candidato in candidatos_prefeito:
                total_votos = votos_prefeito.count(candidato)
                resultado_votos_prefeito.append((candidato, total_votos))
            numero_de_eleitores = len(lista_eleitores)

            #Contagem de votos nulos e brancos dentro das listas de voto 
            total_brancos = 0
            total_nulos = 0
            for cpf, voto in votos_presidente:
                if voto == -1:
                    total_brancos = total_brancos + 1
                elif voto == -2:
                    total_nulos = total_nulos + 1

            for cpf, voto in votos_governador:
                if voto == -1:
                    total_brancos = total_brancos + 1
                elif voto == -2:
                    total_nulos = total_nulos + 1

            for cpf, voto in votos_prefeito:
                if voto == -1:
                    total_brancos = total_brancos + 1
                elif voto == -2:
                    total_nulos = total_nulos + 1

            print("---------------------------------------------------")
            print("  Número  |       Nome       |  Votos  |  Idade  ")
            print("---------------------------------------------------")
            for i, candidato in enumerate(resultado):
                print(f"    {candidato['Numero']:02d}    | {candidato['Nome']:15s} | {candidato['Votos']:6d}  |   {candidato['Idade']:3d}   |")

                total_votos_validos = numero_de_eleitores - total_brancos - total_nulos
                total_votos = total_votos_validos + total_brancos + total_nulos
                porcentagem_votos_validos = total_votos / (numero_de_eleitores - total_brancos - total_nulos) * 100
                porcentagem_votos_brancos = (total_brancos / numero_de_eleitores) * 100
                porcentagem_votos_nulos = (total_nulos / numero_de_eleitores) * 100

            print("---------------------------------------------------")
            print("Total de votos: ", total_votos)
            print(f"Total de votos válidos: {total_votos_validos} - {porcentagem_votos_validos}%")
            print(f"Total de votos brancos: {total_brancos} - {porcentagem_votos_brancos}")
            print(f"Total de votos nulos: {total_nulos} - {porcentagem_votos_nulos}")

    # Chamar a função para apurar os resultados
        apurar_resultados()

    #opção para o relatório e estatísticas
    elif opcao_menu == 5:
        def relatorio_estatisticas():
            #exibindo lista dos eleitores que votaram (ordenado por nome)
            lista_eleitores_ordenador = sorted(lista_eleitores, key=lambda x: x["Nome"])
            print("====================== NOME DOS ELEITORES QUE VOTARAM ======================")
            for eleitor in lista_eleitores_ordenador:
                print("------------")
                print(eleitor["Nome"])

            #verificando se a votação foi auditada, comparando o número de eleitores bate com os votos
            total_eleitores = len(lista_eleitores)
            for eleitor in lista_eleitores:
                total_votos = len(set([eleitor["Nome"]]))   
            if total_eleitores * 3  == total_votos: 
                print("---------------------")  
                print("Votação Auditada!") 
                print("---------------------") 
            else:
                print("---------------------") 
                print("Problema na Auditoria!") 
                print("---------------------") 
            
            #politicos por partido

        
        #chamar função
        relatorio_estatisticas()


    #opção para finalizar programa
    elif opcao_menu == 7:
        print("[=============== /// FINALIZANDO PROGRAMA1 /// ===============]")
        finalizar_menu = finalizar_menu + 1












        


                            
    