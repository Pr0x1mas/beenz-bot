#                    ===beenz-bot v2.4.2===
#                   ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

print("Loading beenzbot...")

import beenz
import os
from globals import *
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.join(os.path.dirname(__file__), '.env'))
# ---Setup connection to bot---
TOKEN = os.getenv("TOKEN")

client = beenz.Bot(sysversion)

client.registerCommands()

client.run(TOKEN)

