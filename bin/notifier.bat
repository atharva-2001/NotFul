echo msgbox "The battery has reached the value you set. You can change that value in the log file." > %tmp%\tmp.vbs
cscript /nologo %tmp%\tmp.vbs
del %tmp%\tmp.vbs