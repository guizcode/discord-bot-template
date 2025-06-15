import discord
from discord.ext import commands

class Filtered_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
          if message.author.bot:
              return
          if message.content.lower() == "example":
              await message.delete()
              await message.channel.send("This message is blocked on the server.")
              return
          ctx = await self.bot.get_context(message)
          if ctx.valid:
              return
          await self.bot.process_commands(message)
        except Exception as e:
            print(f'Error: {e}') 


async def setup(bot):
    await bot.add_cog(Filtered_message(bot))