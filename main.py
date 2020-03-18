#                     ===beenz-bot v2.0===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg5NTczMzUwMDg3MDY1NjQ4.XnE7GQ.Oy_RUZXdYu_IuemhXJt-Zk0_IjE"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

