import discord
import csv
import random

rawJokes = csv.reader(open('assets/jokes.csv', 'r'))
jokes = sum([i for i in rawJokes],[])

TOKEN = 'NjgyMzI5OTA1ODk5NjM0NzMz.XlbbfQ.b5nto8lGAwhXeNxWjLCxoxcgiaM'

client = discord.Client()

@client.event


async def on_message(message):
     if message.author == client.user:
        return

     if message.content.lower() == "$joke":
          await message.channel.send(random.choice(jokes))

     if message.content.lower() == "$propaganda":
          for i in range(15):
               await message.channel.send("@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
               await message.channel.send(file=discord.File('assets/flag.png'))
               await message.channel.send("Join us: https://discord.gg/arvVft4")

@client.event
async def on_ready():
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('------')


client.run(TOKEN)

