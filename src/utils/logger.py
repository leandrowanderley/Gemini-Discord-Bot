# === Como Usar ===

# from src.utils.logger import log

# log("Mensagem enviada com sucesso", "sucesso")
# log("Erro ao carregar arquivo", "erro")
# log("Comando /chat executado", "info")
# log("Histórico de mensagens limpo", "aviso")
# log("Valor da variável x: 42", "debug")


import datetime

# === Códigos ANSI para cores ===
RESET = "\033[0m"
BOLD = "\033[1m"

COLORS = {
    "info": "\033[94m",     # Azul
    "sucesso": "\033[92m",  # Verde
    "erro": "\033[91m",     # Vermelho
    "aviso": "\033[93m",    # Amarelo
    "debug": "\033[95m",    # Roxo
}

# === Emojis para os tipos de log ===
EMOJIS = {
    "info": "ℹ️",
    "sucesso": "✅",
    "erro": "❌",
    "aviso": "⚠️",
    "debug": "🛠️",
}

# === Função de log unificada ===
def log(msg: str, tipo: str = "info", nome: str = "LOG"):
    cor = COLORS.get(tipo, "\033[97m")  # Branco padrão
    emoji = EMOJIS.get(tipo, "📝")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{cor}{BOLD}[{timestamp}] [{emoji} {nome.upper()}] {msg}{RESET}")
