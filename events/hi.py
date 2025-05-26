import discord
from discord.ext import commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      try:
        if message.author.bot:
            return
        if message.content.lower() == 'Hi bot':
            await message.reply('Hi!')
        ctx = await self.bot.get_context(message)
        if ctx.valid:
            return
        await self.bot.process_commands(message)
      except Exception as e:
        print(f'Error: {e}')


async def setup(bot):
    await bot.add_cog(Hi(bot))