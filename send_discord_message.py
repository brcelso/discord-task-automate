import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Pegando os valores das variáveis do ambiente (GitHub Secrets)
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

# Verificar se as variáveis foram carregadas corretamente
if not TOKEN or not CHANNEL_ID:
    raise ValueError("As variáveis de ambiente DISCORD_BOT_TOKEN ou DISCORD_CHANNEL_ID não foram encontradas.")

# Configurar o bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.send('Olá! Lembre-se de dar comida para os Dogs!')
            print(f'Mensagem enviada para o canal {channel.name}.')
        except Exception as e:
            print(f'Erro ao enviar mensagem: {e}')
    else:
        print('Canal não encontrado.')

    # Encerrar o bot após enviar a mensagem
    await bot.close()

# Iniciar o bot
bot.run(TOKEN)
