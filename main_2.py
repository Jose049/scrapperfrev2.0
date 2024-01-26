from telethon import TelegramClient, events
import telebot
import re
import datetime
import random
import requests
from time import sleep
from os import system, name, execv
from sys import executable, argv
from bin import get_bin_info
from apis import apid, apihasd, token

now = datetime.datetime.now()
mes_actual = now.month
ano_actual = now.year

client = TelegramClient('anon', apid, apihasd)
client.parse_mode = 'html'
bot = telebot.TeleBot(token, parse_mode="html")
id_channel = -1002062068679

def vef_ccn(ccn):
    with open('ccs.txt', 'r') as f:
        r = f.read()
    if ccn in r:
        return True
    else:
        return False


@client.on(events.NewMessage)
async def my_event(event: events):
    try:
        text = event.raw_text
    except MemoryError:
        return ...

    if "|":
        x = re.findall(r'\d+', text)
        if len(x) < 4:
            return

        cc = x[0]
        mm = x[1]
        yy = x[2]
        cvv = x[3]

        if len(cc) > 16 or len(mm) > 2 or len(yy) > 4 or len(cvv) > 4:
            return

        if mm.startswith('2'):
            mm, yy = yy, mm

        if int(mm) < mes_actual or (len(mm) >= 3 and int(yy) < ano_actual):
            return

        cxc = f"{cc}"
        v = vef_ccn(cxc)
        if v:
            return

    

        with open('ccs.txt', 'a') as d:
            d.write(f'{cc}|{mm}|{yy}|{cvv}\n')

   
        for _ in range(4):
            random_digits = "".join(random.choice("0123456789") for _ in range(6))
            random_month = random.randint(1, 12)
            random_year = random.randint(2024, 2030)
        

        
        
        req = requests.get(f"https://bins.antipublic.cc/bins/{cxc[:6]}").json()      
        brand = req['brand'].lower()
        country = req['country_name'].lower()
        emoji = req['country_flag'].lower()
        bank = req['bank'].lower()
        level = req['level'].lower()
        type_ = req['type'].lower()
        flag = req["country_flag"].lower()
        
        text = f"""

<b><i>𝘒𝙈6𝙅 𝙎𝘾𝙍𝘼𝙋𝙋𝙀𝙍 [𝙁𝙍𝙀𝙀] </i></b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝘛𝘈𝘙𝘑𝘌𝘛𝘈 ⇰ ✽ <code>{cc}|{mm}|{yy}|{cvv}</code>
𝘙𝘌𝘚𝘗𝘜𝘌𝘚𝘛𝘈 ⇰ ✽ <b>Approved! ✅</b>
𝘌𝘟𝘛𝘙𝘈 1 ⇰ ✽ ✽ <code>{cxc[:6]}{random_digits}xxxx|{random_month:02d}|{random_year}|rnd</code>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝘉𝘐𝘕 ⇰ ✽ {emoji}{brand} {level} {type_}{emoji}
𝘉𝘈𝘕𝘊𝘖 ⇰ ✽ {emoji}{bank}{emoji}
𝘗𝘈𝘐𝘚 ⇰ ✽ {emoji}{country} {flag}{emoji}
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
Owner ⇰ ♛ @GatoOnichan2
"""

        sleep(40)
        try:
            bot.send_message(id_channel, text)
        except:
            bot.send_message(id_channel, text)

    else:
        pass


system('cls' if name == 'nt' else 'clear')
print('Inicio!')
try:
    client.start()
except Exception as e:
    print(e)
client.run_until_disconnected()
