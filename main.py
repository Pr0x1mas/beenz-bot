#                     ===beenz-bot v2.0===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg0NDgxODk2ODIyMjEwNTYw.Xm_o9Q.7yQWe8Ri7G47k94oU0Hdy2oR8NI"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

