#                     ===beenz-bot v2.0===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg1ODE2NTAyMDc4OTMxMTA3.XmaGHg.6e6YHz6MwE2lcn7rJH74IYaGhSI"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

