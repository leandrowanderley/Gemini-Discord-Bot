# FalAI - Assistente Inteligente para Discord com Gemini

<div align="center">
  <img src="banner.png" alt="Banner do FalAI" width="680">
  
  *Conectando comunidades através de conversas inteligentes*
  
  <img src="icon.png" alt="Ícone do FalAI" width="200">
</div>

## 🚀 Funcionalidades Principais

- **🤖 Interação Conversacional**: Utiliza a API Gemini para gerar respostas contextualizadas baseadas no histórico de mensagens
- **📚 Histórico de Mensagens**: Mantém registro das últimas 10 interações para conversas mais naturais
- **⚙️ Fácil Configuração**: Personalização completa via arquivos `config.json`, `prompts.json` e `mensagens.json`
- **🌐 Multiplataforma**: Compatível com Windows, macOS e Linux

## 💻 Technology Stack

<div align="center">

| Tecnologia          | Descrição                                  |
|---------------------|-------------------------------------------|
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"> Python | Linguagem base do projeto |
| <img src="https://gemini.google.com/static/images/gemini-favicon.png" width="40"> Google Gemini API | Geração de respostas inteligentes |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/discord/discord-original.svg" width="40"> Discord.py | Integração com Discord |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/json/json-original.svg" width="40"> JSON | Configurações e armazenamento |

</div>

## ⚡ Configuração Rápida

### 📋 Pré-requisitos

- Python 3.7+
- Conta de desenvolvedor no Discord
- Chave de API da Gemini

### 🛠️ Passos de Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/leandrowanderley/Gemini-Discord-Bot
    cd Gemini-Discord-Bot
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `config.json` com o seguinte formato:

    ```bash
    {
        "discord_token": "SEU_TOKEN_DO_BOT_DO_DISCORD",
        "gemini_api_key": "SUA_CHAVE_DE_API_GEMINI"
    }
    ```

5. Crie um arquivo `prompts.json` e `mensagens.json`:
Você deve criar esses arquivos `.json`, pois eles possuem uma função específica para a personalidade que eu quero que o Gemini use, e mensagens pré feitas para que ele envie na dm dos usuário, como pode ser visto no código. Caso você queira coloca-los basta criar ambos os arquivos assim

    ```bash
    # prompts.json
    {
        "prompt1": "Você é o FalAI, um assistente...",
        "prompt2": "Responda de forma amigável..."
    }
    
    # mensagens.json
    {
        "mensagens": [
            "Bem-vindo ao servidor!",
            "Como posso te ajudar hoje?"
        ]
    }
    ```

6. Execute o bot:

    ```bash
    python run.py
    ```

## 📜 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE.txt) para detalhes.

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE.txt) file for details.

<div align="center">
  <img src="icon.png" alt="FalAI Icon" width="100">
</div>
