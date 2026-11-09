
print("====================================")
print("   MONITORAMENTO DE SERVIDORES")
print("====================================")

servidores = []
cpus = []
memorias = []

while True:
    print("\n========== MENU ==========")
    print("1 - Cadastrar servidor")
    print("2 - Listar servidores")
    print("3 - Consultar servidor")
    print("4 - Atualizar uso do servidor")
    print("5 - Verificar alertas")
    print("6 - Relatório geral")
    print("7 - Excluir servidor")
    print("8 - Sair")
    print("==========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CADASTRAR SERVIDOR ---")

        nome = input("Nome do servidor: ")
        cpu = float(input("Uso da CPU (%): "))
        memoria = float(input("Uso da memória (%): "))

        if nome == "" or cpu < 0 or cpu > 100 or memoria < 0 or memoria > 100:
            print("Erro: dados inválidos!")

        elif nome in servidores:
            print("Erro: servidor já cadastrado!")

        else:
            servidores.append(nome)
            cpus.append(cpu)
            memorias.append(memoria)

            print("\nServidor cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE SERVIDORES ---")

        if len(servidores) == 0:
            print("Nenhum servidor cadastrado!")

        else:
            for i in range(len(servidores)):
                print("\n--------------------------")
                print("Servidor:", servidores[i])
                print(f"CPU: {cpus[i]:.1f}%")
                print(f"Memória: {memorias[i]:.1f}%")

                if cpus[i] >= 90 or memorias[i] >= 90:
                    print("Status: CRÍTICO")

                elif cpus[i] >= 80 or memorias[i] >= 80:
                    print("Status: ALERTA")

                else:
                    print("Status: NORMAL")

    elif opcao == "3":
        print("\n--- CONSULTAR SERVIDOR ---")

        nome = input("Nome do servidor: ")
        encontrado = False

        for i in range(len(servidores)):
            if servidores[i] == nome:
                encontrado = True

                print("\nServidor:", servidores[i])
                print(f"Uso da CPU: {cpus[i]:.1f}%")
                print(f"Uso da memória: {memorias[i]:.1f}%")

                if cpus[i] >= 90 or memorias[i] >= 90:
                    print("Status: CRÍTICO")

                elif cpus[i] >= 80 or memorias[i] >= 80:
                    print("Status: ALERTA")

                else:
                    print("Status: NORMAL")

                break

        if encontrado == False:
            print("Servidor não encontrado!")

    elif opcao == "4":
        print("\n--- ATUALIZAR SERVIDOR ---")

        nome = input("Nome do servidor: ")
        encontrado = False

        for i in range(len(servidores)):
            if servidores[i] == nome:
                encontrado = True

                nova_cpu = float(input("Novo uso da CPU (%): "))
                nova_memoria = float(input("Novo uso da memória (%): "))

                if nova_cpu < 0 or nova_cpu > 100 or nova_memoria < 0 or nova_memoria > 100:
                    print("Erro: valores inválidos!")

                else:
                    cpus[i] = nova_cpu
                    memorias[i] = nova_memoria

                    print("Servidor atualizado com sucesso!")

                    if cpus[i] >= 90 or memorias[i] >= 90:
                        print("ATENÇÃO: SERVIDOR EM ESTADO CRÍTICO!")

                    elif cpus[i] >= 80 or memorias[i] >= 80:
                        print("ALERTA: USO ELEVADO DE RECURSOS!")

                break

        if encontrado == False:
            print("Servidor não encontrado!")

    elif opcao == "5":
        print("\n--- ALERTAS DO SISTEMA ---")

        alertas = 0

        for i in range(len(servidores)):
            if cpus[i] >= 90 or memorias[i] >= 90:
                print("\nALERTA CRÍTICO!")
                print("Servidor:", servidores[i])
                print(f"CPU: {cpus[i]:.1f}%")
                print(f"Memória: {memorias[i]:.1f}%")

                alertas = alertas + 1

            elif cpus[i] >= 80 or memorias[i] >= 80:
                print("\nALERTA DE UTILIZAÇÃO!")
                print("Servidor:", servidores[i])
                print(f"CPU: {cpus[i]:.1f}%")
                print(f"Memória: {memorias[i]:.1f}%")

                alertas = alertas + 1

        if alertas == 0:
            print("Nenhum alerta identificado!")

        else:
            print("\nTotal de servidores em alerta:", alertas)

    elif opcao == "6":
        print("\n--- RELATÓRIO GERAL ---")

        total = len(servidores)
        normais = 0
        alertas = 0
        criticos = 0
        soma_cpu = 0
        soma_memoria = 0

        for i in range(total):
            soma_cpu = soma_cpu + cpus[i]
            soma_memoria = soma_memoria + memorias[i]

            if cpus[i] >= 90 or memorias[i] >= 90:
                criticos = criticos + 1

            elif cpus[i] >= 80 or memorias[i] >= 80:
                alertas = alertas + 1

            else:
                normais = normais + 1

        print("Total de servidores:", total)
        print("Servidores normais:", normais)
        print("Servidores em alerta:", alertas)
        print("Servidores críticos:", criticos)

        if total > 0:
            media_cpu = soma_cpu / total
            media_memoria = soma_memoria / total

            print(f"\nMédia de uso da CPU: {media_cpu:.1f}%")
            print(f"Média de uso da memória: {media_memoria:.1f}%")

        else:
            print("\nNenhum servidor cadastrado!")

    elif opcao == "7":
        print("\n--- EXCLUIR SERVIDOR ---")

        nome = input("Nome do servidor: ")
        encontrado = False

        for i in range(len(servidores)):
            if servidores[i] == nome:
                servidores.pop(i)
                cpus.pop(i)
                memorias.pop(i)

                print("Servidor excluído com sucesso!")
                encontrado = True
                break

        if encontrado == False:
            print("Servidor não encontrado!")

    elif opcao == "8":
        print("\nEncerrando monitoramento...")
        print("Sistema finalizado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
