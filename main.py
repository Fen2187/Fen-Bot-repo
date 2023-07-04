import discord
import random

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

  if ctx.content.startswith('/ur fat'):
    await ctx.channel.send("Your fat32 you can't store files over 4GB😎")

  if ctx.content.startswith('/bank'):
    await ctx.channel.send('You robbed money from the Fen bank!!!')

  if ctx.content.startswith('the discord mods'):
    await ctx.channel.send('Nooooooooo!!!!!!!!')

  if ctx.content.startswith('android is better'):
    await ctx.channel.send('Android sucks. oh you use Android LoL')
    await ctx.channel.send('LoL')
    await ctx.channel.send('LoL')
    await ctx.channel.send('LoL')

  if ctx.content.startswith('/play'):
    await ctx.channel.send('Ok guys play in five minutes')
  
  #DnD dice help thing
  if ctx.content.startswith('/DnD-help'):
    await ctx.channel.send('What can Sir Fen AI do to help')

  if ctx.content.startswith('/DnD-roll6'):
    await ctx.channel.send(random.randint(1, 6))

  if ctx.content.startswith('/DnD--roll6'):
    await ctx.channel.send(random.randint(1, 6))
    await ctx.channel.send(random.randint(1, 6))

  if ctx.content.startswith('/DnD---roll6'):
    await ctx.channel.send(random.randint(1, 6))
    await ctx.channel.send(random.randint(1, 6))
    await ctx.channel.send(random.randint(1, 6))

  if ctx.content.startswith('/DnD----roll6'):
    await ctx.channel.send(random.randint(1, 6))
    await ctx.channel.send(random.randint(1, 6))
    await ctx.channel.send(random.randint(1, 6))
    await ctx.channel.send(random.randint(1, 6))

  if ctx.content.startswith('/DnD-roll20'):
    await ctx.channel.send(random.randint(1, 20))

  if ctx.content.startswith('/DnD--roll20'):
    await ctx.channel.send(random.randint(1, 20))
    await ctx.channel.send(random.randint(1, 20))

  if ctx.content.startswith('/DnD-roll80'):
    await ctx.channel.send(random.randint(00, 80)('Just simplify the number, example 64 = 60 or 17 = 20'))
client.run('')
