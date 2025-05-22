# Auto-backup-with-navicat
# Navicat Auto-Backup HTTP Trigger

A lightweight HTTP server that triggers Windows scheduled tasks for Navicat database backups. The server:

- Listens on a configurable port for HTTP requests
- Authenticates requests using a Bearer token
- Triggers a Windows scheduled task using `schtasks`
- Monitors the task execution until completion
- Returns standardized JSON responses with execution status and timing information

Perfect for integrating database backups into automated workflows or triggering backups from remote systems via HTTP requests.

## Key Features:
- Token-based authentication
- Real-time task status monitoring
- JSON response format with timing metrics
- Supports both header and query parameter authentication
- Configurable polling interval

## 中文描述

# Navicat 自动备份 HTTP 触发器

一个轻量级 HTTP 服务器，用于触发 Windows 计划任务执行 Navicat 数据库备份。该服务器：

- 在可配置端口上监听 HTTP 请求
- 使用 Bearer 令牌进行请求认证
- 通过 `schtasks` 触发 Windows 计划任务
- 实时监控任务执行直至完成
- 返回标准化 JSON 响应，包含执行状态和时间信息

非常适合将数据库备份集成到自动化工作流中，或通过 HTTP 请求从远程系统触发备份。

## 主要特点：
- 基于令牌的身份验证
- 实时任务状态监控
- JSON 格式响应，包含计时指标
- 同时支持请求头和查询参数认证
- 可配置的轮询间隔 


# Run step
## 1、先在navicat上创建一个名为：oceanbase-auto-bak 的自动运行任务
![image](https://github.com/user-attachments/assets/f59295d5-0e6e-43b0-9553-2ffe0fe1a304)

## 2、在这个任务中添加你需要备份的库，然后点击开始测试备份是否正常，若正常就保存下来
![image](https://github.com/user-attachments/assets/2bfffe9b-e9ee-42bd-ab87-8c163dea3bde)

## 3、配置这个自动运行任务为定时执行，例如配置：每天凌晨1:00开始执行备份
![image](https://github.com/user-attachments/assets/c74cfcee-aa22-432c-8422-aacc270f31da)

## 4、使用Python3环境启动这个main.py的备份脚本,脚本默认会监听本机的8089端口
### 注意：Python脚本中navicat的自动备份任务名要配置必须一致，可以改成自己的，一致就行
`cd ./Auto-backup-with-navicat/  && ./main.py`

## 5、在命令行访问本机启动的8089端口，触发自动备份（注意token需要带上，可以在脚本中修改成自定义的token）
`curl.exe -N "http://127.0.0.1:8089/?token=ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU"`

执行结果如下图：
![img_v3_02m7_894f3462-a342-4fed-87cb-c78599c71fbg](https://github.com/user-attachments/assets/4242aba4-f545-4a01-82fd-081a66a01d58)
