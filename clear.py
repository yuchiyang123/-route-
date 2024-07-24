import subprocess
import re
import tkinter as tk
from tkinter import messagebox

def run_cmd(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        show_alert(f"命令執行失敗:{command}\n{e.output}")
        return None

def show_alert(message):
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口
    messagebox.showinfo("提示", message)
    root.destroy()

def find_and_delete_202_ip_routes():
    output = run_cmd("route print")

    if output:
        pattern = r'\b202\.(\d{1,3}\.){2}\d{1,3}\s+(\d{1,3}\.){3}\d{1,3}'
        matches = re.findall(pattern, output)

        if matches:
            show_alert("找到202開頭的IP")
            for match in matches:
                ip = match[0]
                mask = match[1]
                full_ip = f"202.{ip}"
                show_alert(f"IP: {full_ip}, 掩碼: {mask}")

                delete_command = f"route delete {full_ip}"
                show_alert(f"執行刪除命令: {delete_command}")
                result = run_cmd(delete_command)
                if result is not None:
                    show_alert("路由成功刪除")
                else:
                    show_alert("路由刪除失敗")
        else:
            show_alert("未找到202開頭的IP")
    else:
        show_alert("無法獲取路由訊息")

if __name__ == "__main__":
    find_and_delete_202_ip_routes()