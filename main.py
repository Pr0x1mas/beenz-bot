#         ===beenz-bot v1.3.2===
#      ===Copyright 2020 Pr0x1mas===
#            ===main.py===
#  ===Branched by TheProgramableTurtle===
print("Loading beenzbot...")

import beenz
from globals import *
from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njg1ODE2NTAyMDc4OTMxMTA3.XmOKpQ.Rsve4K8WOFRuuW5KuRBecgrVrh0"

client = beenz.Bot(sysversion)



client.registerCommands()

client.run(TOKEN)

