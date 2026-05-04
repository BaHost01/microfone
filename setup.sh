#!/bin/bash

# Setup script for Mic Listener Troll

PROJECT_DIR=$(pwd)
BOOT_DIR="$HOME/.termux/boot"
BOOT_SCRIPT="$BOOT_DIR/start_troll_mic.sh"

echo "[*] Iniciando setup..."

# Create boot directory if it doesn't exist
mkdir -p "$BOOT_DIR"

# Create the boot script
cat <<EOF > "$BOOT_SCRIPT"
#!/bin/bash
# Keep the CPU awake
termux-wake-lock
# Start the mic listener in the background
python "$PROJECT_DIR/troll_mic.py" &
EOF

chmod +x "$BOOT_SCRIPT"

echo "[+] Script de boot criado em: $BOOT_SCRIPT"
echo "[!] Certifique-se de ter o app 'Termux:Boot' instalado (F-Droid)."
echo "[!] Abra o app 'Termux:Boot' uma vez após instalar para ativar."
echo ""
echo "[*] Para testar agora, execute: python troll_mic.py"
