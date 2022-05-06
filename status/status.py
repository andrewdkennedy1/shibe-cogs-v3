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

        for s in member.activities:
            if isinstance(s, discord.CustomActivity):
                status_string = s

        name = str(member)
        name = " ~ ".join((name, member.nick)) if member.nick else name

        embed = discord.Embed()
        embed.title = name + "'s status"
        embed.colour = member.colour
        embed.set_footer(text="Powered by ShibeBot!")
        embed.add_field(name="", value=status_string)
        embed.set_thumbnail(url=member.avatar_url_as(static_format="png"))

        await ctx.send(embed=embed)
