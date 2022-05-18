import discord
from dotenv import load_dotenv
import os
# import utils
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='??',
                   case_insensitive=False)

@bot.event
async def on_ready():
    print('Connecté sans souci !')
    return


# @bot.event
# async def on_message(message):
#     if not message.author.bot:
#         await message.channel.send(message.content)
#     return


@bot.command()
async def echo(ctx, *arg):
    channel = bot.get_channel(976233370814120009)
    if not ctx.author.bot:
        await channel.send(arg[0])
    return

@bot.command()
async def echo_ping(ctx, *arg):
    channel = bot.get_channel(976233370814120009)
    if not ctx.author.bot:
        await channel.send(f"<@{arg[0]}> {arg[1]}")
    return

# @bot.command()
# async def somme(ctx, *arg):
#     if not ctx.author.bot:
#         await ctx.channel.send(utils.somme(arg))
#     return


bot.run(TOKEN)