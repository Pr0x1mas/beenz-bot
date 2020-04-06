#                     ===beenz-bot v2.4===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "***REMOVED***"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

