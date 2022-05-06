import discord
from redbot.core import commands, Config, checks
import aiohttp
from redbot.core.utils.menus import menu, commands, DEFAULT_CONTROLS

BaseCog = getattr(commands, "Cog", object)

class status(BaseCog):
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
        activity = ("Chilling in {} status").format(member.status)

        status_string = "No Custom Status Dectected"

        for s in member.activities:
            if isinstance(s, discord.CustomActivity):
                status_string = s

        name = str(member)
        name = " ~ ".join((name, member.nick)) if member.nick else name

        embed = discord.Embed()
        embed.title = name
        embed.colour = member.colour
        embed.add_field(name="What Doing?", value=activity)
        embed.add_field(name="Custom Status", value=status_string)
        embed.set_thumbnail(url=member.avatar_url_as(static_format="png"))

        await ctx.send(embed=embed)
