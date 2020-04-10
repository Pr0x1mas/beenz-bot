#                     ===beenz-bot v2.4.2===
#                       ===freeze.py===
#  ======Copyright 2020 TheProgramableTurtle======

from cx_Freeze import setup, Executable
from globals import *

packages = ["os", "time", "random", "inspect", "asyncio", "io", "pathlib"]
with open("requirements", "r") as requirements:
    for line in requirements:
        packages.append(line.rstrip())
    requirements.close()
excludes = ["tkinter", "tk", "tcl", "xml", "xmlrpc", "yarl", "email"]
build_exe_options = {"packages": packages,
                     "excludes": excludes}
bdist_msi_options = {"initial_target_dir": "C:\Program Files\beenz-bot",
                     "all_users": True}
print(packages)

setup(  name = "beenz-bot",
        version = sysversion,
        description = "Server software for beenz-bot discord bot",
        options = {"build_exe": build_exe_options,
                   "bdist_msi": bdist_msi_options},
        executables = [Executable("main.py",
                                  shortcutName="beenz-bot",
                                  shortcutDir="StartMenuFolder")])
