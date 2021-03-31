import re
import aiohttp
from bs4 import BeautifulSoup
from redbot.core import commands
import discord


class whereboat(commands.Cog):

    """Fetches AAUCARGO.INFO"""


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.base_url = "http://aaucargo.info/"
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def whereboat(self, ctx):
        """gets boat location"""
        results = []
        url = self.base_url
        async with self.session.get(url) as response:
            boatinfo = BeautifulSoup(await response.text(), "html.parser")
            output = boatinfo.find('h1'+'h2'+'h3')
            em = discord.Embed(title='Where Boat', description=output, colour=0xFFD966)
        await ctx.send(em)
