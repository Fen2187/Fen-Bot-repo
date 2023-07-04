import discord
import random
import requests
import json 
from keep_alive import keep_alive


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

  #special things
  if ctx.content.startswith('Happy Birthday'):
    await ctx.channel.send('Happy Birthday' + 'From {client.user}')

  if ctx.content.startswith('Merry Christmas'):
    await ctx.send('Merry Christams')

    if ctx.content.startswith('/details'):
      await ctx.channel.send('This bot was desinged to fit the needs of the user Fen2187')
      await ctx.channel.send('This bot was so he could play DnD with his friends online, play games, do dumb things')
      await ctx.channel.send('The code is on a github for a respoatry for people to look at the code and intergrate it into therePython Discord bots')
      await ctx.channel.send('This was a great way for him to learn Python and app development')
      await ctx.channel.send('He hopes you and others enjoy the bot')
      await ctx.channel.send('Fen2187 reprogrammed this whole bot because of his developer badge taking away, he also did this because the old one was laking features and very outdated')
      await ctx.channel.send('If you have any ideas DM me on my GitHub repo and i may intergrate it. The key for this bot is private and is not on GitHub')
      await ctx.channel.send('Hope you like me and what I do {client.user}')
  
  
  #dumb things
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

  if ctx.content.startswith('💀'):
    await ctx.channel.send('💀')

  
  #DnD dice help thing
  if ctx.content.startswith('/DnD-help'):
    await ctx.channel.send('What can Sir Fen AI do to help')
    await ctx.channel.send('Just do /DnD to call dnd command, use - example - = 1 dice roll ---- = 4 dice roll and then add the numbers on the dice at the end example 6 = 6 sided dice')

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

  if ctx.content.startswith('/DnD-rollD4'):
    await ctx.channel.send(random.randint(1, 4))

  if ctx.content.startswith('/DnD-roll8'):
    await ctx.channel.send(random.randint(1, 8))
    
  if ctx.content.startswith('/DnD-roll8'):
    await ctx.channel.send(random.randint(1, 8))

  #gaming commands
  if ctx.content.startswith('/game?'):
    one = '-Valorant'
    two = '-Minecraft'
    three = '-Fortnite'
    four = '-Stormworks'
    five = '-KSP (Kerbal Space Program)'
    six = '-League Of Legends'
    seven = '-Mario Karts'
    eight = '-Zelda Breath of the Wild'
    nine = '-Zelda Tears of the Kingdoms'
    ten = '-Halo'
    eleven = '-Terrara'

    game = random.randint(1, 11)
    print(game)
    if game == 1:
      await ctx.channel.send(one)
    if game == 2:
      await ctx.channel.send(two)
    if game == 3:
      await ctx.channel.send(three)
    if game == 4:
      await ctx.channel.send(four)
    if game == 5:
      await ctx.channel.send(five)
    if game == 6:
      await ctx.channel.send(six)
    if game == 7:
      await ctx.channel.send(seven)
    if game == 8:
      await ctx.channel.send(eight)
    if game == 9:
      await ctx.channel.send(nine)
    if game == 10:
      await ctx.channel.send(ten)
    if game == 11:
      await ctx.channel.send(eleven)

  if ctx.content.startswith('/play-time'):
    await ctx.channel.send(random.randint(1, 10) + 'Minutes and then we will call')
client.run('')
