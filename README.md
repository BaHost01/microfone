# Mic Listener Troll 🎤😈

Um script Python multiplataforma (Windows/Android Termux) que monitora o microfone e exibe mensagens falsas de "hacking" quando detecta sons contínuos (como gemidos).

## ✨ Funcionalidades
- **Multiplataforma:** Suporte para Windows e Android (Termux).
- **Auto-Boot:** Scripts inclusos para iniciar com o sistema.
- **Admin Required:** No Windows, solicita privilégios de administrador automaticamente.
- **Background Mode:** Otimizado para rodar em segundo plano com baixo consumo de RAM/CPU.
- **Mensagens Aleatórias:** Sequências de mensagens realistas de invasão.
- **GitHub Actions:** Build automático de `.exe` para Windows.

## 🚀 Instalação e Uso

### Windows
1. Baixe o `MicTroll.exe` da aba **Actions** do GitHub.
2. Execute como Administrador.
3. Para iniciar no boot, coloque um atalho do `.exe` na pasta:
   `%AppData%\Microsoft\Windows\Start Menu\Programs\Startup`

### Android (Termux)
1. Instale as dependências:
   ```bash
   pkg install python-numpy portaudio fftw
   pip install sounddevice numpy
   ```
2. Execute o setup:
   ```bash
   bash setup.sh
   ```

## 🛠️ Otimizações
- **Sample Rate:** Reduzido para 16kHz para economizar processamento.
- **Sleep:** Loop principal com sleep de 1s para minimizar uso de CPU.
- **Dtype:** Uso de `float32` para processamento eficiente com NumPy.

## ⚠️ Aviso
Este script é apenas para fins educacionais e de brincadeira (troll). Use com responsabilidade.
