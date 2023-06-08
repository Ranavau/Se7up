##__IMPORT__##

import os , time 
from time import sleep
os.system("pkg install git")
#os.system(''pkg install python'')
###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

logo =('''''
\x1b[38;5;46m███████ ███████ ████████ ██    ██ ██████  
\x1b[38;5;196m██      ██         ██    ██    ██ ██   ██ 
\033[1;97m███████ █████      ██    ██    ██ ██████  
\x1b[38;5;196m     ██ ██         ██    ██    ██ ██      
\x1b[38;5;46m███████ ███████    ██     ██████  ██  

\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
╠══[Author                   • \33[1;38mMR-Rana ]\33[1;38m      ║\033[1;31m 
╠══[Facebook                 • Rana Ahmed ]   ║  \033[1;97m  
╠══[Github                   • \33[1;38mRanaVau ]      ║\33[1;34m   
╠══[Whatsapp                 • 018500**** ]   ║\33[1;35m 
╠══[TOOLS                    • Free ]         ║ \33[1;32m   
╠══[VERSION                  • 0.1 ]          ║\033[1;35m 
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m
''''')

os.system('espeak -a 300 " Your,   Real,  Name,"')
uname =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  Rana,  Setup,  Tools"')
pass


menu =(f'''{kk}
[1] Basic Setup
[2] Advance Setup 
[3] Contact Me
[4] Exit
''')

def setup ():
	os.system('''pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4''')
	
def advance ():
	os.system('''pkg update -y && pkg upgrade -y && pip install requests mechanize futures rich bs4 lolcat''')

def main ():
	os.system('clear')
	print (logo)
	print ('')
	print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
	print (menu)
	option = input (f'{ORANGE} Choose Option :')
	if option =='1':
		setup()
		main()
	elif option=='2':
		advance()
		main()
	elif option=='3':
		os.system("xdg-open https://wa.me/+8801745338756")
		main()
	elif option=='4':
		exit()
	else:
		print('/n')
		print(f'Choose Carefully')
		time.sleep(3)
		main()
		
main()
	

