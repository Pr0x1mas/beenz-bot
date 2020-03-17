#                     ===beenz-bot v2.0===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg0NDgxODk2ODIyMjEwNTYw.XnEXRQ.DItMiP_O7UAglsnoK_JJjB_O5Y8"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

