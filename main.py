import discord
import random
import requests
import json
import server
from keep_alive import keep_alive
import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#random stuff
version = '2.2'
host = 'how hosted on github'

money = random.randint(0,1000)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


##PREPROGRAMMED LINES
@client.event
async def on_message(ctx):
  if ctx.author == client.user:
    return

  #special thingse
  if ctx.content.startswith('Happy Birthday'):
    await ctx.channel.send('Happy Birthday')

  if ctx.content.startswith('Merry Christmas'):
    await ctx.channel.send('Merry Christams')

  if ctx.content.startswith('/details'):
    await ctx.channel.send(
      'This bot was desinged to fit the needs of the user Fen2187.')
    await ctx.channel.send(
      'This bot was so he could play DnD with his friends online, play games, do dumb things.'
    )
    await ctx.channel.send(
      'The code is on a github for a respoatry for people to look at the code and intergrate it into there Python Discord bots.'
    )
    await ctx.channel.send(
      'This was a great way for others to learn Python and app development.')
    await ctx.channel.send('I hopes you and others enjoy the bot!')
    await ctx.channel.send(
      'Fen2187 reprogrammed this whole bot because of his developer badge taking away, he also did this because the old one was laking features and very outdated'
    )
    await ctx.channel.send(
      'If you have any ideas DM Fen on his GitHub repo and he may intergrate it. The key for this bot is private and is not on GitHub'
    )
    await ctx.channel.send('Hope you like me and what I do.')
    await ctx.channel.send(' - Fen Bot')

  #dumb things
  if ctx.content.startswith('hello'):
    await ctx.channel.send('Hello!')

  if ctx.content.startswith('Hello'):
    await ctx.channel.send('Hello!')

  if ctx.content.startswith('hi'):
    await ctx.channel.send('hi')

  if ctx.content.startswith('lol'):
    await ctx.channel.send('lol')

  if ctx.content.startswith('Lol'):
    await ctx.channel.send('Lol')

  if ctx.content.startswith('e'):
    await ctx.channel.send('E')

  if ctx.content.startswith('E'):
    await ctx.channel.send('E')

  #to stop from meaing mean and to roast them like a chicken
  if ctx.content.startswith('/ur fat'):
    oner = 'Your fat32 you cant store files over 4GB😎'
    twor = 'Wow you as bad as toast chicken😎'
    threer = 'Your so fat you look like a discord mod😎 lol'
    fourr = 'The christmas photo your parents took last Christmas is still printing😎 lol'
    roast = random.randint(1, 4)
    print(roast)
    if roast == 1:
      await ctx.channel.send(oner)
    if roast == 2:
      await ctx.channel.send(twor)
    if roast == 3:
      await ctx.channel.send(threer)
    if roast == 4:
      await ctx.channel.send(fourr)

  if ctx.content.startswith('/bank'):
    await ctx.channel.send('You robbed money from the Fen bank!!!')

  if ctx.content.startswith('The discord mods'):
    await ctx.channel.send('Nooooooooo!!!!!!!!')

  if ctx.content.startswith('Android is better'):
    await ctx.channel.send('Android sucks. oh you use Android LoL')
    await ctx.channel.send('LoL')
    await ctx.channel.send('LoL')
    await ctx.channel.send('LoL')

  if ctx.content.startswith('💀'):
    await ctx.channel.send('💀')

  if ctx.content.startswith('lets go'):
    await ctx.channel.send('LETS GO')

    #hacking/terminal function
  if ctx.content.startswith('lets hack'):
    await ctx.channel.send('😎')
    await ctx.channel.send('Get out that turbo keyboard man')
    await ctx.channel.send('get the hack under way')
    await ctx.channel.send('Put on some music and chill!')

  if ctx.content.startswith('/terminal'):
    await ctx.channel.send('Terminal window ' + version)

  if ctx.content.startswith('ip-address'):
    ip1g = random.randint(10, 40)
    ip2g = random.randint(1, 9)
    ip3g = random.randint(0, 10)
    ip4g = random.randint(0, 11)
    ip = str(ip1g) + '.' + str(ip2g) + '.' + str(ip3g) + '.' + str(ip4g)

    await ctx.channel.send(ip)

  if ctx.content.startswith('dehash'):
    await ctx.channel.send('[Dehashing] online')
    await ctx.channel.send('hash please')
  if ctx.content.startswith(server.hash):
    await ctx.channel.send(server.user)
    await ctx.channel.send(server.password)
    await ctx.channel.send(server.ip)

  if ctx.content.startswith('ping-ip'):
    await ctx.channel.send('[ip]:')

  if ctx.content.startswith('hash_challange'):
    await ctx.channel.send(server.hash)

  if ctx.content.startswith(server.ip):
    await ctx.channel.send('root->')
    await ctx.channel.send('password')

  if ctx.content.startswith(server.password):

    money = random.randint(0,1000)
    
    await ctx.channel.send('Congrats you hacked ' + server.ip + ' you were able to collect there data and sell it for $' + str(money))

  
  
  #DnD dice help thing
  if ctx.content.startswith('/D&D-help'):
    await ctx.channel.send('What can Sir Fen AI do to help')
    await ctx.channel.send(
      'To roll dice do /D&D and the - roll and the sided die.')
    await ctx.channel.send('I guess you are now on your own fair well.')

  if ctx.content.startswith('/D&D-roll6'):
    await ctx.channel.send(random.randint(1, 6))

  if ctx.content.startswith('/D&D-roll20'):
    await ctx.channel.send(random.randint(1, 20))

  if ctx.content.startswith('/D&D-roll80'):
    await ctx.channel.send(random.randint(00, 80))

  if ctx.content.startswith('/D&D-rollD4'):
    await ctx.channel.send(random.randint(1, 4))
    await ctx.channel.send(random.randint(1, 4))
    await ctx.channel.send(random.randint(1, 4))

  if ctx.content.startswith('/D&D-roll8'):
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


keep_alive()
client.run('')
