import discord
import utils
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

keys_held = {
    'w' : False, 
    's' : False, 
    'a' : False, 
    'd' : False, 
}

modes = ['sport', 'drive']
current_mode = 0

executor = ThreadPoolExecutor(max_workers=5)

def hold_key(keys_to_hold, times):
    for i in range(len(keys_to_hold)):
        duty_cycle = 1
        if keys_to_hold[i] == 'a' or keys_to_hold[i] == 'd':
            duty_cycle = 0.8 if current_mode == 0 else 0.4
            utils.hold_key(keys_to_hold[i], times[i], duty_cycle)
        else:
            duty_cycle = 0.8 if current_mode == 0 else 0.4
            utils.hold_key(keys_to_hold[i], times[i], duty_cycle)
            
            

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if not mod_message(message):
        return

    mode = len(message.content.lower().split(' '))
    arg = int(message.content.lower().split(" ")[1]) if mode == 2 else None

    if message.content.lower() == 'tr':
        hold_key(['w', 'd'], [1.3, 1.1])

    if message.content.lower() == 'tl':
        hold_key(['w', 'a'], [1.3, 1.1])

    # if message.content.lower().startswith('w'):
    #     if not keys_held['w']:
    #         if mode == 1:
    #             x = message.content.lower().count('w')
    #             run_input_task(x * 0.25, 'w')
    #         else:
    #             run_input_task(arg, 'w')
        
    
    # if message.content.lower().startswith('s'):
    #     if not keys_held['s']:
    #         if mode == 1:
    #             x = message.content.lower().count('s')
    #             run_input_task(x * 0.25, 's')
    #         else:
    #             run_input_task(arg, 's')
        
    
    # if message.content.lower().startswith('d'):
    #     if not keys_held['d']:
    #         if mode == 1:
    #             x = message.content.lower().count('d')
    #             run_input_task(x * 0.25 * 0.5, 'd')
    #         else:
    #             await run_input_task(arg, 'd')
        
            
    # if message.content.lower().startswith('a'):
    #     if not keys_held['a']:
    #         if mode == 1:
    #             x = message.content.lower().count('a')
    #             await run_input_task(x * 0.25 * 0.5, 'a')
    #         else:
    #             await run_input_task(arg, 'a')
        
           


async def mod_message(message):
    if not utils.check_channel(message.channel.id):
        return False

    if len(message.content.split(' ')) > 2 or len(message.content)> 20:
        return False

    if message.author == client.user:
        return False

    if message.channel.id != 1262326547658969119:
        return False

    if message.content.lower() == 'help':
        message.channel.send(file = discord.File('help.png'))
        return False
    
    if message.content.lower().startswith('mode sport'):
        current_mode = 0
        return False

    if message.content.lower().startswith('mode drive'):
        current_mode = 1
        return False

    if not message.content.lower()[0] in ['w', 'a', 's', 'd', 't']:
        return False

    return True



client.run(os.getenv('TOKEN'))