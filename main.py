import discord
from discord.ext import commands
import requests
import os

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ff(ctx, uid: str):
    url = f"https://free-fire-api-six.vercel.app/api/v1/info?region=ind&uid={uid}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            embed = discord.Embed(title="Free Fire Info", color=0xff4500)
            embed.add_field(name="Name", value=data.get('nickname', 'N/A'))
            embed.add_field(name="Level", value=data.get('level', 'N/A'))
            await ctx.send(embed=embed)
        else:
            await ctx.send("Player not found!")
    except:
        await ctx.send("API Error!")

bot.run(TOKEN)
