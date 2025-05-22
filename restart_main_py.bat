@echo off
:: 关闭已有的 main.py（根据窗口标题名或端口查找）
for /f "tokens=2 delims=," %%i in ('netstat -ano ^| find ":8089" ^| find "LISTENING"') do (
    for /f "tokens=1" %%j in ('tasklist /FI "PID eq %%i" /NH') do (
        echo 终止进程 PID %%i (%%j)
        taskkill /F /PID %%i
    )
)

:: 启动新的 main.py（确保路径正确）
cd /d D:\develop-file\1-cursor\03-py-project\frp_0.62.1_windows_amd64
start "" python D:\your\path\to\main.py