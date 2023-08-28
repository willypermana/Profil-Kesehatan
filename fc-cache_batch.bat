@ECHO OFF 
TITLE Rebuild LaTeX font-cache
cd C:\texlive\2021\bin
fc-cache.exe -f
PAUSE
