#                     ===beenz-bot v2.5b===
#                       ===freeze.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

from cx_Freeze import setup, Executable

packages = ["os", "time", "random", "inspect", "asyncio", "io", "pathlib"]
with open("requirements", "r") as requirements:
    for line in requirements:
        packages.append(line.rstrip())
    requirements.close()

build_exe_options = {"packages": packages}
bdist_msi_options = {"initial_target_dir": "C:\Program Files\metalgearrape",
                     "all_users": True}
print(packages)

setup(  name = "metalgearrape",
        version = "2.5b",
        description = "Server software for metalgearrape discord bot",
        options = {"build_exe": build_exe_options,
                   "bdist_msi": bdist_msi_options},
        executables = [Executable("metalgearrape.py",
                                  shortcutName="metalgearrape",
                                  shortcutDir="StartMenuFolder")])