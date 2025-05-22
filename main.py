#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import subprocess
import time
import re
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs

# ———— 配置区 ————
PORT          = 8089
TOKEN         = "ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU"
# 一定要和“任务计划程序”里的“任务名”完全一致，包括前导反斜杠
TASK_NAME     = r"\oceanbase-auto-bak"
POLL_INTERVAL = 2    # 秒，轮询间隔
# ————————————

# 匹配“状态:”、“Status:” 或 “模式:”，支持中英文、全/半角冒号
status_re = re.compile(r'^(状态|Status|模式)[:：]\s*(.+)$', re.IGNORECASE)

class BackupHandler(http.server.BaseHTTPRequestHandler):
    def _write_json(self, code, data, msg, start_time=None, end_time=None, error=None):
        payload = {
            "start_time": start_time,
            "end_time": end_time,
            "code": code,
            "data": data,
            "msg": msg
        }
        # 如果有 error 字段，也一并输出
        if error is not None:
            payload["error"] = error
        self.send_response(200 if code == 0 else 500)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode('utf-8'))

    def do_GET(self):
        # 1. 校验 token
        qs   = parse_qs(urlparse(self.path).query)
        auth = self.headers.get('Authorization', '')
        if not ((auth.startswith("Bearer ") and auth.split()[1] == TOKEN)
                or qs.get("token", [None])[0] == TOKEN):
            self._write_json(
                code=401,
                data=False,
                msg="Unauthorized",
                start_time=None,
                end_time=None
            )
            return

        # 2. 记录开始时间
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 3. 触发任务
        try:
            subprocess.run(
                ["schtasks", "/Run", "/TN", TASK_NAME],
                check=True, capture_output=True, text=True
            )
        except subprocess.CalledProcessError as e:
            self._write_json(
                code=1,
                data=False,
                msg="触发失败",
                start_time=start_time,
                end_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                error=e.stderr.strip()
            )
            return

        # 4. 轮询状态直到非运行态
        final_status = None
        while True:
            proc = subprocess.run(
                ["schtasks", "/Query", "/TN", TASK_NAME, "/V", "/FO", "LIST"],
                capture_output=True, text=True
            )
            if proc.stderr.strip():
                final_status = f"Query Error: {proc.stderr.strip()}"
                break

            status = None
            for line in proc.stdout.splitlines():
                m = status_re.match(line.strip())
                if m:
                    status = m.group(2)
                    break

            if not status:
                final_status = "UNKNOWN"
                break

            if any(kw in status for kw in ("running", "运行中", "正在运行")):
                time.sleep(POLL_INTERVAL)
                continue

            final_status = status
            break

        # 5. 记录结束时间
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 6. 输出标准化 JSON
        if final_status == "就绪":
            # 就绪改成“备份完成”
            self._write_json(
                code=0,
                data=True,
                msg="成功",
                start_time=start_time,
                end_time=end_time
            )
        else:
            # 非“就绪”也当作成功返回，只是 msg 带上实际状态
            self._write_json(
                code=0,
                data=True,
                msg=final_status,
                start_time=start_time,
                end_time=end_time
            )

    def log_message(self, format, *args):
        pass  # 静默日志

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

if __name__ == "__main__":
    print(f"Starting server on port {PORT}, task='{TASK_NAME}'")
    with ThreadedHTTPServer(("", PORT), BackupHandler) as httpd:
        httpd.serve_forever()
