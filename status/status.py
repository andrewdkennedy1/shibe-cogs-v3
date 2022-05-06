import asyncio
import re
import io
import discord
import requests
from redbot.core import commands


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


        names, nicks = await self.get_names_and_nicks(member)

        joined_at = member.joined_at
        voice_state = member.voice
        member_number = (
            sorted(guild.members, key=lambda m: m.joined_at or ctx.message.created_at).index(
                member
            )
            + 1
        )

        created_on = (
            f"{discord.utils.format_dt(member.created_at)}\n"
            f"{discord.utils.format_dt(member.created_at, 'R')}"
        )
        if joined_at is not None:
            joined_on = (
                f"{discord.utils.format_dt(joined_at)}\n"
                f"{discord.utils.format_dt(joined_at, 'R')}"
            )
        else:
            joined_on = _("Unknown")

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
        status_string = self.get_status_string(member)

        data = discord.Embed(description=status_string or activity, colour=member.colour)
        data.set_footer(text=_("Member #{} | User ID: {}").format(member_number, member.id))

        name = str(member)
        name = " ~ ".join((name, member.nick)) if member.nick else name
        name = filter_invites(name)

        avatar = member.display_avatar.replace(static_format="png")
        data.set_author(name=f"{statusemoji} {name}", url=avatar)
        data.set_thumbnail(url=avatar)

        await ctx.send(embed=data)
