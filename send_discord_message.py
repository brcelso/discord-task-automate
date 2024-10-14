import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente (não será necessário se estiver usando o GitHub Actions diretamente)
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
            await channel.send('Olá! Esta é uma mensagem automatizada do GitHub Actions.')
            print(f'Mensagem enviada para o canal {channel.name}.')
        except Exception as e:
            print(f'Erro ao enviar mensagem: {e}')
    else:
        print('Canal não encontrado.')

# Iniciar o bot
bot.run(TOKEN)
