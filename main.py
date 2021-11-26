import os

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

from discord.ext import commands
from connectDB import config
from method import discord_common

token = config.config.get("DISCORD_TOKEN")
def setup():
    if os.path.exists('database') is False:
        os.mkdir('database')

setup()


# bot
bot = commands.Bot(command_prefix='h32>>')
bot.load_extension("command.General")
bot.load_extension("command.Handle")
# bot.load_extension("command.Room")
bot.load_extension("command.Problems")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    print(error)
    await ctx.send(embed=discord_common.embed_alert(error))

@bot.event
async def on_error(event, *args, **kwargs):
    # print(event)
    pass

bot.run(token)
