import discord
import os
from discord.ext import commands

# Configurações do bot
TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Token do bot via variável de ambiente
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))  # Canal via variável de ambiente

# Inicializar o bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online!')

# Função para enviar a mensagem
async def enviar_mensagem():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Lembrete diário: Não esqueça de realizar sua tarefa!")
    await bot.close()

# Iniciar o bot e enviar a mensagem
if __name__ == "__main__":
    bot.loop.create_task(enviar_mensagem())
    bot.run(TOKEN)
