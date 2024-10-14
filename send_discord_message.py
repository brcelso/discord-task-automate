import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Definir as variáveis de ambiente
TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Token do bot
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))  # Canal via variável de ambiente

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

    try:
        # Obter o canal
        print(f"Tentando encontrar o canal com ID {CHANNEL_ID}...")
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            print(f"Canal encontrado: {channel.name}. Enviando mensagem...")
            await channel.send("Lembrete diário: Não se esqueça de realizar sua tarefa!")
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Canal com ID {CHANNEL_ID} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
    finally:
        print("Encerrando bot...")
        await bot.close()

if __name__ == "__main__":
    print("Iniciando bot...")
    print(f"DISCORD_BOT_TOKEN: {TOKEN[:5]}********")
    print(f"DISCORD_CHANNEL_ID: {CHANNEL_ID}")
    asyncio.run(bot.start(TOKEN))
