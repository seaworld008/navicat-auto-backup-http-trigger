# Navicat Auto-Backup HTTP Trigger User Manual / 使用手册

## English Version

### Overview
The Navicat Auto-Backup HTTP Trigger is a lightweight HTTP server that enables remote triggering of Windows scheduled tasks for Navicat database backups. This tool bridges the gap between automated workflows and Navicat's backup functionality by providing a REST API interface.

### Features
- **HTTP API Interface**: Trigger backups via HTTP requests
- **Token-based Authentication**: Secure access with Bearer token authentication
- **Real-time Monitoring**: Live tracking of backup task execution status
- **JSON Response Format**: Standardized responses with timing metrics
- **Flexible Authentication**: Supports both header and query parameter authentication
- **Configurable Settings**: Customizable port, token, and polling intervals

### Requirements
- Windows operating system
- Python 3.x
- Navicat (with backup tasks configured)
- Administrative privileges (for scheduled task management)

### Installation & Setup

#### Step 1: Create Navicat Backup Task
1. Open Navicat and create a new automated backup task
2. Name the task: `oceanbase-auto-bak` (or customize in script)
3. Add the databases you want to backup
4. Test the backup task to ensure it works correctly
5. Save the task configuration

#### Step 2: Configure Windows Scheduled Task
1. Set up the Navicat backup task as a Windows scheduled task
2. Configure timing (e.g., daily at 1:00 AM)
3. Ensure the task name matches the script configuration: `\oceanbase-auto-bak`

#### Step 3: Configure the Python Script
1. Download the `main.py` script
2. Edit the configuration section:
   ```python
   PORT = 8089                    # HTTP server port
   TOKEN = "your-secure-token"    # Authentication token
   TASK_NAME = r"\oceanbase-auto-bak"  # Windows task name
   POLL_INTERVAL = 2              # Status polling interval (seconds)
   ```

#### Step 4: Start the HTTP Server
```bash
cd /path/to/script/
python main.py
```
The server will start listening on the configured port (default: 8089).

### Usage

#### API Endpoint
- **URL**: `http://localhost:8089/`
- **Method**: GET
- **Authentication**: Bearer token or query parameter

#### Authentication Methods

**1. Header Authentication:**
```bash
curl -H "Authorization: Bearer ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU" http://localhost:8089/
```

**2. Query Parameter Authentication:**
```bash
curl "http://localhost:8089/?token=ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU"
```

#### Response Format
```json
{
  "start_time": "2024-01-01 10:00:00",
  "end_time": "2024-01-01 10:05:30",
  "code": 0,
  "data": true,
  "msg": "成功"
}
```

**Response Fields:**
- `start_time`: Task execution start time
- `end_time`: Task execution end time
- `code`: Status code (0 = success, 1 = error, 401 = unauthorized)
- `data`: Boolean indicating success/failure
- `msg`: Status message
- `error`: Error details (if applicable)

### Troubleshooting

#### Common Issues
1. **401 Unauthorized**: Check token configuration
2. **Task not found**: Verify Windows scheduled task name
3. **Permission denied**: Run with administrator privileges
4. **Port in use**: Change the PORT configuration

#### Logs
The server runs silently by default. Check Windows Task Scheduler for task execution logs.

---

## 中文版本

### 概述
Navicat 自动备份 HTTP 触发器是一个轻量级 HTTP 服务器，可以远程触发 Windows 计划任务执行 Navicat 数据库备份。该工具通过提供 REST API 接口，在自动化工作流和 Navicat 备份功能之间架起桥梁。

### 功能特点
- **HTTP API 接口**：通过 HTTP 请求触发备份
- **基于令牌的身份验证**：使用 Bearer 令牌确保安全访问
- **实时监控**：实时跟踪备份任务执行状态
- **JSON 响应格式**：标准化响应，包含计时指标
- **灵活的身份验证**：同时支持请求头和查询参数认证
- **可配置设置**：可自定义端口、令牌和轮询间隔

### 系统要求
- Windows 操作系统
- Python 3.x
- Navicat（已配置备份任务）
- 管理员权限（用于计划任务管理）

### 安装与设置

#### 步骤 1：创建 Navicat 备份任务
1. 打开 Navicat 并创建新的自动备份任务
2. 任务命名为：`oceanbase-auto-bak`（或在脚本中自定义）
3. 添加需要备份的数据库
4. 测试备份任务确保正常工作
5. 保存任务配置

#### 步骤 2：配置 Windows 计划任务
1. 将 Navicat 备份任务设置为 Windows 计划任务
2. 配置执行时间（例如：每天凌晨 1:00）
3. 确保任务名称与脚本配置一致：`\oceanbase-auto-bak`

#### 步骤 3：配置 Python 脚本
1. 下载 `main.py` 脚本
2. 编辑配置部分：
   ```python
   PORT = 8089                    # HTTP 服务器端口
   TOKEN = "your-secure-token"    # 认证令牌
   TASK_NAME = r"\oceanbase-auto-bak"  # Windows 任务名称
   POLL_INTERVAL = 2              # 状态轮询间隔（秒）
   ```

#### 步骤 4：启动 HTTP 服务器
```bash
cd /path/to/script/
python main.py
```
服务器将在配置的端口上开始监听（默认：8089）。

### 使用方法

#### API 端点
- **URL**: `http://localhost:8089/`
- **方法**: GET
- **认证**: Bearer 令牌或查询参数

#### 认证方式

**1. 请求头认证：**
```bash
curl -H "Authorization: Bearer ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU" http://localhost:8089/
```

**2. 查询参数认证：**
```bash
curl "http://localhost:8089/?token=ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU"
```

#### 响应格式
```json
{
  "start_time": "2024-01-01 10:00:00",
  "end_time": "2024-01-01 10:05:30",
  "code": 0,
  "data": true,
  "msg": "成功"
}
```

**响应字段说明：**
- `start_time`: 任务执行开始时间
- `end_time`: 任务执行结束时间
- `code`: 状态码（0 = 成功，1 = 错误，401 = 未授权）
- `data`: 布尔值表示成功/失败
- `msg`: 状态消息
- `error`: 错误详情（如果适用）

### 故障排除

#### 常见问题
1. **401 未授权**：检查令牌配置
2. **任务未找到**：验证 Windows 计划任务名称
3. **权限被拒绝**：使用管理员权限运行
4. **端口被占用**：更改 PORT 配置

#### 日志
服务器默认静默运行。可查看 Windows 任务计划程序获取任务执行日志。

# Run step
## 1、先在navicat上创建一个名为：oceanbase-auto-bak 的自动运行任务
![image](https://github.com/user-attachments/assets/f59295d5-0e6e-43b0-9553-2ffe0fe1a304)

## 2、在这个任务中添加你需要备份的库，然后点击开始测试备份是否正常，若正常就保存下来
![image](https://github.com/user-attachments/assets/2bfffe9b-e9ee-42bd-ab87-8c163dea3bde)

## 3、配置这个自动运行任务为定时执行，例如配置：每天凌晨1:00开始执行备份
![image](https://github.com/user-attachments/assets/c74cfcee-aa22-432c-8422-aacc270f31da)

## 4、使用Python3环境启动这个main.py的备份脚本,脚本默认会监听本机的8089端口
### 注意：Python脚本中navicat的自动备份任务名要配置必须一致，可以改成自己的，一致就行
```bash
cd /path/to/script/
python main.py
```

## 5、在命令行访问本机启动的8089端口，触发自动备份（注意token需要带上，可以在脚本中修改成自定义的token）
```bash
curl.exe -N "http://127.0.0.1:8089/?token=ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU"
```

执行结果如下图：
![img_v3_02m7_894f3462-a342-4fed-87cb-c78599c71fbg](https://github.com/user-attachments/assets/4242aba4-f545-4a01-82fd-081a66a01d58)
