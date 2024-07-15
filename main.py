import pydirectinput as keys 
import time
import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
#import pygetwindow as gw
#title = 'Grand Theft Auto: San Andreas – The Definitive Edition  '

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

keys_held = {
    'w' : False, 
    's' : False, 
    'a' : False, 
    'd' : False, 
}



async def hold_key(time, key_chars):
    for key_char in key_chars:
        keys_held[key_char] = True
        keys.keyDown(key_char)
    await asyncio.sleep(time)
    for key_char in key_chars:
        keys.keyUp(key_char)
        keys_held[key_char] = False 


async def run_input_task(time, key_chars):
    await hold_key(time, list(key_chars))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if len(message.content.split(' ')) > 2:
        return

    if message.author == client.user:
        return

    if message.channel.id != 1262326547658969119:
        return

    if message.content == 'help':
        await message.channel.send(file = discord.File('help.png'))

    if not message.content[0] in ['w', 'a', 's', 'd', 't']:
        return

    mode = len(message.content.split(' '))
    arg = int(message.content.split(" ")[1]) if mode == 2 else  None

    if message.content == 'tr':
        if not keys_held['w'] and not keys_held['d']:
            await run_input_task(1.1, ['w', 'd'])

    if message.content == 'tl':
        if not keys_held['w'] and not keys_held['a']:
            await run_input_task(1.1, ['w', 'a'])

                  

    if message.content.startswith('w'):
        if not keys_held['w']:
            if mode == 1:
                x = message.content.count('w')
                await run_input_task(x * 0.25, 'w')
            else:
                await run_input_task(arg, 'w')
        
    
    if message.content.startswith('s'):
        if not keys_held['s']:
            if mode == 1:
                x = message.content.count('s')
                await run_input_task(x * 0.25, 's')
            else:
                await run_input_task(arg, 's')
        
    
    if message.content.startswith('d'):
        if not keys_held['d']:
            if mode == 1:
                x = message.content.count('d')
                await run_input_task(x * 0.25 * 0.5, 'd')
            else:
                await run_input_task(arg, 'd')
        
            
    if message.content.startswith('a'):
        if not keys_held['a']:
            if mode == 1:
                x = message.content.count('a')
                await run_input_task(x * 0.25 * 0.5, 'a')
            else:
                await run_input_task(arg, 'a')
        
           

client.run(os.getenv('TOKEN'))
