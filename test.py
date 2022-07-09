import random
class PrintRPS():
  def printRPS(i):
    if i == 0:
      return "グー"
    elif i == 1:
      return "チョキ"
    elif i == 2:
      return "パー"
  
class PrintText():
  def win(playerRPS,cpuRPS):
    print(PrintRPS.printRPS(playerRPS),"vs",PrintRPS.printRPS(cpuRPS))
    print("PLAYER WIN\n")
    print("YOU WIN\n")
  def lose(playerRPS,cpuRPS):
    print(PrintRPS.printRPS(playerRPS),"vs",PrintRPS.printRPS(cpuRPS))
    print("CPU WIN\n")
    print("YOU LOSE\n")
  def aiko(playerRPS,cpuRPS):
    print(PrintRPS.printRPS(playerRPS),"vs",PrintRPS.printRPS(cpuRPS))
    print("aiko mouitido\n")
while True:
  RPS_list = (0,1,2)
  cpuRPS = random.choice(RPS_list)
  print('グー:0\チョキ:1\パー:2\n')
  playerRPS = int(input())
  if cpuRPS == 0:
    if playerRPS == 0:
      PrintText.aiko(playerRPS,cpuRPS)
    elif playerRPS == 1:
      PrintText.lose(playerRPS,cpuRPS)
      break
    elif playerRPS == 2:
      PrintText.win(playerRPS,cpuRPS)
      break
  elif cpuRPS == 1:
    if playerRPS == 0:
      PrintText.win(playerRPS,cpuRPS)
      break
    elif playerRPS == 1:
      PrintText.aiko(playerRPS,cpuRPS)
    elif playerRPS == 2:
      PrintText.lose(playerRPS,cpuRPS)
      break
  else:
    if playerRPS == 0:
      PrintText.lose(playerRPS,cpuRPS)
      break
    elif playerRPS == 1:
      PrintText.win(playerRPS,cpuRPS)
      break
    elif playerRPS == 2:
      PrintText.aiko(playerRPS,cpuRPS)
    else:
      print("error")