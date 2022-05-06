
import asyncio
from collections import deque, defaultdict, namedtuple

import discord

from redbot.core import checks, Config, modlog, commands
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n
from redbot.core.utils.chat_formatting import box, escape

_ = Translator("Mod", __file__)

# Classname should be CamelCase and the same spelling as the folder
class status(commands.Cog):
    """gib status pls"""

    @commands.command(pass_context=True)
    async def status(self, ctx, *, member: discord.Member = None):
        """gib status"""
        author = ctx.author
        guild = ctx.guild

        if not member:
            member = author

        if any(a.type is discord.ActivityType.streaming for a in member.activities):
            statusemoji = "\N{LARGE PURPLE CIRCLE}"
        elif member.status.name == "online":
            statusemoji = "\N{LARGE GREEN CIRCLE}"
        elif member.status.name == "offline":
            statusemoji = "\N{MEDIUM WHITE CIRCLE}\N{VARIATION SELECTOR-16}"
        elif member.status.name == "dnd":
            statusemoji = "\N{LARGE RED CIRCLE}"
        elif member.status.name == "idle":
            statusemoji = "\N{LARGE ORANGE CIRCLE}"
        activity = _("Chilling in {} status").format(member.status)

        for s in member.activities:
            if isinstance(s, discord.CustomActivity):
                status_string = s

        data = discord.Embed(description=status_string or activity, colour=member.colour)
        name = str(member)
        name = " ~ ".join((name, member.nick)) if member.nick else name
        await ctx.send(embed=data)
