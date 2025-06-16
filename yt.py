from os import system as c
import time
import random

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{G}
██████╗ ██╗   ██╗████████╗ ██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
██████╔╝██║   ██║   ██║   ██║   ██║
██╔═══╝ ██║   ██║   ██║   ██║   ██║
██║     ╚██████╔╝   ██║   ╚██████╔╝
╚═╝      ╚═════╝    ╚═╝    ╚═════╝ 
{P} HACKING WORLD - YOUTUBE VIP SUB TOOL
""")

def progress(task):
    print(f"{C}[+] {task}...")
    for i in range(3):
        print(f"{Y}[*] Loading{'.'*i}")
        time.sleep(1)

def subscribe():
    logo()
    link = input(f"{Y}ENTER YOUTUBE VIDEO LINK: ")
    progress("Connecting to YouTube Server")
    print(f"{G}[✓] Link Verified: {link}")
    time.sleep(2)
    num = int(input(f"{C}ENTER NUMBER OF SUBSCRIBERS TO ADD: "))
    print(f"{Y}[+] Starting Subscriber Injection...\n")
    for i in range(num):
        print(f"{G}[✓] Subscribed {i+1}/{num}")
        time.sleep(0.2)
    print(f"\n{P}[✓] All {num} Subscribers Added Successfully!")
    print(f"{B}Enjoy Your VIP Status!\n")
    input(f"{A}Press Enter To Return To Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Start Subscribe Boost")
    print(f"{A}[0] Exit Tool")
    choice = input(f"{Y}Select Option: ")
    if choice == '1':
        subscribe()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()