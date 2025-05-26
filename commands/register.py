import discord
from discord.ext import commands

import sqlite3

class Register(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.connection = sqlite3.connect('data/users.db')
    self.cursor = self.connection.cursor()
    
  @commands.hybrid_command(name='register', description='Register your username and user id in database.')
  async def registrar(self, ctx):
    try:
      user_id = ctx.author.id
      user_name = ctx.author.display_name
      
      self.cursor.execute('INSERT INTO users (user_id, user_name) VALUES (?, ?)',(user_id, user_name,))
      self.connection.commit()
  
      await ctx.reply(f'{ctx.author.mention}, successfully registered.')
    except sqlite3.IntegrityError:
      await ctx.reply('You are already registered.')
    except Exception:
      await ctx.reply('Error.')
  
  
  def cog_unload(self):
    self.connection.close()
      
      
async def setup(bot):
  await bot.add_cog(Register(bot))