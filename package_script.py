import os
import subprocess

def install_pyinstaller():
    print("正在安裝 PyInstaller...")
    subprocess.run(["pip", "install", "pyinstaller"], check=True)

def package_script(script_name, exe_name):
    print(f"正在打包 {script_name} 為 exe 文件...")
    subprocess.run(["pyinstaller", "--onefile", f"--name={exe_name}", script_name], check=True)

def main():
    script_name = "clear.py"  # 這裡填寫您的腳本名稱
    exe_name = "楓之谷route清除"  # 自定義的exe名稱

    if not os.path.exists(script_name):
        print(f"錯誤：找不到腳本 {script_name}")
        return

    try:
        install_pyinstaller()
        package_script(script_name, exe_name)
        print(f"打包完成！exe 文件 '{exe_name}.exe' 應該在 'dist' 文件夾中。")
    except subprocess.CalledProcessError as e:
        print(f"打包過程中出錯：{e}")

if __name__ == "__main__":
    main()