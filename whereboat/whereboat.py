import re
import aiohttp
from bs4 import BeautifulSoup
from redbot.core import commands
import discord


class whereboat(commands.Cog):

    """Fetches AAUCARGO.INFO"""


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.base_url = "http://aaucargo.info"
        self.session = aiohttp.ClientSession()
        self.header = {"User-Agent": "ShibeCogs/3.0"}

    @commands.command()
    async def whereboat(self, ctx):
        """gets boat location"""
        results = []
        url = self.base_url
        async with self.session.get(url, headers=self.header) as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
        datah1 = soup.find('h1')
        datah2 = soup.find('h2')
        datah3 = soup.find('h3')
        output = datah1 + datah2 + datah3
        await ctx.send(output)
