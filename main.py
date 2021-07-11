import discord, time, librosa
from discord import FFmpegPCMAudio
from os import listdir
from os.path import isfile, join
from sys import platform

client = discord.Client()

sound_list = [f"sounds/{sound}" for sound in listdir('sounds') if isfile(join('sounds', sound))]
sounds_name_with_ext = [sound for sound in listdir('sounds') if isfile(join('sounds', sound))]
sounds_name = [ element.split('.mp3')[0] for element in  sounds_name_with_ext ]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in sounds_name:
        await join(message.author, message.content)

@client.event
async def join(member : discord.Member,msg):
    channel = member.voice.channel
    if channel: 
        voice = await channel.connect() 
        source = FFmpegPCMAudio(f'sounds/{msg}.mp3')
        player = voice.play(source)
    time.sleep(librosa.get_duration(filename=(f'sounds/{msg}.mp3')))
    await voice.disconnect()


client.run('Insert Your Token')