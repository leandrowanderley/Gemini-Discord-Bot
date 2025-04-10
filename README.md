# FalAI - Assistente Inteligente para Discord com Gemini

<div align="center">
  <img src="imgs/banner.png" alt="Banner do FalAI" width="340">
  
  *Conectando comunidades através de conversas inteligentes*
  
  <img src="imgs/logo-lw.png" alt="Logo LW (Leandro Wanderley)" width="200">
  
  *Made by: LW (Leandro Wanderley)*
</div>

## 🚀 Funcionalidades Principais

- **🤖 Interação Conversacional**: Utiliza a API Gemini para gerar respostas contextualizadas baseadas no histórico de mensagens
- **📚 Histórico de Mensagens**: Mantém registro das últimas 10 interações para conversas mais naturais
- **⚙️ Fácil Configuração**: Personalização completa via arquivos `config.json`, `prompts.json` e `mensagens.json`
- **🌐 Multiplataforma**: Compatível com Windows, macOS e Linux

## 💻 Technology Stack

<div align="center">

<table>
  <tr>
    <th>Tecnologia</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td align="center">
      <img src="imgs/icon-python.svg" height="40"><br>
      <strong>Python</strong>
    </td>
    <td align="center">Linguagem base do projeto</td>
  </tr>
  <tr>
    <td align="center">
      <img src="imgs/icon-gemini.png" height="40"><br>
      <strong>Google Gemini API</strong>
    </td>
    <td align="center">Geração de respostas inteligentes</td>
  </tr>
  <tr>
    <td align="center">
      <img src="imgs/icon-discord.jpg" height="40"><br>
      <strong>Discord.py</strong>
    </td>
    <td align="center">Integração com Discord</td>
  </tr>
  <tr>
    <td align="center">
      <img src="imgs/icon-json.svg" height="40"><br>
      <strong>JSON</strong>
    </td>
    <td align="center">Configurações e armazenamento</td>
  </tr>
</table>

</div>


<!-- <div align="center">

| Tecnologia          | Descrição                                  |
|---------------------|-------------------------------------------|
| <img src="imgs/icon-python.svg" width="40"> Python | Linguagem base do projeto |
| <img src="imgs/icon-gemini.png" width="40"> Google Gemini API | Geração de respostas inteligentes |
| <img src="imgs/icon-discord.jpg" width="40"> Discord.py | Integração com Discord |
| <img src="imgs/icon-json.svg" width="40"> JSON | Configurações e armazenamento |

</div> -->

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
  <img src="imgs/icon.png" alt="FalAI Icon" width="100">
</div>
