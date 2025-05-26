import discord
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.hybrid_command(name='ping', description='View the bot latency.')
  async def ping(self, ctx):
    try:
      latency = round(self.bot.latency * 1000)
      await ctx.reply(f'pong! latency is: {latency} ms')
    except Exception:
      await ctx.reply('Error.')
      
    
async def setup(bot):
  await bot.add_cog(Ping(bot))