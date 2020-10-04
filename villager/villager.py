import aiohttp
import asyncio
import logging

from redbot.core import commands

class villager(commands.Cog):
    """villager"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @commands.command()
    async def villager(self,ctx, *, villager):
        """villager"""
        await ctx.trigger_typing()
        villager = {quote(villager)}
        villager.replace(" ", "_")
        await ctx.send("https://nookipedia.com/wiki/" + villager)
