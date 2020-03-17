#                     ===beenz-bot v2.0===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg5NTczMzUwMDg3MDY1NjQ4.XnE1Tg.ccZd2-hIBZOnnOk1xSq87A6IwOE"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

