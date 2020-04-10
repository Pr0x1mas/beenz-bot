@echo off
IF EXIST ./dist (ECHO dist directory already exists, previous builds may be overwritten.)
IF EXIST ./build (ECHO build directory already exists, it will be deleted.)
PAUSE
ECHO Deleting previous python object files, pre-compiled python scripts, libraries, dlls, and python library files
DEL "./build"
ECHO Starting Compile
python freeze.py build bdist_msi
IF EXIST ./dist (ECHO see dist folder for installer)
PAUSE