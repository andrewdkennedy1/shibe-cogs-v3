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
        data = soup.find_all('h3')
        h3 = data[0].text
        await ctx.send(h3)
