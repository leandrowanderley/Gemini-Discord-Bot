# Discord Bot com Gemini

Este repositório contém um bot do Discord desenvolvido em Python que utiliza a API Gemini para interações conversacionais. O bot é projetado para responder a mensagens dos usuários com base em um histórico de conversas, permitindo diálogos mais naturais e contextuais.

## Funcionalidades

- **Interação Conversacional**: O bot utiliza a API Gemini para gerar respostas baseadas nas mensagens anteriores.
- **Histórico de Mensagens**: O bot mantém um histórico das últimas 10 mensagens e respostas para proporcionar continuidade nas conversas.
- **Fácil Configuração**: Configurações personalizáveis através de um arquivo `config.json`, incluindo tokens de acesso e parâmetros de geração de mensagens.

## Tecnologias Utilizadas

- Google Gemini API
- Python
- Discord.py
- Json

## Como Começar

### Pré-requisitos

- Python 3.7 ou superior
- Conta no Discord para criar um bot
- Token do Bot do Discord
- Key de API da Gemini

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/leandro-odev/BotDiscord
   cd BotDiscord
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv .venv
    # Ative o ambiente virtual
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
        "discord_token": "SEU_TOKEN_DO_DISCORD",
        "gemini_api_key": "SUA_CHAVE_DE_API_GEMINI"
    }
    ```

5. Crie um arquivo `prompts.json` e `mensagens.json`:
Você deve criar esses arquivos `.json`, pois eles possuem uma função específica para a personalidade que eu quero que o Gemini use, e mensagens pré feitas para que ele envie na dm dos usuário, como pode ser visto no código. Caso você queira coloca-los basta criar ambos os arquivos assim

    ```bash
    // prompts.json
    {
        "prompt1": "Prompt 1",
        "prompt2": "Prompt 2"
    }
    
    // mensagens.json
    {
    "mensagens": [
            "Mensagem 1",
            "Mensagem 2",
            "Mensagem 3",
            "..."
        ]
    }
    ```

6. Execute o bot:

    ```bash
    python main.py
    ```

EXTRA. Fazer um executável para o bot:
Caso queira, faça um executável com esse comando.

```bash
python -m PyInstaller --onefile --icon=../icon.png bot.py --hidden-import google --hidden-import google.generativeai
```

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE.txt) para detalhes.
