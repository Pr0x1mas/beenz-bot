#                    ===beenz-bot v2.4.2b===
#                   ===metalgearrape.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

print("Loading beenzbot...")

import beenz
from globals import *
# ---Setup connection to bot---
TOKEN = "***REMOVED***"

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

