import os
os.system("title ᴇʏᴇ ᴏꜰ ɢᴏᴅ")
os.system("cls")
import discord
from datetime import datetime
from pystyle import *

RED = '\033[1;91m'
WHITE = '\033[0m'
GREEN = '\033[1;32m'
GRAY = '\033[1;90m'
GOLD = '\033[0;33m'
BLUE = '\033[1;34m'


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

log_filename = f"{datetime.now().strftime('%Y-%m-%d')}_chat.log"

def log_message(content):
    stripped_content = content.replace(RED, "").replace(WHITE, "").replace(GREEN, "").replace(GRAY, "").replace(GOLD, "")
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(stripped_content + "\n")


art = f"""
                    ▓█████▓██   ██▓▓█████     ▒█████    █████▒     ▄████  ▒█████  ▓█████▄ 
                    ▓█   ▀ ▒██  ██▒▓█   ▀    ▒██▒  ██▒▓██   ▒     ██▒ ▀█▒▒██▒  ██▒▒██▀ ██▌
                    ▒███    ▒██ ██░▒███      ▒██░  ██▒▒████ ░    ▒██░▄▄▄░▒██░  ██▒░██   █▌
                    ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄    ▒██   ██░░▓█▒  ░    ░▓█  ██▓▒██   ██░░▓█▄   ▌
                    ░▒████▒ ░ ██▒▓░░▒████▒   ░ ████▓▒░░▒█░       ░▒▓███▀▒░ ████▓▒░░▒████▓ 
                    ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░   ░ ▒░▒░▒░  ▒ ░        ░▒   ▒ ░ ▒░▒░▒░  ▒▒▓  ▒ 
                     ░ ░  ░▓██ ░▒░  ░ ░  ░     ░ ▒ ▒░  ░           ░   ░   ░ ▒ ▒░  ░ ▒  ▒ 
                       ░   ▒ ▒ ░░     ░      ░ ░ ░ ▒   ░ ░       ░ ░   ░ ░ ░ ░ ▒   ░ ░  ░ 
                       ░  ░░ ░        ░  ░       ░ ░                   ░     ░ ░     ░    
                           ░ ░                                                     ░            
"""
Dev = f"""
                                                     {BLUE}╭────────────────────────╮
                                                     │ {WHITE}Dev by: {RED}ByteWardenDev{BLUE}  │
                                                     ╰────────────────────────╯{WHITE}    
"""
print(Colorate.Vertical(Colors.black_to_white, Center.XCenter(art)))
print(Dev)
TOKEN = input(f" {GRAY}[ {RED}#{GRAY} ]{WHITE} Enter token >")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    timestamp = datetime.now().strftime('%H:%M:%S')
    log_entry = (f"{GRAY}[{GOLD}{timestamp}{GRAY}]{WHITE} — [{message.channel}] "
                 f"{message.author}: {message.content}")

    print(log_entry)
    log_message(log_entry)

client.run(TOKEN)
