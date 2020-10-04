import aiohttp
import asyncio
import logging

from redbot.core import commands

class villager(commands.Cog):
    """villager"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__url: str = "https://nookipedia.com/wiki/"
        self.__session = aiohttp.ClientSession()

    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

    @commands.command()
    async def villager(self, ctx):
        """villager"""
        await ctx.trigger_typing()
        await ctx.send(self.__url+ctx)
        
