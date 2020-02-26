import discord

TOKEN = 'NjgyMzI5OTA1ODk5NjM0NzMz.XlbbfQ.b5nto8lGAwhXeNxWjLCxoxcgiaM'

client = discord.Client()

@client.event


async def on_message(message):
     if message.author == client.user:
        return


@client.event
async def on_ready():
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('------')


client.run(TOKEN)

