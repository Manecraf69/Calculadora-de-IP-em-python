# Meu código é uma melhoria do código do meu amigo GuilhermeGamaliel

# Repositório do código dele: https://github.com/GuilhermeGamaliel/CalculadoraIP.git

# Código do qual minha calculadora nasceu:

# Entrada de dados por parte do usuário
ip = input(str("Coloque o IP: "))
mascara = input(str("Coloque a mascara que deseja aplicar no ip: "))
numero_func = input(str("Selecione a primeira ou a segunda função: "))

# Caso o usuário coloque um IP inválido

#O código comentado abaixo é outra forma de separar a parte principal de um IP
#ip_parte_principal = ip[:-int(ip[::-1].find("."))-1]
mascara = mascara.replace("/", "")
ip_dividido = ip.split(".")
principal = ip_dividido[0] + "." +  ip_dividido[1] +  "." + ip_dividido[2] + "."
last = int(ip_dividido[3])

# Declaração de variáveis 
host = 0
primeiro_ip = host + 1
divisor_total = 2 ** (int(mascara) - 24)
broadcast = int(256 / divisor_total) - 1
ultimo_ip = int(broadcast) - 1

# Primeira função que traz a tabela contendo todas as subredes
def primeira_func(ip, mascara, host, primeiro_ip, ultimo_ip, broadcast):
  print("")
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

# Segunda função que busca a subrede especifica onde o ip está
def segunda_func(ip, mascara, host, primeiro_ip, ultimo_ip, broadcast):
  print("")
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

# Funções para casos de exceção 
def func_inexistente(ip):
  print("")
  print("Essa função não existe, " +
  "para primeira função digite 1, " +
  "para segunda função digite 2")
  numero_func = input(str("Selecione a primeira ou a segunda função: "))

def mascara_inexistente(mascara):
  print("")
  print("Essa mascara não existe, tente uma mascara dentro de /25 a /32")
  mascara = input(str("Coloque a mascara que deseja aplicar no ip: "))

# Bloco de decisão que diferencia a primeira da segunda função

if int(mascara) < 25 or int(mascara) > 32:
  mascara_inexistente(mascara) 
elif numero_func == "1":
  primeira_func(ip, mascara, host, primeiro_ip, ultimo_ip, broadcast)
elif numero_func == "2" :
  segunda_func(ip, mascara, host, primeiro_ip, ultimo_ip, broadcast)
elif numero_func != "1" or numero_func != "2":
  while numero_func != "1" or numero_func != "2":
    func_inexistente(ip)