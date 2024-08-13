import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sum(ctx, a, b):
    await ctx.send(int(a)+ int(b))

@bot.command()
async def sub(ctx, a, b):
    await ctx.send(int(a)- int(b))

@bot.command()
async def multi(ctx, a, b):
    await ctx.send(int(a)* int(b))

@bot.command()
async def divi(ctx, a, b):
    await ctx.send(int(a)/ int(b))

@bot.command()
async def bothelp(ctx):
    help_text = (
            "bothelp - команда Help показывает все существующие команды\n"
            "heh - если написать просто heh, бот будет смеяться\n"
            "sum - сложение двух чисел\n"
            "sub - вычитание двух чисел\n"
            "multi - умножение двух чисел\n"
            "divi - деление двух чисел\n"
        )
    await ctx.send(help_text)



bot.run("")
