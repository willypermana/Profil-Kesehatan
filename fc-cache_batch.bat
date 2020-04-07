@ECHO OFF 
TITLE Rebuild LaTeX font-cache
cd C:\texlive\2016\bin
fc-cache.exe -f
PAUSE
