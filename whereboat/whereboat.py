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
        h1 = datah1.h1.text
        h2 = datah2.h2.text
        h3 = datah3.h4.text
        output = h1 + h2 + h3
        await ctx.send(output)
