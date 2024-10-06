@echo off
set arg1=%1
(for /f usebackq^ eol^= %%a in ("output.txt") do break) && echo has data || goto vlc
:vlc
"vlc\dir\here" --started-from-file --playlist-enqueue --play-and-exit %arg1%