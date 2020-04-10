#                     ===beenz-bot v2.4.2b===
#                       ===freeze.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

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
bdist_msi_options = {"initial_target_dir": "C:\Program Files\metalgearrape",
                     "all_users": True}
print(packages)

setup(  name = "metalgearrape",
        version = sysversion,
        description = "Server software for metalgearrape discord bot",
        options = {"build_exe": build_exe_options,
                   "bdist_msi": bdist_msi_options},
        executables = [Executable("metalgearrape.py",
                                  shortcutName="metalgearrape",
                                  shortcutDir="StartMenuFolder")])