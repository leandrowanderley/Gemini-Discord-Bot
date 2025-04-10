def log(msg: str, tipo: str = "info"):
    cores = {
        "info": "\033[94m",     # azul
        "sucesso": "\033[92m",  # verde
        "erro": "\033[91m",     # vermelho
        "aviso": "\033[93m",    # amarelo
        "reset": "\033[0m"      # resetar cor
    }

    emojis = {
        "info": "ℹ️",
        "sucesso": "✅",
        "erro": "❌",
        "aviso": "⚠️"
    }

    cor = cores.get(tipo, cores["info"])
    emoji = emojis.get(tipo, "")
    print(f"{cor}[{tipo.upper()}] {emoji} {msg}{cores['reset']}")
