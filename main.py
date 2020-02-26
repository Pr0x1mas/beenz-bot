import discord
import csv
import random

rawJokes = csv.reader(open('jokes.csv', 'r'))
jokes = sum([i for i in rawJokes],[])

TOKEN = 'NjgyMzI5OTA1ODk5NjM0NzMz.XlbbfQ.b5nto8lGAwhXeNxWjLCxoxcgiaM'

client = discord.Client()

@client.event


async def on_message(message):
     if message.author == client.user:
        print(" ")
        return

     if message.content == "$joke":
          await message.channel.send(random.choice(jokes))

@client.event
async def on_ready():
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('------')


client.run(TOKEN)

