# Opção que mostra a tabela completa do / selecionado.
def segunda_funcao():
  host = 0
  primeiro_ip = host + 1
  divisor_total = 2 ** (int(mascara) - 24)
  broadcast = int(256 / divisor_total) - 1
  ultimo_ip = int(broadcast) - 1

  print("A máscara tem", divisor_total, "subredes no total.")
  print("   Host    | Primeira IP disponivel " +
        "| Último IP disponivel | Broadcast")
  for i in range(divisor_total):
      print(principal + str(host) + " |" + "     " 
            + principal + str(primeiro_ip) + "     |"
            + "     " + principal + str(ultimo_ip) + "     |"
            + "     " + principal + str(broadcast))
      host = host + int(256 / divisor_total)
      primeiro_ip = host + 1
      broadcast = host + int(256 / divisor_total) - 1
      ultimo_ip = broadcast - 1

# Opção que mostra somente a subrede específica do IP selecionado.
def terceira_funcao():
  host = 0
  primeiro_ip = host + 1
  divisor_total = 2 ** (int(mascara) - 24)
  broadcast = int(256 / divisor_total) - 1
  ultimo_ip = int(broadcast) - 1

  print("   Host    | Primeira IP disponivel " +
        "| Último IP disponivel | Broadcast")
  for i in range(divisor_total):
    if host <= last and broadcast >= last:
      print(principal + str(host) + " |"
        + "     " + principal + str(primeiro_ip) + "     |"
        + "     " + principal + str(ultimo_ip) + "     |"
        + "     " + principal + str(broadcast))
      host = host + int(256 / divisor_total)
      broadcast = host + int(256 / divisor_total) - 1
    else:
      host = host + int(256 / divisor_total)
      primeiro_ip = host + 1
      broadcast = host + int(256 / divisor_total) - 1
      ultimo_ip = broadcast - 1

# Seleção das funcionalidades do programa.
ip = 0
mascara = 0
opcao = 0
while opcao != "5":
  opcao = input("\033[1;95mDigite o número com a respectiva função que deseja trabalhar:\033[0;0m"
    "\n1. Primeira função: Selecionar novo IP e máscara."
    "\n2. Segunda função: Mostrar tabela completa da máscara selecionada."
    "\n3. Terceira função: Mostrar a subrede específica do IP selecionado."
    "\n4. Quarta função: Mostrar informações de classe e tipo do IP selecionado."
    "\n5. Quinta função: Encerrar programa.\n")

  if opcao == "1":
    exc = 0
    while exc != 1:
      ip = input("Informe o IP (exemplo: 111.111.11.1): ")

      ip_dividido = ip.split(".") # Separa a string da resposta do usuário em octetos por meio dos pontos para verificar como inteiro.
      principal = ip_dividido[0] + "." +  ip_dividido[1] +  "." + ip_dividido[2] + "." # Mantém os 3 primeiros octetos por eles não se alterarem nesse sistema.
      last = int(ip_dividido[3]) # Separa o último octeto para ser trabalhado.

      if int(ip_dividido[0]) > 255 or int(ip_dividido[1]) > 255 or int(ip_dividido[2]) > 255 or last > 255:
        print("IP inválido.")
      else:
        exc = 1

    exc = 0
    while exc != 1:
      mascara = input(str("Coloque a máscara que deseja aplicar (de /24 até /30): "))

      mascara = mascara.replace("/", "") # Tira a barra da resposta do usuário para funcionar como inteiro.

      if int(mascara) < 24 or int(mascara) > 30:
        print("Máscara não suportada ou inexistente.")
      else:
        exc = 1

    print("Informações prontas para serem trabalhadas!")

  if opcao == "2":
    if ip == 0:
      print("Faça a primeira opção antes!")
    else:
      segunda_funcao()

  if opcao == "3":
    if ip == 0:
      print("Faça a primeira opção antes!")
    else:
      terceira_funcao()

  if opcao == "4":
    if ip == 0:
      print("Faça a primeira opção antes!")
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

      print("O IP selecionado tem classe", classe, "e tipo", tipo + ".")

  if opcao == "5":
    print("Programa encerrado.")
    break