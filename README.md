# Notificação Diária no Discord

Este projeto tem como objetivo enviar uma notificação diária para um canal do Discord utilizando um bot. A notificação é programada para ser enviada automaticamente todos os dias em um horário específico.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para criar o script do bot.
- **Discord.py**: Biblioteca para interagir com a API do Discord.
- **GitHub Actions**: Para automação do envio de mensagens em horários programados.

## Configuração

### Pré-requisitos

Antes de executar o projeto, você precisa:

1. Ter uma conta no Discord.
2. Criar um bot no Discord e obter o token de autenticação.
3. Adicionar o bot ao seu servidor.
4. Criar um canal onde as notificações serão enviadas.

### Variáveis de Ambiente

Você deve configurar as seguintes variáveis de ambiente no GitHub Actions:

- `DISCORD_BOT_TOKEN`: Token do bot do Discord.
- `DISCORD_CHANNEL_ID`: ID do canal do Discord onde as notificações serão enviadas.

### Instalação das Dependências

As dependências necessárias podem ser instaladas utilizando o `pip`. Execute os seguintes comandos:

```bash
pip install discord.py python-dotenv
