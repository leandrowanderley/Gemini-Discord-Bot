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

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv .venv
    # Ative o ambiente virtual
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt

4. Crie um arquivo `config.json` com o seguinte formato:

    ```bash
    {
        "discord_token": "SEU_TOKEN_DO_DISCORD",
        "gemini_api_key": "SUA_CHAVE_DE_API_GEMINI"
    }

Onde tem `SEU_TOKEN_DO_DISCORD` coloque o Token do Bot do Discord.
E onde tem `SUA_CHAVE_DE_API_GEMINI` coloque a Key da API do Gemini.

5. Execute o bot:

    ```bash
    python main.py


## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
