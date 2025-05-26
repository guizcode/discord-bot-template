import discord
from discord.ext import commands

import os
import json

class Connect:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        
        with open('config.json') as c:
            config = json.load(c)
            
        self.token = config['TOKEN']
        self.prefix = config['PREFIX']
        self.bot = commands.Bot(command_prefix=self.prefix, intents=intents, case_sensitive=True)
    
        self.bot.event(self.on_ready)


    async def load_pasts(self):
        for file in os.listdir('commands'):
            if file.endswith('.py'):
                await self.bot.load_extension(f'commands.{file[:-3]}')
                
        for file in os.listdir('events'):
            if file.endswith('.py'):
                await self.bot.load_extension(f'events.{file[:-3]}')
                
          
    async def on_ready(self):
        await self.load_pasts()
        await self.bot.tree.sync()
        print(f'{self.bot.user} is online.')
        
        
    def run(self):
        self.bot.run(self.token)