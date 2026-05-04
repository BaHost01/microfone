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
COOLDOWN = 60         # Segundos para esperar antes de permitir outro disparo
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

if __name__ == "__main__":
    if platform.system() == "Windows" and not is_admin():
        print("[!] Solicitando permissões de administrador...")
        run_as_admin()

    # Otimização: Uso de stream de baixo recurso
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
