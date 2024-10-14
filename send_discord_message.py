import discord
import os
import asyncio
from discord.ext import commands

# Definir as variáveis de ambiente
TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Token do bot
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))  # Canal via variável de ambiente

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True  # Habilitar a intent de leitura de conteúdo das mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

    # Obter o canal pelo ID
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Lembrete diário: Não se esqueça de realizar sua tarefa!")
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Canal com ID {CHANNEL_ID} não encontrado.")

    # Fechar o bot após o envio da mensagem
    await bot.close()

# Função principal para iniciar o bot
if __name__ == "__main__":
    asyncio.run(bot.start(TOKEN))
