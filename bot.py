import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement: Bot prêt
@bot.event
async def on_ready():
    print(f'{bot.user} est connecté et prêt!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Commande slash: /ping
@bot.tree.command(name='ping', description='Retourne la latence du bot')
async def ping(interaction: discord.Interaction):
    latency = bot.latency * 1000
    await interaction.response.send_message(f'🏓 Pong! Latence: {latency:.2f}ms')

# Commande slash: /say
@bot.tree.command(name='say', description='Fait répéter le bot')
@app_commands.describe(message='Le message à répéter')
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f'💬 {message}')

# Commande slash: /user
@bot.tree.command(name='user', description='Affiche les informations de l\'utilisateur')
async def user(interaction: discord.Interaction):
    user = interaction.user
    embed = discord.Embed(title=f'Profil de {user.name}', color=discord.Color.blue())
    embed.add_field(name='ID', value=user.id, inline=False)
    embed.add_field(name='Compte créé le', value=user.created_at.strftime('%d/%m/%Y'), inline=False)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    await interaction.response.send_message(embed=embed)

# Commande slash: /help
@bot.tree.command(name='help', description='Affiche l\'aide du bot')
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title='Commandes disponibles', color=discord.Color.green())
    embed.add_field(name='/ping', value='Retourne la latence du bot', inline=False)
    embed.add_field(name='/say [message]', value='Fait répéter le bot', inline=False)
    embed.add_field(name='/user', value='Affiche tes informations', inline=False)
    embed.add_field(name='/hello', value='Salue l\'utilisateur', inline=False)
    await interaction.response.send_message(embed=embed)

# Commande slash: /hello
@bot.tree.command(name='hello', description='Salue l\'utilisateur')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'👋 Salut {interaction.user.mention}!')

# Lancer le bot
if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError('DISCORD_TOKEN non trouvé dans le fichier .env')
    bot.run(token)