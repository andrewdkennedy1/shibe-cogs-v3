import asyncio
import re
import io
import discord
import requests
from datetime import datetime
from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class status(commands.Cog):
    """gib status pls"""

    @commands.command(pass_context=True)
    async def status(ctx, member: Member):
        await bot.say(str(member.status))
