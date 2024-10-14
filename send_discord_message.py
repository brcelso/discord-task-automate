import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Pegando os valores das variáveis do ambiente (GitHub Secrets)
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_IDS = os.getenv('DISCORD_CHANNEL_IDS')

# Verificar se as variáveis foram carregadas corretamente
if not TOKEN or not CHANNEL_IDS:
    raise ValueError("As variáveis de ambiente DISCORD_BOT_TOKEN ou DISCORD_CHANNEL_IDS não foram encontradas.")

# Converter os IDs de canais em uma lista de inteiros
channel_ids = [int(channel_id.strip()) for channel_id in CHANNEL_IDS.split(',')]

# Configurar o bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

    for channel_id in channel_ids:
        channel = bot.get_channel(channel_id)
        if channel:
            try:
                await channel.send('Olá! Lembre-se de dar comida para os Dogs!')
                print(f'Mensagem enviada para o canal {channel.name}.')
            except Exception as e:
                print(f'Erro ao enviar mensagem para o canal {channel.name}: {e}')
        else:
            print(f'Canal com ID {channel_id} não encontrado.')

    # Encerrar o bot após enviar as mensagens
    await bot.close()

# Iniciar o bot
bot.run(TOKEN)
