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
        embed = discord.Embed(title=' Description of: %s' % (self.channel), description='', color=0x00ff00)
        embed.set_author(name="ShibeBot", url=self.avatar_url, icon_url=self.avatar_url)
        embed.add_field(name='Description', value=self.channel.description)
        await target_channel.send('', embed=embed)
