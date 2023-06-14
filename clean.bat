@echo off
cd "%ALGO_PATH%/algorithm_solutions"
del /s /q *.exe *.txt
for %%F in (*) do (
    if "%%~xF"=="" (
        del "%%F"
    )
)
echo "All .exe && extensionless files have been deleted."