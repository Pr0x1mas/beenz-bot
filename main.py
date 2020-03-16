#                     ===beenz-bot v2.0===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg1ODE2NTAyMDc4OTMxMTA3.Xm_eUQ.3g6CUj9T-kbaFI5AX5SPIROmuxw"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

