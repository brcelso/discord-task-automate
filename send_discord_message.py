import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Pegando os valores das variáveis do ambiente (GitHub Secrets)
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID_1 = int(os.getenv('DISCORD_CHANNEL_ID_1'))
CHANNEL_ID_2 = int(os.getenv('DISCORD_CHANNEL_ID_2'))

# Verificar se as variáveis foram carregadas corretamente
if not TOKEN or not CHANNEL_ID_1 or not CHANNEL_ID_2:
    raise ValueError("As variáveis de ambiente DISCORD_BOT_TOKEN, DISCORD_CHANNEL_ID_1 ou DISCORD_CHANNEL_ID_2 não foram encontradas.")

# Configurar o bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

    # Enviar mensagem para o primeiro canal
    channel_1 = bot.get_channel(CHANNEL_ID_1)
    if channel_1:
        try:
            await channel_1.send('Olá! \nLembre-se de dar comida para os Dogs, \nTreino da Re, \nTreino Spy e \nTira o foco, \nLavar Carro Sexta 08h, \nImprimir material ET!')
            print(f'Mensagem enviada para o canal {channel_1.name}.')
        except Exception as e:
            print(f'Erro ao enviar mensagem para o canal {channel_1.name}: {e}')
    else:
        print('Canal 1 não encontrado.')

    # Enviar mensagem para o segundo canal
    channel_2 = bot.get_channel(CHANNEL_ID_2)
    if channel_2:
        try:
            await channel_2.send('Olá! \nLembre-se de dar comida para os Dogs, \nTreino da Re, \nTreino Spy e \nTira o Foco, \nLavar Carro Sexta 08h, \nImprimir Material ET!\!')
            print(f'Mensagem enviada para o canal {channel_2.name}.')
        except Exception as e:
            print(f'Erro ao enviar mensagem para o canal {channel_2.name}: {e}')
    else:
        print('Canal 2 não encontrado.')

    # Encerrar o bot após enviar as mensagens
    await bot.close()

# Iniciar o bot
bot.run(TOKEN)
