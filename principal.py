def funcao_subredes():
  rede = 0
  primeiro_ip_host = rede + 1
  divisor_total = 2 ** (int(mascara) - 24)
  broadcast = int(256 / divisor_total) - 1
  ultimo_ip_host = int(broadcast) - 1
  num_hosts = int(256 / divisor_total - 2)

  if func == 2: # Opção que mostra a tabela completa do / selecionado.
    print("\033[1;92m*  A máscara tem", divisor_total, "subredes no total, com", num_hosts, "endereços hosts em cada uma delas.  *")
    print("   Host    | Primeira IP disponivel | Último IP disponivel | Broadcast")
    for i in range(divisor_total): # Laço for para que em looping cada subrede seja printada no terminal.
        print("\033[1;92m" + principal + str(rede) + " |" 
              + "     " + principal + str(primeiro_ip_host) + "     |"
              + "     " + principal + str(ultimo_ip_host) + "     |"
              + "     " + principal + str(broadcast) + "\033[0;0m")
        rede = rede + int(256 / divisor_total)
        primeiro_ip_host = rede + 1
        broadcast = rede + int(256 / divisor_total) - 1
        ultimo_ip_host = broadcast - 1

  elif func == 3: # Opção que mostra somente a subrede específica do IP selecionado.
    print("\033[1;92m   Host    | Primeira IP disponivel | Último IP disponivel | Broadcast")
    for i in range(divisor_total): # Laço for para que o código rode por todas as subredes e pare na específica selecionada.
      if rede <= last and broadcast >= last:
        print(principal + str(rede) + " |"
          + "     " + principal + str(primeiro_ip_host) + "     |"
          + "     " + principal + str(ultimo_ip_host) + "     |"
          + "     " + principal + str(broadcast) + "\033[0;0m")
        rede = rede + int(256 / divisor_total)
        broadcast = rede + int(256 / divisor_total) - 1
      else:
        rede = rede + int(256 / divisor_total)
        primeiro_ip_host = rede + 1
        broadcast = rede + int(256 / divisor_total) - 1
        ultimo_ip_host = broadcast - 1

# Seleção das funcionalidades do programa.
ip = 0
mascara = 0
func = 0
opcao = 0
while opcao != "6":
  opcao = input("\033[1;95mDigite o número com a respectiva função que deseja trabalhar:\033[0;0m"
    "\n1. Primeira função: Selecionar novo IP."
    "\n2. Segunda função: Selecionar nova máscara."
    "\n3. Terceira função: Mostrar tabela completa da máscara selecionada."
    "\n4. Quarta função: Mostrar a subrede específica do IP selecionado."
    "\n5. Quinta função: Mostrar informações de classe e tipo do IP selecionado."
    "\n6. Sexta função: Encerrar programa.\n")

  if opcao == "1":
    exc = 0
    while exc != 1:
      ip = input("Informe o IP (exemplo: 111.111.11.1): ")

      ip_dividido = ip.split(".") # Separa a string da resposta do usuário em octetos por meio dos pontos para verificar como inteiro.
      if len(ip_dividido) != 4:
        print("IP inválido.")
        
      elif not all(oct.isdigit() for oct in ip_dividido): # Verificar se existe uma letra no endereço de IP.
        print("IP inválido.") 

      elif int(ip_dividido[0]) > 255 or int(ip_dividido[1]) > 255 or int(ip_dividido[2]) > 255 or int(ip_dividido[3]) > 255: # Verficar se existe um octeto superior a 255 endereços.
        print("IP inválido.")

      else:
        exc = 1
        principal = ip_dividido[0] + "." +  ip_dividido[1] +  "." + ip_dividido[2] + "." # Mantém os 3 primeiros octetos por eles não se alterarem nesse sistema.
        last = int(ip_dividido[3]) # Separa o último octeto para ser trabalhado.

    print("\033[1;96mIP selecionado!\033[0;0m")

  if opcao == "2":
    exc = 0
    while exc != 1:
      mascara = input(str("Coloque a máscara que deseja aplicar (de /24 até /30): "))

      mascara = mascara.replace("/", "") # Tira a barra da resposta do usuário para funcionar como inteiro.

      if not mascara.isdigit(): # Verifica se a máscara contem somente números.
        print("Máscara não suportada ou inexistente.")

      elif int(mascara) < 24 or int(mascara) > 30: # Verifica se a máscara é suportada.
        print("Máscara não suportada ou inexistente.")

      else:
        exc = 1

    print("\033[1;96mMáscara selecionada!\033[0;0m")

  if opcao == "3":
    if ip == 0 or mascara == 0:
      print("Selecione IP e máscara antes!")
    else:
      func = 2
      funcao_subredes()

  if opcao == "4":
    if ip == 0 or mascara == 0:
      print("Selecione IP e máscara antes!")
    else:
      func = 3
      funcao_subredes()

  if opcao == "5":
    if ip == 0 or mascara == 0:
      print("Selecione IP e máscara antes!")
    else:
      if int(ip_dividido[0]) <= 127:
        classe = "A"
      elif int(ip_dividido[0]) >= 128 and int(ip_dividido[0]) <= 191:
        classe = "B"
      elif int(ip_dividido[0]) >= 192 and int(ip_dividido[0]) <= 223:
        classe = "C"
      elif int(ip_dividido[0]) >= 224 and int(ip_dividido[0]) <= 239:
        classe = "D"
      else:
        classe = "E"

      if int(ip_dividido[0]) == 192 and int(ip_dividido[1]) == 168:
        tipo = "Privado"
      elif int(ip_dividido[0]) == 172 and int(ip_dividido[1]) >= 16 and int(ip_dividido[1]) <= 31:
        tipo = "Privado"
      elif int(ip_dividido[0]) == 10:
        tipo = "Privado"
      elif int(ip_dividido[0]) == 127:
        tipo = "Privado"
      else:
        tipo = "Público"

      print("\033[1;96mO IP selecionado tem classe", classe, "e tipo", tipo + ".\033[0;0m")

  if opcao == "6":
    print("Programa encerrado.")
    break