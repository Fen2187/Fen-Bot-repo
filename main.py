import discord
import random as randint

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
##PREPROGRAMMED LINES
@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.content.startswith('hello'):
        await ctx.channel.send('Hello!')
    
    if ctx.content.startswith('e'):
        await ctx.channel.send('E')
    
    if ctx.content.startswith('E'):
        await ctx.channel.send('E')

    if ctx.content.startswith('ur fat'):
        await ctx.channel.send("Your fat32 you can't store files over 4GB😎")

    if ctx.content.startswith('$bank'):
            await ctx.channel.send('You robbed money from the Fen bank!!!')




client.run('MTA5MzQ5MTQ1MDkxMTY3MDMwMg.GoTy-D.haY2rSw5ytrDDT44tQhU151bRJPIh1_7_B05Rk')