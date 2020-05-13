import asyncio
import re
import io
import discord
from datetime import datetime
from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class description(commands.Cog):
    """Describe the channel"""

    @commands.command(pass_context=True)
    async def description(self, ctx):
        """[p]description"""
        embed = discord.Embed(title='Message from: %s' % (bot.self.channel), description='', color=0x00ff00)
        embed.set_author(name="ShibeBot", url=bot.self.avatar_url, icon_url=bot.self.avatar_url)
        embed.add_field(name='Message', value=bot.self.channel.description)
        await target_channel.send('', embed=embed)
