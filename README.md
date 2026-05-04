<div align="center">

# 🎤 Mic Listener Troll — ILove.exe 😈

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Android-lightgrey)](https://github.com/BaHost01/OpenSource-Mic-Listener-Troll)
[![Build](https://img.shields.io/badge/build-automated-success?logo=github-actions)](https://github.com/BaHost01/OpenSource-Mic-Listener-Troll/actions)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Um script de monitoramento acústico furtivo projetado para pregar peças (trolls) em amigos que fazem sons contínuos no microfone.**

[Recursos](#-recursos) • [Instalação](#-instalação) • [Como Funciona](#-como-funciona) • [Aviso](#-aviso)

</div>

---

## 🌟 Recursos

- 🖥️ **Multiplataforma:** Suporte nativo para **Windows** e **Android (Termux)**.
- 🛠️ **Auto-Persistência:** Instala-se automaticamente na pasta de inicialização do Windows.
- 🛡️ **Privilégios Administrativos:** Solicita permissão UAC automaticamente para controle total do sistema.
- ⚡ **Otimização Extrema:** Consumo mínimo de CPU/RAM (Sample rate de 16kHz).
- ⚖️ **Sistema de Strikes:** Penalidades crescentes para o usuário "barulhento".
- 🎨 **Interface ANSI:** Design de terminal estilizado com cores e animações de hacking.

## ⚖️ Sistema de Penalidades (Strikes)

O script monitora o ambiente. Após **3 disparos** (strikes), ele executa ações defensivas:

1. **Strike 1 & 2:** Avisos visuais de intrusão no terminal.
2. **Strike 3:**
   - Tenta encerrar o **Roblox**.
   - Se não disponível, tenta encerrar o **FL Studio**.
   - Se nenhum estiver aberto, fecha a **janela ativa** atual.

## 🚀 Instalação

### Windows (Recomendado)
1. Vá até a aba [**Actions**](https://github.com/BaHost01/OpenSource-Mic-Listener-Troll/actions) do repositório.
2. Baixe o artefato mais recente do build **Ilove-Windows**.
3. Execute o `Ilove.exe` como Administrador.
> *O arquivo se copiará para a inicialização automaticamente.*

### Android (Termux)
```bash
# Instalar dependências do sistema
pkg install python-numpy portaudio fftw

# Instalar bibliotecas Python
pip install sounddevice numpy

# Configurar boot automático
bash setup.sh
```

## 🛠️ Detalhes Técnicos

- **Detecção:** Processamento de sinal em tempo real usando RMS (Root Mean Square).
- **Furtividade:** O executável é compilado com a flag `--noconsole` (roda em background).
- **Cooldown:** Sistema de espera de 60 segundos entre disparos para evitar spam.

## ⚠️ Aviso

Este projeto é **estritamente para fins educacionais e de entretenimento**. O autor não se responsabiliza por qualquer uso indevido, perda de dados ou danos causados por este script. Use com responsabilidade e apenas com o consentimento de seus amigos.

---

<div align="center">
  Criado com ❤️ por <a href="https://github.com/BaHost01">BaHost01</a>
</div>
