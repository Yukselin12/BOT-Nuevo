import discord
from discord.ext import commands
from bot_logic import get
from sintexis import speak
intents = discord.Intents.default()
intents.message_content = True  # Para leer mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# Manejador de comando !start
@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que anuncia el pronóstico del tiempo.")

@bot.command()
async def dato(ctx):
    dato = get()
    speak(dato)
    await ctx.send(dato)

bot.run("token")