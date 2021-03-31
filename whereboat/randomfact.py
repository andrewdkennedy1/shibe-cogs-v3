import re

import aiohttp
from bs4 import BeautifulSoup
from redbot.core import commands


class whereboat(commands.Cog):

    """Fetches AAUCARGO.INFO"""

    def __init__(self, bot):
        self.bot = bot
        self.base_url = "http://aaucargo.info/"
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    @commands.command()
    async def whereboat(self, ctx):
        """gets boat location"""
        results = []
        url = self.base_url
        async with self.session.get(url) as response:
            boatinfo = BeautifulSoup(await response.text(), "html.parser")
            output = boatinfo.find('h1'+'h2'+'h3')
        await ctx.send("```" + output + "```")
