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
        status = data[0].text
        leavetime = data[1].text
        nextport =data[2].text
        em=discord.Embed(title="WHERE BOAT!?", url="http://aaucargo.info/", description=status + ' ' + leavetime , color=0xFF5733)
        await ctx.send(embed=em)
